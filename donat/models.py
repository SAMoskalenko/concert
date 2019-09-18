from django.db import models


class DonatorsData(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)


class DonatsSourcesData(models.Model):
    source = models.CharField(max_length=250, blank=True, null=True)  # unique
    details = models.CharField(max_length=100, blank=True, null=True)


class DonationsData(models.Model):
    donator = models.ForeignKey(DonatorsData, on_delete=models.PROTECT, blank=True, null=True)
    donat_source = models.ForeignKey(DonatsSourcesData, on_delete=models.PROTECT, blank=True, null=True)
    summ = models.IntegerField(blank=True, null=True)


class Event(models.Model):
    target = models.IntegerField(blank=True, null=True)
