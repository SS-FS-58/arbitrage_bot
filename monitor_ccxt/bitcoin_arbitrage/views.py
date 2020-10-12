import logging
import os
import asyncio
import csv
from datetime import date

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from bitcoin_arbitrage import config

from . import models 



class RealTime(LoginRequiredMixin, View):
    template_name = "index.html"
    login_url = "/login/"

    def get_queryset(self):
        return (models.Spread.objects.all()
                .order_by("-pk")[:5]
                .order_by("-spread"))

    def get(self, request, *args, **kwargs):
        data = {"last_spreads" : self.get_queryset}
        return render(request, template_name=self.template_name, context=data)


class TodayView(LoginRequiredMixin, View):
    template_name = "spreads_list.html"
    login_url = "/login/"

    def get_queryset(self):
        now = date.today()
        today_spread = models.Spread.objects.filter(recorded_date__date=now).all()
        if today_spread.count() > 0:
            highest = today_spread.order_by("-spread")[0]
            lowest = today_spread.order_by("spread")[0]
        else:
            highest = today_spread.order_by("-spread")
            lowest = today_spread.order_by("spread")
        title = "Today"
        data = {"spreads" : today_spread,
                "highest" : highest,
                "lowest" : lowest,
                "title" : title}
        return data 

    def get(self, request, *args, **kwargs):
        data = self.get_queryset()
        return render(request, template_name=self.template_name, context=data)


class AllSpreads(LoginRequiredMixin, View):
    template_name = "spreads_list.html"
    login_url = "/login/"
    
    def get_queryset(self):
        spreads = models.Spread.objects.all()
        if spreads.count() > 0:
            highest = spreads.order_by("-spread")[0]
            lowest = spreads.order_by("spread")[0]
        else:
            highest = spreads.order_by("-spread")
            lowest = spreads.order_by("spread")
        title = "AllSpreads"
        data = {"spreads" : spreads,
                "highest" : highest,
                "lowest" : lowest,
                "title" : title}
        return data
    
    def get(self, request, *args, **kwargs):
        data = self.get_queryset()
        return render(request, template_name=self.template_name, context=data)