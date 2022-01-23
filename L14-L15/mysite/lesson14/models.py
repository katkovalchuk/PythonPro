from django.db import models


class Passport(models.Model):
    pass_number = models.CharField(max_length=20)
    exp_date = models.IntegerField(default=0)

    def __str__(self):
        return self.pass_number


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    passport = models.OneToOneField(Passport, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name


