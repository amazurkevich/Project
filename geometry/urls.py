from django.urls import path, include
from . import views

urlpatterns = [
    path('rectangle/<int:width>/<int:height>', views.rectangle),
    path('square/<int:width>', views.square),
    path('circle/<int:radius>', views.circle),

]
