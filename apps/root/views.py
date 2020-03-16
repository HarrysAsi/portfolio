from django.shortcuts import render

# Create your views here.
from apps.user.models import CustomUser
from portfolio.settings import OWNER_EMAIL


def root_view(request):
    # get or create returns tuple with (User, created) so we extract the user of it
    user = CustomUser.objects.get(email=OWNER_EMAIL)

    context = {
        "user": user,
        "profile": user.get_profile(),
        "address": user.get_address(),
        "experiences": user.get_experiences(),
        "educations": user.get_educations(),
        "skills": user.get_skills(),
        "interests": user.get_interests(),
        "awards": user.get_awards(),
        "projects": user.get_projects(),
    }
    return render(request, "root/index.html", context)


def handler404(request, exception):
    return render(request, 'handlers/404.html', status=404)


def handler500(request):
    return render(request, 'handlers/500.html', status=500)
