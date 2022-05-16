from django.urls import path
from . import views
from .views import profile

urlpatterns = [
    path('profiles/', views.profile, name='profiles'),
]