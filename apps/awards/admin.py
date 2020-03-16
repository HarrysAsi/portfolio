from django.contrib import admin

# Register your models here.
from apps.awards.models import Award

admin.site.register(Award)
