import csv
from datetime import datetime
from pprint import pprint

from django.shortcuts import render
from django.views import View
from . import functions

fetch_keys = ["people", "planets", "films", "species", "vehicles", "starships"]


class HomePageView(View):
    def get(self, request):
        document = functions.get_page(fetch_keys[0])
        reader = csv.reader(document)
        for row in reader:
            pprint(row, indent=4)

        # data = functions.get_data(fetch_keys[0]).get("results")[:2]
        # pprint(data, indent=4)
        # for d in data:
        #     d["edited"] = d["edited"].split("T")[0]
            # d["edited"] = datetime.fromisoformat(d["edited"])
            # d["homeworld"] = (functions.get_single_record_api(d["homeworld"])).get("name")

        ctx = {
            "document": document,
        }
        return render(request, 'pages/homepage.html', ctx)
