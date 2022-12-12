from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.db.models import Sum
import csv
from django.views import View
from .forms import *
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from . import helper
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from django.http import JsonResponse
from apps.customer.serializers import *
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
#####################################################################################################################



def createuser(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
            # return HttpResponseRedirect(request.path_info)

    context = {'form': form}
    return render(request, 'adminpanel/UserEntry.html', context)

def createpurchase(request):
    P_form = CreatePurchaseForm()

    if request.method == "POST":
        P_form = CreatePurchaseForm(request.POST)
        if P_form.is_valid():
            P_form.save()
            # return redirect('/')
            return HttpResponseRedirect(request.path_info)

    context = {'P_form': P_form}
    return render(request, 'adminpanel/PurchaseEntry.html', context)

def createpayment(request):
    Pay_form = CreatePaymentForm()

    if request.method == "POST":
        Pay_form = CreatePaymentForm(request.POST, request.FILES)
        if Pay_form.is_valid():
            Pay_form.save()
            # return redirect('/')
            return HttpResponseRedirect(request.path_info)

    context = {'Pay_form': Pay_form}
    return render(request, 'adminpanel/PaymentEntry.html', context)

@csrf_exempt
def user_api(request):
    users = User.objects.all()
    serializer = UserSerializers(users, many=True)
    return JsonResponse(serializer.data, safe=False)


