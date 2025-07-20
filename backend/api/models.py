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


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=25, unique=False)
    country_code = models.CharField(max_length=25, default='+1')
    email = models.EmailField(max_length=255, unique=False)
    date_of_birth = models.DateField(default='2025-01-01')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "User: " + self.username

    class Meta:
        db_table = 'users'


class MembershipTier(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    facility_id = models.ForeignKey('Facility', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Membership Tier: {self.title} for Facility: {self.facility.id}"

    class Meta:
        db_table = 'membership_tiers'


"""
# Membership model
class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    facility_id = models.ForeignKey('Facility', on_delete=models.CASCADE)
    membership_id = models.ForeignKey('MembershipTier', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Membership: {self.membership.title} for {self.user.username}"
    
    class Meta:
        db_table = 'memberships'

 

# Membership Tier model
class MembershipTier(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    facility_id = models.ForeignKey('Facility', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Membership Tier: {self.title} for Facility: {self.facility.id}"

    class Meta:
        db_table = 'membership_tiers'


# Courts model
class Court(models.Model):
    id = models.BigAutoField(primary_key=True)
    facility_id = models.ForeignKey('Facility', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Court: {self.name} for Facility: {self.facility.id}"

    class Meta:
        db_table = 'courts'


# Booking model
class Booking(models.Model):
    id = models.BigAutoField(primary_key=True)
    facility_id = models.ForeignKey('Facility', on_delete=models.CASCADE)
    court_id = models.ForeignKey('Court', on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking: {self.id} from {self.start_time} to {self.end_time}"

    class Meta:
        db_table = 'bookings'

"""