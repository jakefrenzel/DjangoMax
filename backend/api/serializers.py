from rest_framework import serializers

# Import Models here:
from .models import Item, Box, Product, Setting, Facility, Franchisee


# Example Serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


# CourtsPro Official Serializers

class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        fields = '__all__'

class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = '__all__'

class FranchiseeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Franchisee
        fields = '__all__'