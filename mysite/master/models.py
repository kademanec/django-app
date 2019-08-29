# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
# Create your models here.


class item(models.Model):
    cat_no_type=models.CharField(max_length=200)
    short_desc=models.CharField(max_length=2000)
    long_desc=models.CharField(max_length=2000)
    pom=models.CharField(max_length=200)
    basic_pom=models.CharField(max_length=400)
    purchase_gst=models.FloatField(null=True, blank=True, default=None)
    landed_pur=models.FloatField(null=True, blank=True, default=None)
    selling_uom=models.CharField(max_length=200)
    basicpriceperselling_uom=models.CharField(max_length=300)
    selling_gst_rate=models.CharField(max_length=300)
    landed_selling_price=models.CharField(max_length=200)
    cat_no=models.CharField(max_length=20)

class customer(models.Model):
    cus_grp_name=models.CharField(max_length=200)
    cus_name=models.CharField(max_length=200)
    cus_type=models.CharField(max_length=200)
    cus_address=models.CharField(max_length=2000)
    city=models.CharField(max_length=200)
    country=models.CharField(max_length=200)
    pincode=models.IntegerField(default=10)
    gst_no=models.CharField(max_length=200)
    pan_no=models.CharField(max_length=200)
    contact_person=models.CharField(max_length=200)
    contact_no=models.IntegerField(default=14)
    contact_no1=models.IntegerField(default=14)
    email_id=models.CharField(max_length=200)
    payment_terms=models.CharField(max_length=200)
    customer_no=models.CharField(max_length=20)

class people(models.Model):
    asso_name=models.CharField(max_length=200)
    asso_code_no=models.IntegerField(default=20)
    sex=models.CharField(max_length=200)
    communication_address=models.CharField(max_length=200)
    photo=models.FileField()
    idproof=models.CharField(max_length=200)
    idproof_no=models.CharField(max_length=200)
    join_date=models.DateField(default=datetime.now)
    resign_date=models.DateField(default=datetime.now)
    salarypermonth=models.CharField(max_length=200)
    revised_salary=models.CharField(max_length=200)
