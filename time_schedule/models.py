from django.db import models
from django.utils import timezone
# Create your models here.

class Unit(models.Model):
    positions=models.CharField(max_length=30,primary_key=True)
    def __str__(self):
        return  self.positions


class Employee(models.Model):
    employee_name = models.CharField(max_length=30,primary_key=True)
    on_channel_time = models.DateTimeField(blank=True, null=True)
    time_of_relieve = models.DateTimeField(blank=True, null=True)
    hours_on_break = models.TimeField(blank=True, null=True)
    def __str__(self):
       return self.employee_name


class Position(models.Model):
    position_name=models.ForeignKey(Unit)
    controller_name=models.ForeignKey(Employee)



