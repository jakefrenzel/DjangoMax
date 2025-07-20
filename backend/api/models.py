from django.db import models

# Create your models here.


# Basic Example Models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Box(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
# CourtsPro Official Models

class Setting(models.Model):
    id = models.BigAutoField(primary_key=True)
    facility_id = models.ForeignKey('Facility', on_delete=models.CASCADE)
    facility_open = models.IntegerField()
    facility_close = models.IntegerField()
    facility_courts = models.IntegerField()

    def __str__(self):
        return f"Setting: {self.id} for Facility: {self.facility_id}"
    
    class Meta:
        db_table="settings"


class Facility(models.Model):
    id = models.BigAutoField(primary_key=True)
    franchisee_id = models.ForeignKey('Franchisee', on_delete=models.CASCADE, null=True)
    allow_external_membership = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Facility: {self.id}"

    class Meta:
        db_table = 'facilities'


class Franchisee(models.Model):
    id = models.BigAutoField(primary_key=True)
    owner = models.BigIntegerField() # not sure where we were going with this
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Franchisee: {self.id}"
    
    class Meta:
        db_table = 'franchisees'