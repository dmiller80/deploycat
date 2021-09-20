from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
    client_id = models.IntegerField(blank=False, null=False)
    name = models.CharField(max_length=50)
    nick_name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    email = models.EmailField(max_length=200)
    cell_phone = models.CharField(max_length=50)
    birth_date = models.DateField(default=timezone.now, blank=True, null=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.client_id)

class Exercise(models.Model):
    exercise_id = models.IntegerField(blank=False, null=False)
    name = models.CharField(max_length=50)
    cal_minute = models.DecimalField(max_digits=7, decimal_places=1)
    note = models.CharField(max_length=200)

    def __str__(self):
        return str(self.exercise_id)

class Activity(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='activity')
    date = models.DateField(default=timezone.now)
    type = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='exercise')
    duration = models.DecimalField(max_digits=7, decimal_places=1)
    note = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Activities"

    def __str__(self):
        return str(self.client_id)



