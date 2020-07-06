from django.db import models


class Madlib(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    container = models.CharField(max_length=100, blank=False, null=False)
    adj1 = models.CharField(max_length=100, blank=False, null=False)
    adj2 = models.CharField(max_length=100, blank=False, null=False)
    adj3 = models.CharField(max_length=100, blank=False, null=False)
    noun = models.CharField(max_length=100, blank=False, null=False)
    animal = models.CharField(max_length=100, blank=False, null=False)
    veg1 = models.CharField(max_length=100, blank=False, null=False)
    veg2 = models.CharField(max_length=100, blank=False, null=False)
    color = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name


class Madlib2(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    adj1 = models.CharField(max_length=100, blank=False, null=False)
    adj2 = models.CharField(max_length=100, blank=False, null=False)
    body_part = models.CharField(max_length=100, blank=False, null=False)
    noun = models.CharField(max_length=100, blank=False, null=False)
    animal = models.CharField(max_length=100, blank=False, null=False)
    verb = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name

