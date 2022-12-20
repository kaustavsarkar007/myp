from django.db import models

# Create your models here.


class Contact(models.Model):
    sno = models.AutoField(primary_key = True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=254)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add =True,blank= True)

    def __str__(self) -> str:
        return self.firstname