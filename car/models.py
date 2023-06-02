from django.db import models


class Car(models.Model):
    username = models.CharField(max_length=30, null=True, blank=True)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    price = models.IntegerField(max_length=7)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(null=True, blank=True, upload_to='car_images/')

    def __str__(self):
        return f"{self.brand} {self.model}"
