
from django.urls import path

from . import views

urlpatterns = [
        path('',views.homepage_view),
        path('map/',views.map_view),
        path('sightings/',views.list_sights),
        path('sightings/stats/',views.stats_view),
        path('sightings/add/',views.add_sights),
        path('sightings/<Unique_Squirrel_Id>/',views.update_sights),
        ]
