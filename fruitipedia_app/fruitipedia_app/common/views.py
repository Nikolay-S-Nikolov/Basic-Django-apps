from django.shortcuts import render

from fruitipedia_app.fruit.models import Fruit
from fruitipedia_app.user_profile.models import Profile


# Create your views here.
def index(request):
    profile = Profile.objects.first()
    context = {
        "profile": profile,
    }
    return render(request, 'index.html', context)


def dashboard(request):
    profile = Profile.objects.first()
    context = {
        "profile": profile,
        "fruits": Fruit.objects.all()
    }
    return render(request, 'dashboard.html', context)
