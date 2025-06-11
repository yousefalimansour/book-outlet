from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Address(models.Model):
    street =models.CharField(max_length=100)
    postal_code = models.CharField(max_length=80)
    city = models.CharField(max_length=80)
    def __str__(self):
        return f'{self.street}, {self.postal_code} , {self.city}'
    class Meta:
        verbose_name_plural = "Address Entiries"

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE ,null=True)
    #related name is just Author ,Book cause it just one of them not set 
    def __str__(self):
        return f'{self.first_name} {self.last_name} \n address: {self.address}'



class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50)

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE,null=True ,related_name="booksAuthor") #models.CharField(null= True,max_length=50)
    isbest_seller = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=7,decimal_places=2)
    slug = models.SlugField(default="",blank=True,null=False ,db_index=True)
    country = models.ManyToManyField(Country)

    def get_absolute_url(self):
        return reverse("book_outlet:book_details", args=[self.slug])
    # remove save for adding prepopulated in admin 
    # def save(self,*args,**kwargs):
    #     self.slug = slugify(self.title)
    #     return super().save(*args,**kwargs)
    def __str__(self):
        return f"{self.title} by {self.author} - Rating: {self.rating}/10, Price: ${self.price}, Best Seller: {'Yes' if self.isbest_seller else 'No'}"
    
