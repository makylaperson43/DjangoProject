from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from app.models import Book
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .models import *
from .forms import BookForm, CreateUserForm
from .filters import OrderFilter
from .decorators import unauthenticated_user, allowed_users, admin_only

# Create your views here.
@unauthenticated_user
def registerPage(request):

	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			group = Group.objects.get(name='person')
			user.groups.add(group)

			messages.success(request, 'Account was created for ' + username)

			return redirect('login')
 

	context = {'form':form}
	return render(request, 'register.html', context)

@unauthenticated_user
def loginPage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'login.html', context)
    
def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
@admin_only

def home(request):
	books = Book.objects.all()
	context = {'books':books}
	return render(request, 'dashboard.html', context)

def userPage(request):
	books = Book.objects.all()
	context = {'books':books}
	return render(request, 'user.html', context)


@login_required(login_url='login')
def createPurchase(request):
	form = BookForm()
	if request.method == "POST":
		form = BookForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("home")
	context = {"form":form}
	return render(request, 'purchase.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updatePurchase(request, pk):

	purchase = Book.objects.get(id=pk)
	form = BookForm(instance=purchase)

	if request.method == 'POST':
		form = BookForm(request.POST, instance=purchase)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'purchase.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deletePurchase(request, pk):
	purchase = Book.objects.get(id=pk)
	if request.method == "POST":
		purchase.delete()
		return redirect('home')

	context = {'item':purchase}
	return render(request, 'delete.html', context)