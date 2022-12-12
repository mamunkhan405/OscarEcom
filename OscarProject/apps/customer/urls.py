from django.urls import path
from . import views

app_name = 'users'
urlpatterns=[
    path('createuser/', views.createuser, name= 'createuser'),
    path('createpurchase/', views.createpurchase, name= 'createpurchase'),
    path('createpayment/', views.createpayment, name= 'createpayment'),
    

]