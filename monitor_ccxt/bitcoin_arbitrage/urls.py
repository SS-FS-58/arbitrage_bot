from django.urls import path
from bitcoin_arbitrage import views 
from bitcoin_arbitrage.api import views as api_views

app_name = "bitcoin_arbitrage"

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
    ),
    path(
        route="realtime-spreads/", 
        view=api_views.RealTimeSpreadEndpoint.as_view(), 
        name="realtime_spreads"
    ),
    path(
        route="monitor/",
        view=api_views.MonitorEndpoint.as_view(),
        name="monitor"
    )
]

