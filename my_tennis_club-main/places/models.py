from django.contrib.auth.models import User
from django.db import models



class Place(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

#這是新加的
class Court(models.Model):
    COURT_TYPES = [
        ('grass', '草地'),
        ('hard', '硬地'),
        ('clay', '泥地'),
        ('carpet', '地毯'),
    ]

    name = models.CharField(max_length=100, verbose_name='球場名稱')
    court_type = models.CharField(max_length=10, choices=COURT_TYPES, verbose_name='球場型態')
    city = models.CharField(max_length=100, verbose_name='所在城市')

    def __str__(self):
        return self.name

