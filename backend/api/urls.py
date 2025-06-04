from django.urls import path
from . import views

# Import classes here!
from .views import Item

urlpatterns = [
    path('', Item.as_view(), name='success'),
]