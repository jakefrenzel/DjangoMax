from django.db import models

# Create your models here.


# Basic Django Model Example

class Item(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.name