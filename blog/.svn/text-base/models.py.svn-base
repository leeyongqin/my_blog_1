from __future__ import unicode_literals
from django.contrib import admin
from django.db import models
from django.utils.timezone import now


class Item(models.Model):
    asin = models.CharField(max_length=20, blank=False)
    sku = models.CharField(max_length=60, blank=False)
    title = models.CharField(max_length=800)
    brand = models.CharField(max_length=30)
    seller = models.CharField(max_length=30)
    description = models.TextField()
    timestamp = now()

    def __unicode__(self):
        return self.asin

    class Meta:
        ordering = ('sku',)


class Reviews(models.Model):
    five_star = models.IntegerField(default=0, blank=False)
    four_star = models.IntegerField(default=0, blank=False)
    three_star = models.IntegerField(default=0, blank=False)
    two_star = models.IntegerField(default=0, blank=False)
    one_star = models.IntegerField(default=0, blank=False)

    def __unicode__(self):
        return self.five_star


class ItemAdmin(admin.ModelAdmin):
    list_display = ('asin', 'sku', 'title', 'brand', 'seller', 'description', 'timestamp', )