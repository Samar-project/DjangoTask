# trip_app/urls.py

from django.urls import path
# from .views import TripView
from route.views import RouteListCreateView,RouteRetrieveUpdateDestroyView

urlpatterns = [
    # path('trip/', TripView.as_view(), name='trip'),
    # Add other URL patterns as needed
    path('lists/', RouteListCreateView.as_view(), name='route-list'),
    path('lists/<pk>', RouteRetrieveUpdateDestroyView.as_view(), name='route-details'),

]
