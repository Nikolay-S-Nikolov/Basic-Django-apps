from django.shortcuts import render
from django.views import generic as views

from world_of_speed_app.car.forms import CarCreateForm, CarEditForm, CarDeleteForm
from world_of_speed_app.car.models import Car
from world_of_speed_app.user_profile.models import Profile
from django.urls import reverse_lazy


# Create your views here.
class ProfileGetMixin:
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["profile"] = Profile.objects.first()
        return context


class CarCatalogueView(ProfileGetMixin, views.ListView):
    template_name = "car/catalogue.html"
    model = Car


class CarCreateView(ProfileGetMixin, views.CreateView):
    template_name = "car/car-create.html"
    form_class = CarCreateForm
    success_url = reverse_lazy("cars-catalogue")


class CarDetailsView(ProfileGetMixin, views.DetailView):
    queryset = Car.objects.all()
    template_name = "car/car-details.html"


class CarEditVIew(ProfileGetMixin, views.UpdateView):
    queryset = Car.objects.all()
    form_class = CarEditForm
    template_name = "car/car-edit.html"
    success_url = reverse_lazy("cars-catalogue")


class CarDeleteView(ProfileGetMixin, views.DeleteView):
    queryset = Car.objects.all()
    template_name = "car/car-delete.html"
    success_url = reverse_lazy("cars-catalogue")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CarDeleteForm(instance=self.object)
        return context
