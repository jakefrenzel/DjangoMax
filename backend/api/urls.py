from django.urls import path
from . import views

# Import classes here!
from .views import classView

urlpatterns = [
    path('', views.getData, name='getData'),
]