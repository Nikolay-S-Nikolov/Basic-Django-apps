from django import forms

from fruitipedia_app.user_profile.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("first_name", "last_name", "email", "password")
        widgets = {
            "first_name": forms.TextInput(attrs={'placeholder': "First Name"}),
            "last_name": forms.TextInput(attrs={'placeholder': "Last Name"}),
            "email": forms.EmailInput(attrs={'placeholder': "Email"}),
            "password": forms.PasswordInput(attrs={'placeholder': "Password"}),
        }


class ProfileCreateForm(ProfileBaseForm):
    class Meta(ProfileBaseForm.Meta):
        labels = {
            "first_name": "",
            "last_name": "",
            "email": "",
            "password": "",
        }
        help_texts = {"password": "*Password length requirements: 8 to 20 characters"}


class ProfileDetailsForm(ProfileBaseForm):
    pass


class ProfileEditForm(ProfileBaseForm):
    class Meta(ProfileBaseForm.Meta):
        fields = ("first_name", "last_name", "image_url", "age")
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "image_url": "Image URL",
        }


class ProfileDeleteForm(ProfileBaseForm):
    pass
