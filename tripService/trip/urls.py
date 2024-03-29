# trip_app/urls.py

from django.urls import path
from .views import TripListCreateView,TripRetrieveUpdateDestroyView
# from route.views import RouteListCreateView

urlpatterns = [
    # path('list/', TripView.as_view(), name='trip'),
    # Add other URL patterns as needed
    path('lists/', TripListCreateView.as_view(), name='trip-list'),
    path('lists/<pk>', TripRetrieveUpdateDestroyView.as_view(), name='trip-details'),

]
