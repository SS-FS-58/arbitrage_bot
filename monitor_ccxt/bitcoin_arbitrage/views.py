import logging
import os
import asyncio
import csv
from datetime import date

from django.shortcuts import render
from django.views import View

from bitcoin_arbitrage import config

from . import models


class RealTime(View):
    template_name = "index.html"

    def get_queryset(self):
        return (models.Spread.objects.all()
                .order_by("-pk")[:5]
                .order_by("-spread"))

    def get(self, request, *args, **kwargs):
        data = {"last_spreads" : self.get_queryset}
        return render(request, template_name=self.template_name, context=data)


class TodayView(View):
    template_name = "spreads_list.html"

    def get_queryset(self):
        now = date.today()
        today_spread = models.Spread.objects.filter(recorded_date__date=now).all()
        if today_spread.count() > 0:
            highest = today_spread.order_by("-spread")[0]
            lowest = today_spread.order_by("spread")[0]
        else:
            highest = today_spread.order_by("-spread")
            lowest = today_spread.order_by("spread")
        data = {"spreads" : today_spread,
                "highest" : highest,
                "lowest" : lowest}
        return data

    def get(self, request, *args, **kwargs):
        data = self.get_queryset()
        return render(request, template_name=self.template_name, context=data)


class AllSpreads(View):
    template_name = "spreads_list.html"

    def get_queryset(self):
        spreads = models.Spread.objects.all()
        if spreads.count() > 0:
            highest = spreads.order_by("-spread")[0]
            lowest = spreads.order_by("spread")[0]
        else:
            highest = spreads.order_by("-spread")
            lowest = spreads.order_by("spread")
        data = {"spreads" : spreads,
                "highest" : highest,
                "lowest" : lowest}
        return data

    def get(self, request, *args, **kwargs):
        data = self.get_queryset()
        return render(request, template_name=self.template_name, context=data)
