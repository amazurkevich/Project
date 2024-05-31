from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<str:git_command>', views.get_git_command),
    # path('<str:git_command>', views.get_git_command, name='git'),
]
