from django.db import models

# Create your models here.
class product(models.Model):
    image=models.URLField(max_length=500)
    cart_title=models.CharField(max_length=200)
    description=models.CharField(max_length=300)
    pricess=models.IntegerField()

    def __str__(self):
        return self.cart_title
