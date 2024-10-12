from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from fruitipedia_app.fruit.forms import FruitCreateForm, FruitDetailsForm, FruitEditForm, FruitDeleteForm
from fruitipedia_app.fruit.models import Fruit
from fruitipedia_app.user_profile.models import Profile


# Create your views here.
class GetProfileMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = Profile.objects.first()
        return context


class FruitCreateView(GetProfileMixin, views.CreateView):
    form_class = FruitCreateForm
    template_name = "fruit/create-fruit.html"
    success_url = reverse_lazy("dashboard")

    def form_valid(self, form):
        form.instance.owner_id = Profile.objects.first().id
        return super().form_valid(form)


class FruitDetailsView(GetProfileMixin, views.DetailView):
    form_class = FruitDetailsForm
    queryset = Fruit.objects.all()
    template_name = "fruit/details-fruit.html"


class FruitEditView(GetProfileMixin, views.UpdateView):
    form_class = FruitEditForm
    queryset = Fruit.objects.all()
    template_name = "fruit/edit-fruit.html"
    success_url = reverse_lazy("dashboard")


class FruitDeleteView(GetProfileMixin, views.DeleteView):
    queryset = Fruit.objects.all()
    template_name = "fruit/delete-fruit.html"
    success_url = reverse_lazy("dashboard")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = FruitDeleteForm(instance=self.object)
        return context
