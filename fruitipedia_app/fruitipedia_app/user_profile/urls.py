from django.urls import path

from fruitipedia_app.user_profile.views import ProfileCreateView, ProfileEditView, ProfileDetailsView, ProfileDeleteView

urlpatterns = (
    path('create/', ProfileCreateView.as_view(), name='profile-create'),
    path('details/', ProfileDetailsView.as_view(), name='profile-details'),
    path('edit/', ProfileEditView.as_view(), name='profile-edit'),
    path('delete/', ProfileDeleteView.as_view(), name='profile-delete'),
)
