from django.urls import path
from . import views

app_name = "bitcoint_arbitrage"

urlpatterns = [
    path(
        route="", 
        view=views.RealTime.as_view(), 
        name="realtime"
    ),
    path(
        route="today/", 
        view=views.TodayView.as_view(), 
        name="today"
    ),
    path(
        route="all-spreads/", 
        view=views.AllSpreads.as_view(), 
        name="all_spreads"
    )
]

