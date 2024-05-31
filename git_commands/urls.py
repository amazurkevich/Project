from django.urls import path
from . import views

urlpatterns = [
    path('<git_command>', views.get_git_command),
]
