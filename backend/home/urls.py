from django.urls import path
from .views import BikeCreateView, home

urlpatterns = [
    path("", home, name="home"),
    path("bikes/create/", BikeCreateView.as_view(), name="create_bike"),
]
