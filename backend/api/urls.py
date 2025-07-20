from django.urls import path
from . import views

# Import classes here!
from .views import ItemListCreateView, BoxView, ProductListCreateView, SettingView, FacilityView, FranchiseeView, UserView, MembershipTierView, CourtView

urlpatterns = [
    #example urls
    path('box/', BoxView.as_view(), name='box-create'),
    path('product/', ProductListCreateView.as_view(), name='product-create'),
    path('items/', ItemListCreateView.as_view(), name='item-list-create'),

    #CourtsPro Official URLs
    path('settings/<int:pk>/', SettingView.as_view(), name='item-list-create'),
    path('facility/', FacilityView.as_view(), name='facility-list-create'),
    path('franchisee/', FranchiseeView.as_view(), name='franchisee-list-create'),
    path('user/', UserView.as_view(), name='user-list-create'),
    path('membershiptier/', MembershipTierView.as_view(), name='membership-tier-list-create'),
    path('court/', CourtView.as_view(), name='court-list-create'),

]