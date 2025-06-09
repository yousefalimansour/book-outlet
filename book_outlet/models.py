from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)])
    author = models.CharField(null= True,max_length=50)
    isbest_seller = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=7,decimal_places=2)

    def __str__(self):
        return f"{self.title} by {self.author} - Rating: {self.rating}/10, Price: ${self.price}, Best Seller: {'Yes' if self.isbest_seller else 'No'}"
    
