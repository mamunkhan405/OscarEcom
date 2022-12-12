from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.db.models import Sum
import csv
from django.views import View
from .forms import *
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
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

