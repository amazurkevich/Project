from django.urls import path
from . import views

urlpatterns = [
    path('<str:git_command>', views.get_git_command),
    path('<str:git_command>', views.get_git_command_by_group, name="git")
]
