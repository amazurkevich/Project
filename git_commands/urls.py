from django.urls import path
from . import views

urlpatterns = [
    path('synch/', views.synch),
    path('save/', views.save),
    path('publish/', views.publish),
    path('branches/', views.branches),
    path('bash/', views.bash),
    path('navigation/', views.navigation),
]
