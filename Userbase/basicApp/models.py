from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class AddOnFieldsTo_User(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #addons
    portfolio = models.URLField(blank=True)
    DP = models.ImageField(upload_to='Profile_pics', blank=True)

    def __str__(self):
        return self.user.username