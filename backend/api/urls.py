from django.urls import path
from . import views

# Import classes here!
from .views import ItemListCreateView, BoxView, ProductListCreateView

urlpatterns = [
    path('box/', BoxView.as_view(), name='box-create'),
    path('product/', ProductListCreateView.as_view(), name='product-create'),
    path('items/', ItemListCreateView.as_view(), name='item-list-create')
]