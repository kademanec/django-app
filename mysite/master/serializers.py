from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import serializers
from master.models import item,customer,people,reports,inventory,sales,purchase


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

class reportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = reports
        fields = ['field_head', 'info_req', 'control']

class inventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = inventory
        fields = ['entry_type', 'gr_no', 'vendor_name','invoice_no','invoice_date','po_num','vehicle_no','item_code','item_desc','qty_recieved','uom','qty_per_uom']

class salesSerializer(serializers.ModelSerializer):
    class Meta:
        model = sales
        fields = ['entry_type','cus_grp_name','cus_name','cus_po_num','cus_po_date','payment_terms','bill_to_add','ship_to_add','item_entry','shipping_terms','cus_po_tc','other_info','basic_value','gst_value','total_value','cus_date','ef_planned_date_del','ef_actual_deliery_date','payment_date']


class purchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = purchase
        fields = ['po_type', 'sales_order_ref', 'vendor_name','payment_terms','bill_to_add','ship_to_add','item_entry','shipping_terms','po_tc','other_info','po_basic','po_gst','total_po','payment_date','po_no']
