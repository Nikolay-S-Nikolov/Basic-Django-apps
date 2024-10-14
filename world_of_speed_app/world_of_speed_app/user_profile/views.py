from django.db.models import Sum
from django.views import generic as views
from django.urls import reverse_lazy
from world_of_speed_app.user_profile.forms import ProfileCreateForm, ProfileEditForm
from world_of_speed_app.user_profile.models import Profile


# Create your views here.
class GetProfileMixin:
    def get_object(self, queryset=None):
        return Profile.objects.first()


class ProfileCreateView(views.CreateView):
    form_class = ProfileCreateForm
    template_name = "user_profile/profile-create.html"
    success_url = reverse_lazy('cars-catalogue')


class ProfileDetailsView(GetProfileMixin, views.DetailView):
    template_name = "user_profile/profile-details.html"
    queryset = Profile.objects.all()
    extra_context = {
        "total_price": Profile.objects.first().car_set.aggregate(total=Sum("price"))["total"] or 0
    }

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["total_price"] = Profile.objects.first().car_set.aggregate(total=Sum("price"))["total"] or 0
    #     return context


class ProfileEditView(GetProfileMixin, views.UpdateView):
    form_class = ProfileEditForm
    queryset = Profile.objects.all()
    template_name = "user_profile/profile-edit.html"
    success_url = reverse_lazy("profile-details")


class ProfileDeleteView(GetProfileMixin, views.DeleteView):
    template_name = "user_profile/profile-delete.html"
    success_url = reverse_lazy("index")
