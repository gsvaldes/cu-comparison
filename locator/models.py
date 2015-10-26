from django.db import models


class Company(models.Model):

    BUSINESS_TYPE= (
        ('CU', 'Credit Union'),
        ('CC', 'Check Cashing'),
    )

    created = models.DateTimeField(auto_now_add=True)
    business_name = models.CharField(max_length=100)
    link = models.URLField()
    business_type = models.CharField(max_length=2, choices=BUSINESS_TYPE)


class Location(models.Model):
    business = models.ForeignKey(Company)
    created = models.DateTimeField(auto_now_add=True)
