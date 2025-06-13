"""URL routes for the bus management system."""

from django.urls import path
from . import views

urlpatterns = [
    path('realtime/', views.realtime_monitor, name='realtime-monitor'),
    path('update-location/<int:dispatch_id>/', views.update_location, name='update-location'),
    path('statistics/', views.statistics_view, name='statistics'),
]
