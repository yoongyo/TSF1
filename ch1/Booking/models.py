from django.db import models

class Nationality(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField()

    def __str__(self):
        return self.name

class SNS(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

SEX = (
    ('Man', 'Man'),
    ('Woman', 'Woman'),
)


class Booking(models.Model):
    LastName = models.CharField(max_length=20)
    FirstName = models.CharField(max_length=20)
    Age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=SEX, blank=True, null=True)
    Email = models.EmailField(max_length=30)
    Date = models.DateField()
    SNS = models.ForeignKey(SNS, on_delete=models.CASCADE)
    SNSID = models.CharField(max_length=20)
    Nationality = models.ForeignKey(Nationality, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    ConfirmedEmail = models.EmailField(max_length=30)
    Language = models.ForeignKey(Language,on_delete=models.CASCADE)
    Demand = models.CharField(max_length=1200)