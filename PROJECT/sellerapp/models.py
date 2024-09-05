from django.db import models

# Create your models here.
class login_tbl(models.Model):
    username = models.CharField(max_length=30)
    email=models.EmailField()
    mobilenumber = models.IntegerField()
    password=models.CharField(max_length=30)
    confirmpassword=models.CharField(max_length=30)

    def __str__(self):
        return self.username