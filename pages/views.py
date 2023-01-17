from datetime import datetime
from pprint import pprint

from django.shortcuts import render
from django.views import View
from . import fetch

fetch_keys = ["people", "planets", "films", "species", "vehicles", "starships"]


class HomePageView(View):
    def get(self, request):
        data = fetch.get_data(fetch_keys[0])[:2]
        # pprint(data, indent=4)
        for d in data:
            # d["edited"] = d["edited"].split("T")[0]
            d["edited"] = datetime.fromisoformat(d["edited"])
            d["homeworld"] = (fetch.get_single_record(d["homeworld"])).get("name")

        ctx = {
            "data": data,
        }
        return render(request, 'pages/homepage.html', ctx)
