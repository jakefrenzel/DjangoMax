from django.urls import path
from . import views

# Import classes here!
from .views import ItemListCreateView, BoxView, ProductListCreateView, SettingView, FacilityView, FranchiseeView

urlpatterns = [
    #example urls
    path('box/', BoxView.as_view(), name='box-create'),
    path('product/', ProductListCreateView.as_view(), name='product-create'),
    path('items/', ItemListCreateView.as_view(), name='item-list-create'),

    #CourtsPro Official URLs
    path('settings/<int:pk>/', SettingView.as_view(), name='item-list-create'),
    path('facility/', FacilityView.as_view(), name='facility-list-create'),
    path('franchisee/', FranchiseeView.as_view(), name='franchisee-list-create'),
]