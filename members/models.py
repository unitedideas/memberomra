

from django.db import models


class Rider(models.Model):
    firstName = models.CharField(null=True, blank=True, max_length=120)
    lastName = models.CharField(null=True, blank=True, max_length=120)
    memberNumber = models.CharField(null=True, blank=True, max_length=120)
    expirationDate = models.DateField(null=True, blank=True)
    active = models.BooleanField()

    def __str__(self):
        return self.firstName + " " + self.lastName + " " + self.memberNumber


class Year(models.Model):
    year = models.IntegerField()

    def __str__(self):
        return self.year


class Series(models.Model):
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    name = models.CharField(null=True, blank=True, max_length=4)

    def __str__(self):
        return self.year + " " + self.name


class Race(models.Model):
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    club = models.CharField(null=True, blank=True, max_length=180)
    name = models.CharField(null=True, blank=True, max_length=4)
    location = models.CharField(null=True, blank=True, max_length=180)
    date = models.DateField()

    def __str__(self):
        return self.name


class RiderClass(models.Model):
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    name = models.CharField(null=True, blank=True, max_length=4)

    def __str__(self):
        return self.name


class Position(models.Model):
    rider_class = models.ForeignKey(RiderClass, on_delete=models.CASCADE)
    rider = models.ForeignKey(Rider, models.CASCADE)
    position = models.IntegerField()
    value = models.IntegerField()

    def __str__(self):
        return self.position + self.value


