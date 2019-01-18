from django.db import models
import datetime

YEAR_CHOICES = []
for r in range(2018, (datetime.datetime.now().year + 2)):
    YEAR_CHOICES.append((r, r))


class Rider(models.Model):
    firstName = models.CharField('First Name', help_text='First Name', null=True, blank=True, max_length=120)
    lastName = models.CharField('Last Name', help_text='Last Name', null=True, blank=True, max_length=120)
    phoneNumber = models.CharField('Phone Number', help_text='Phone Number', null=True, blank=True, max_length=13)
    email = models.EmailField('Email', help_text='Email', null=True, blank=True, max_length=120)
    memberNumber = models.CharField('Member Number', help_text='Member Number', null=True, blank=True, max_length=120)
    plateNumber = models.CharField('Plate Number', help_text='Plate Number', null=True, blank=True, max_length=120)
    membershipYear = models.CharField('Membership Year', choices=YEAR_CHOICES, default='2018',
                                      help_text='2018', null=True, blank=True, max_length=40)

    # membershipYear = models.CharField('Membership Year', choices=YEAR_CHOICES, help_text='Membership Year', null=True,
    #                                   blank=True, max_length=40)

    # active = models.BooleanField('Membership Active', help_text='Membership Active', )

    class Meta:
        verbose_name = 'Rider'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.firstName + " " + self.lastName


class Year(models.Model):
    year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)

    class Meta:
        verbose_name = 'Year'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.year)


class Series(models.Model):
    name = models.CharField(null=True, blank=True, unique=True, max_length=80)

    class Meta:
        verbose_name = 'Race Series'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Club(models.Model):
    name = models.CharField(null=True, blank=True, max_length=80)
    contactPhone = models.CharField(null=True, blank=True, max_length=20)
    contactEmail = models.EmailField(null=True, blank=True, max_length=180)

    class Meta:
        verbose_name = 'Club Info'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Race(models.Model):
    year = models.ForeignKey(Year, on_delete=models.CASCADE, default=2010)
    club = models.ForeignKey(Club, null=True, blank=True, on_delete=models.CASCADE)
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    name = models.CharField(null=True, blank=True, max_length=180)
    location = models.CharField(null=True, blank=True, max_length=180)
    date = models.DateField()

    class Meta:
        verbose_name = 'Race Details'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class RiderClass(models.Model):
    rider_class = models.CharField(null=True, blank=True, unique=True, max_length=80)

    class Meta:
        verbose_name = 'Rider Classes'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.rider_class)


class PositionValues(models.Model):
    place = models.CharField(unique=True, max_length=80, null=True, blank=True, )
    points_value = models.FloatField()

    class Meta:
        verbose_name = 'Position Values'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.place) + " = " + str(self.points_value)


class Position(models.Model):
    race = models.ForeignKey(Race, models.CASCADE)
    rider = models.ForeignKey(Rider, models.CASCADE)
    rider_class = models.ForeignKey(RiderClass, on_delete=models.CASCADE)
    place = models.ForeignKey(PositionValues, models.CASCADE, null=True, blank=True, )

    class Meta:
        verbose_name = 'Race Results'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.rider) + " - " + str(self.place) + " Place"
