from django.shortcuts import render

from world_of_speed_app.user_profile.models import Profile


# Create your views here.
def index(request):
    context = {
        "profile": Profile.objects.first()
    }
    return render(request, 'common/index.html', context)
