from django import forms

from fruitipedia_app.fruit.models import Fruit


class FruitBaseForm(forms.ModelForm):
    class Meta:
        model = Fruit
        exclude = ("owner",)

        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Fruit Name"}),
            "image_url": forms.URLInput(attrs={'placeholder': 'Fruit Image URL'}),
            "description": forms.Textarea(attrs={'placeholder': 'Fruit Description'}),
            "nutrition": forms.Textarea(attrs={'placeholder': 'Nutrition Info'}),
        }


class FruitCreateForm(FruitBaseForm, forms.ModelForm):
    class Meta(FruitBaseForm.Meta):
        labels = {
            "name": "",
            "image_url": "",
            "description": "",
            "nutrition": "",
        }


class FruitDetailsForm(FruitBaseForm):
    pass


class FruitEditForm(FruitBaseForm):
    pass


class FruitDeleteForm(FruitBaseForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for (_, field) in self.fields.items():
    #         field.widget.attrs['disabled'] = 'disabled'
    #         field.widget.attrs['readonly'] = 'readonly'
    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    class Meta(FruitBaseForm.Meta):
        widgets = {
            "name": forms.TextInput(attrs={"readonly": "readonly"}),
            "image_url": forms.URLInput(attrs={"readonly": "readonly"}),
            "description": forms.Textarea(attrs={"readonly": "readonly"}),
            "nutrition": forms.Textarea(attrs={"readonly": "readonly"}),
        }
