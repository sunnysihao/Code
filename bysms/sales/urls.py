# -*- coding = utf-8 -*-
from django.urls import path
from sales import views
from sales.views import listcustomers

urlpatterns = [
    path('orders/', views.listorders),
    path('hello/', views.hello),
    path('customers/', listcustomers)
    ]