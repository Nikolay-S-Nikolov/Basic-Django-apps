from django import forms

from world_of_speed_app.car.models import Car
from world_of_speed_app.user_profile.models import Profile


class CarBaseForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ('owner',)


class CarCreateForm(CarBaseForm):
    def save(self, commit=True):
        if commit:
            self.instance.owner_id = Profile.objects.first().id
        return super().save(commit)

    class Meta(CarBaseForm.Meta):
        widgets = {
            "image_url": forms.URLInput(attrs={'placeholder': "https://..."}),
        }


class CarEditForm(CarBaseForm):
    pass


class CarDeleteForm(CarBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields.keys():
            self.fields[field_name].widget.attrs['readonly'] = "readonly"
            self.fields[field_name].widget.attrs['disabled'] = "disabled"
