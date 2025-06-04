# Import class based methods
from rest_framework.generics import ListCreateAPIView

# Import Models & Serializers here:
from .models import Item
from .serializers import ItemSerializer



# Create your views here.

class Item(ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


