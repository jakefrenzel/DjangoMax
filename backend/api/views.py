# Import class based methods
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Import other necessary modules
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Import Models & Serializers here:
from .models import Item, Box, Product, Setting, Facility, Franchisee, User, MembershipTier, Court
from .serializers import ItemSerializer, BoxSerializer, ProductSerializer, SettingSerializer, FacilitySerializer, FranchiseeSerializer, UserSerializer, MembershipTierSerializer, CourtSerializer



# Create your views here.

# Example Views

# List all products or create a new one
class ProductListCreateView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Retrieve, update, or delete a specific product
class ProductDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class BoxView(APIView):
    def post(self, request):
        serializer = BoxSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        boxes = Box.objects.all()
        serializer = BoxSerializer(boxes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ItemListCreateView(ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


# CourtsPro Official Views

class SettingView(RetrieveUpdateDestroyAPIView):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer

class FacilityView(ListCreateAPIView):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer

class FranchiseeView(ListCreateAPIView):
    queryset = Franchisee.objects.all()
    serializer_class = FranchiseeSerializer

class UserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MembershipTierView(ListCreateAPIView):
    queryset = MembershipTier.objects.all()
    serializer_class = MembershipTierSerializer

class CourtView(ListCreateAPIView):
    queryset = Court.objects.all()
    serializer_class = CourtSerializer