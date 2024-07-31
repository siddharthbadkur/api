from django.db import models

# Create your models here.
class Studentapi(models.Model):
    stu_name=models.CharField(max_length=45)
    stu_email=models.EmailField(max_length=33)
    stu_contact=models.IntegerField(20)
    stu_city=models.CharField(max_length=50)


    def __str__(self):
        return self.stu_city
    
