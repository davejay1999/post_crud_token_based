from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    owner = models.ForeignKey(User, verbose_name="Created By", on_delete=models.CASCADE)
    description = models.TextField(null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user) + str(self.date_created)

    class Meta:
        ordering = ["-date_created"]