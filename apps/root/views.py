from django.shortcuts import render

# Create your views here.
from apps.user.models import CustomUser


def root_view(request):
    user = CustomUser.objects.get(email="xarhsasi@gmail.com")
    context = {
        "user": user,
        "profile": user.get_profile(),
        "address": user.get_address(),
        "experiences": user.get_experiences(),
        "educations": user.get_educations(),
        "skills": user.get_skills(),
        "interests": user.get_interests(),
        "awards": user.get_awards(),
    }
    return render(request, "root/index.html", context)
