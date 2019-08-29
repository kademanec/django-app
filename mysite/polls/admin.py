# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Production,Materials
from master.models import customer,item,people

# Register your models here.
admin.site.register(customer)
admin.site.register(Production)
admin.site.register(Materials)
admin.site.register(item)
admin.site.register(people)
