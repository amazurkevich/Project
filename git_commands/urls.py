from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='git_menu'),
    path('/', views.index),
    path('<str:git_command>', views.get_git_command, name='git'),
    # path('<str:git_command>', views.get_git_command, name='git'),
]
