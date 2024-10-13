from django.urls import path, include

from world_of_speed_app.car.views import CarCatalogueView, CarCreateView, CarDetailsView, CarEditVIew, CarDeleteView

urlpatterns = (
    path("catalogue/", CarCatalogueView.as_view(), name="cars-catalogue"),
    path("create/", CarCreateView.as_view(), name="car-create"),
    path("<int:id>/", include([
        path("details/", CarDetailsView.as_view(), name="car-details"),
        path("edit/", CarEditVIew.as_view(), name="car-edit"),
        path("delete/", CarDeleteView.as_view(), name="car-delete"),
    ])),)
