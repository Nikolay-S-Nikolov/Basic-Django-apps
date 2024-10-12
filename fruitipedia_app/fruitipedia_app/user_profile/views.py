from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from fruitipedia_app.user_profile.forms import ProfileCreateForm, ProfileEditForm
from fruitipedia_app.user_profile.models import Profile


# Create your views here.
class ProfileGetMixin:
    def get_object(self, queryset=None):
        return Profile.objects.first()


class ProfileCreateView(views.CreateView):
    form_class = ProfileCreateForm
    queryset = Profile.objects.all()
    template_name = "user_profile/create-profile.html"
    success_url = reverse_lazy("dashboard")


class ProfileDetailsView(views.DetailView):
    template_name = "user_profile/details-profile.html"

    def get_object(self, queryset=None):
        return Profile.objects.first()


class ProfileEditView(ProfileGetMixin, views.UpdateView):
    form_class = ProfileEditForm
    queryset = Profile.objects.all()
    template_name = "user_profile/edit-profile.html"
    success_url = reverse_lazy("profile-details")


class ProfileDeleteView(ProfileGetMixin, views.DeleteView):
    template_name = "user_profile/delete-profile.html"
    success_url = reverse_lazy("index")
