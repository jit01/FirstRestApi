from django.db import models
class Student(models.Model):
    sno=models.IntegerField()
    sname=models.CharField(max_length=20)
    semail=models.EmailField(max_length=50)
    sfee=models.IntegerField()
    sloc=models.CharField(max_length=20)
    def __str__(self):
        return self.sname