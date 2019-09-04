# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Production,Materials
from master.models import customer,item,people,reports,inventory,sales,purchase

# Register your models here.
admin.site.register(customer)
admin.site.register(Production)
admin.site.register(Materials)
admin.site.register(item)
admin.site.register(people)
admin.site.register(reports)
admin.site.register(inventory)
admin.site.register(sales)
admin.site.register(purchase)
