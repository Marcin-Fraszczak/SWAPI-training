import csv
from datetime import datetime
from pprint import pprint

from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from . import functions, models


class HomePageView(View):
    def get(self, request):
        return render(request, 'collections/homepage.html')


class CollectionView(View):
    def get(self, request, category):

        if "pk" in request.GET:
            collections = get_object_or_404(models.Collection, pk=request.GET.get("pk"))

            ctx = {
                "collections": collections,
            }
            return render(request, 'collections/show_collection.html', ctx)

        elif "fetch" in request.GET:
            df = functions.get_data(category)
            if category == 1:
                people_df = functions.transform_people(df)
                print(people_df)

            return redirect("pages:collection", category=category)

        collections = models.Collection.objects.filter(category=category).order_by('-created')
        ctx = {
            "category": category,
            "collections": collections,
        }
        return render(request, 'collections/collections_list.html', ctx)
