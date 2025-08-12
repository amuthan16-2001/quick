from django.db import models
class student(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.password
class roomid(models.Model):
    username=models.CharField(max_length=100)

    def __str__(self):
        return self.username
class roomname(models.Model):
    username=models.CharField(max_length=100)

    def __str__(self):
        return self.username

# Create your models here.
