import csv
from datetime import datetime
from pprint import pprint

from django.shortcuts import render, get_object_or_404
from django.views import View
from . import functions, models


class HomePageView(View):
    def get(self, request):
        return render(request, 'collections/homepage.html')


class CollectionView(View):
    def get(self, request, category):

        if category > 6:
            category = 6
        elif category < 1:
            category = 1

        if "pk" in request.GET:
            collections = get_object_or_404(models.Collection, pk=request.GET.get("pk"))

            ctx = {
                "collections": collections,
            }
            return render(request, 'collections/show_collection.html', ctx)
        elif "fetch" in request.GET:
            functions.get_people()

        collections = models.Collection.objects.filter(category=category).order_by('-created')

        ctx = {
            "collections": collections,
        }
        return render(request, 'collections/collections_list.html', ctx)
