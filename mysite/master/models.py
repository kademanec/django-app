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

class inventory(models.Model):
    entry_type = models.CharField(max_length=500)
    gr_no = models.IntegerField(default=14)
    vendor_name = models.CharField(max_length=500)
    invoice_no = models.IntegerField(default=14)
    invoice_date = models.DateField(default=datetime.now)
    po_num = models.IntegerField(default=14)
    vehicle_no = models.IntegerField(default=14)
    item_code = models.CharField(max_length=500)
    item_desc = models.CharField(max_length=500)
    qty_recieved = models.IntegerField(default=14)
    uom = models.IntegerField(default=14)
    qty_per_uom = models.IntegerField(default=14)

class sales(models.Model):
    entry_type = models.CharField(max_length=500)
    cus_grp_name=models.CharField(max_length=200)
    cus_name=models.CharField(max_length=200)
    cus_po_num = models.IntegerField(default=1234567890)
    cus_po_date = models.DateField(default=datetime.now)
    payment_terms= models.CharField(max_length=200)
    bill_to_add = models.CharField(max_length=300)
    ship_to_add = models.CharField(max_length=300)
    item_entry =  models.CharField(max_length=300)
    shipping_terms = models.CharField(max_length=300)
    cus_po_tc =  models.CharField(max_length=300)
    other_info =  models.CharField(max_length=300)
    basic_value = models.CharField(max_length=300)
    gst_value = models.CharField(max_length=300)
    total_value = models.CharField(max_length=300)
    cus_date = models.DateField(default=datetime.now)
    ef_planned_date_del=models.DateField(default=datetime.now)
    ef_actual_deliery_date = models.DateField(default=datetime.now)
    payment_date =models.DateField(default=datetime.now)

class purchase(models.Model):
    po_type = models.CharField(max_length=500)
    sales_order_ref = models.CharField(max_length=300)
    vendor_name = models.CharField(max_length=300)
    payment_terms = models.CharField(max_length=500)
    bill_to_add = models.CharField(max_length=500)
    ship_to_add = models.CharField(max_length=500)
    item_entry = models.CharField(max_length=500)
    shipping_terms = models.CharField(max_length=500)
    po_tc =  models.CharField(max_length=500)
    other_info = models.CharField(max_length=500)
    po_basic =  models.CharField(max_length=500)
    po_gst =  models.CharField(max_length=500)
    total_po =  models.CharField(max_length=500)
    payment_date =  models.DateField(default=datetime.now)
    po_no = models.DateField(default=datetime.now)

class reports(models.Model):
    field_head=models.CharField(max_length=200)
    info_req=models.CharField(max_length=500)
    control=models.CharField(max_length=100)
