from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.EmailField(max_length=254)
    desc = models.CharField(max_length=250)
    date = models.DateField()

    def __str__(self):
        return self.name + ':' + self.email