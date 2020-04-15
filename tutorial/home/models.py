from django.db import models
from django.contrib.auth.models import User



class Post(models.Model):
    post=models.CharField(max_length=100,null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.post




class fahime(models.Model):
      pass
