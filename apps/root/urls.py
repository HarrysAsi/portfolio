from django.urls import path, include

from .views import (
    root_view
)

urlpatterns = [
    path('', root_view, name="root"),

]
