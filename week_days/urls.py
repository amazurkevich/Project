from django.urls import path
from . import views

urlpatterns = [
    path('todo_week/', views.index),
    path('todo_week/monday/', views.monday),
    path('todo_week/tuesday/', views.tuesday),
]
