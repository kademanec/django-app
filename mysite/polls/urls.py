from django.conf.urls import url,include
from django.contrib import admin
from . import views,models
from polls.views import productionList,materialsList,itemList,customerList,peopleList


urlpatterns = [

    url(r'^$',views.index,name='index'),
    url(r'^api/customer/',views.customerList.as_view()),
    url(r'^api/production/',views.productionList.as_view()),
    url(r'^api/materials/',views.materialsList.as_view()),
    url(r'^api/item/',views.itemList.as_view()),
    url(r'^api/people/',views.peopleList.as_view()),

]
