from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import serializers
from master.models import item,customer,people


class itemSerializer(serializers.ModelSerializer):
    class Meta:
        model = item
        fields = ['cat_no_type', 'short_desc', 'long_desc','pom','basic_pom','purchase_gst','landed_pur','selling_uom','basicpriceperselling_uom','selling_gst_rate','landed_selling_price','cat_no']

class customerSerializer(serializers.ModelSerializer):
    class Meta:
        model = customer
        fields = ['cus_grp_name', 'cus_name', 'cus_type','cus_address','city','country','pincode','gst_no','pan_no','contact_person','contact_no','contact_no1','email_id','payment_terms','customer_no']

class peopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = people
        fields = ['asso_name', 'asso_code_no', 'sex','communication_address','photo','idproof','idproof_no','join_date','resign_date','salarypermonth','revised_salary']
