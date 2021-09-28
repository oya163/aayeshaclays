from io import BytesIO
from os import name
from PIL import Image
import PIL

from django.core.files import File
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateTimeField
from django.db.models.fields.files import ImageField

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    

    class Meta:
        ordering = ('name',)
        verbose_name = ("Category")
        verbose_name_plural = ("Categorys")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}'

class Color(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    

    class Meta:
        ordering = ('name',)
        verbose_name = ("Color")
        verbose_name_plural = ("Colors")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}'

class Collection(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    

    class Meta:
        ordering = ('name',)
        verbose_name = ("Collection")
        verbose_name_plural = ("Collections")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}'

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    color = models.ForeignKey(Color, related_name='products', on_delete=models.CASCADE)
    collection = models.ForeignKey(Collection, related_name='products', on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)
        verbose_name = ("Product")
        verbose_name_plural = ("Products")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}'


class ImageModel(models.Model):
    product = models.ForeignKey("Product", related_name="product_image", on_delete=models.CASCADE, default=3)
    name = models.CharField(max_length=255, default="Test")
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    default = models.BooleanField(default=False)

    class Meta:
        ordering = ('-date_added',)
        verbose_name = ("ImageModel")
        verbose_name_plural = ("ImageModels")

    def __str__(self):
        return self.name

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''

    # def get_thumbnail(self):
    #     if self.thumbnail:
    #         return 'http://127.0.0.1:8000' + self.thumbnail.url
    #     else:
    #         if self.image:
    #             self.thumbnail = self.make_thumbnail(self.image)
    #             self.save()

    #             return 'http://127.0.0.1:8000' + self.thumbnail.url
    #         else:
    #             return ''

    # def make_thumbnail(self, image, size=[200, 200]):
    #     img = Image.open(image)
    #     img.convert('RGB')
    #     img.thumbnail(size, Image.ANTIALIAS)

    #     thumb_io = BytesIO()
    #     img.save(thumb_io, 'JPEG', quality=85)
    #     thumbnail = File(thumb_io, name=self.image.name)

    #     return thumbnail