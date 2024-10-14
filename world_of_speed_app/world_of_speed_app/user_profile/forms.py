from django import forms

from world_of_speed_app.user_profile.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        widgets = {
            "password": forms.PasswordInput()
        }


class ProfileCreateForm(ProfileBaseForm):
    class Meta(ProfileBaseForm.Meta):
        fields = ("username", "email", "age", "password")


class ProfileEditForm(ProfileBaseForm):
    class Meta:
        model = Profile
        fields = "__all__"
        help_texts = {
            "age": ""
        }
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "profile_picture": "Profile Picture",
        }
