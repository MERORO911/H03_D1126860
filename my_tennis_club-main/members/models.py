from django.db import models



class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age = models.IntegerField(null=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    joined_date = models.DateField(null=True)
    

    def __str__(self):
        return f"{self.firstname} {self.lastname}"



    
