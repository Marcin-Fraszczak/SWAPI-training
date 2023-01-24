import csv
from datetime import datetime
from pprint import pprint

import pandas as pd
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from . import functions, models


class HomePageView(View):
    def get(self, request):
        return render(request, 'collections/homepage.html')


class CollectionView(View):
    def get(self, request, category):

        if "pk" in request.GET:
            collection = get_object_or_404(models.Collection, pk=request.GET.get("pk"))
            filepath = functions.get_path(collection)
            df = pd.read_csv(filepath_or_buffer=filepath)
            df.index += 1
            columns = list(df.columns)
            df = df.to_html(justify="center")

            ctx = {
                "collection": collection,
                "df": df,
                "columns": columns,
            }
            return render(request, 'collections/show_collection.html', ctx)

        elif "fetch" in request.GET:
            df = functions.get_data(category)

            if category == 1:
                df = functions.transform_people(df)
            elif category == 2:
                df = functions.transform_planets(df)

            functions.write_csv(df, category)

            return redirect("pages:collection", category=category)

        collections = models.Collection.objects.filter(category=category).order_by('-created')
        ctx = {
            "category": category,
            "collections": collections,
        }
        return render(request, 'collections/collections_list.html', ctx)
