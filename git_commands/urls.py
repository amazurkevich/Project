from django.urls import path
from . import views

urlpatterns = [
    path('<git_command>', views.get_git_command),
    # path('synch/', views.git_synch),
    # path('save/', views.git_save),
    # path('publish/', views.git_publish),
    # path('branches/', views.git_branches),
    # path('bash/', views.git_bash),
    # path('navigation/', views.git_navigation),
]
