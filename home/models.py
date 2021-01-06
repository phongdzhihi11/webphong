from django.db import models


# Create your models here.
class Post(models.Model):
    post = models.AutoField(primary_key=True)
    ten = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    photo = models.FileField(null=True)
    theloai = models.CharField(max_length=100)

    def __str__(self):
        return self.ten
