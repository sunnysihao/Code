from django.db import models

class Customer(models.Model):
    #客户名称
    name = models.CharField(max_length= 200)
    #联系电话
    phonenumber = models.CharField(max_length= 200)
    #地址
    addresss = models.CharField(max_length=200)
    #QQ
    qq = models.CharField(max_length=200,null= True)

from django.contrib import admin

admin.site.register(Customer)