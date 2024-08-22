from django.db import models

from users.models import User


# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'category'
        verbose_name_plural = 'Categories'


class Product(BaseModel):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    discount = models.IntegerField(default=0, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def discount_price(self):
        if self.discount > 0:
            return self.price * (1 - self.discount / 100)
        return False

    class Meta:
        db_table = 'product'
        verbose_name_plural = 'Products'


class Image(BaseModel):
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    is_primary = models.BooleanField(default=False)

    class Meta:
        db_table = 'image'


class Comment(BaseModel):
    class Ratings(models.IntegerChoices):
        zero = 0
        one = 1
        two = 2
        three = 3
        four = 4
        five = 5

    message = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to='comments/', null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')


class Attribute(BaseModel):
    name = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name


class AttributeValue(BaseModel):
    value = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.value


class ProductAttribute(BaseModel):
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    value = models.ForeignKey(AttributeValue, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
