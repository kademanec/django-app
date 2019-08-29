# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Production(models.Model):
    packers = models.CharField(max_length=200)
    operators = models.CharField(max_length=200)
    chargemen = models.CharField(max_length=200)
    shiftmen = models.CharField(max_length=200)

class Materials(models.Model):
    chem_soap_noodles = models.CharField(max_length=200)
    perfume = models.CharField(max_length=200)
    packing = models.CharField(max_length=200)
    machinery = models.CharField(max_length=200)
