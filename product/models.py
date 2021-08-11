from django.db import models

# Create your models here.
class SubCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)
    sub_categories = models.ManyToManyField(SubCategory, blank=True, default=None)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    categories = models.ManyToManyField(Category, blank=True, default=None)
    # sub_categories = models.ManyToManyField(SubCategory, blank=True, default=None)

    def __str__(self):
        return self.name + " | " + self.price