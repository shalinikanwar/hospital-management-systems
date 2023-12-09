from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
# Create your views here.
from .models import profilepic
from django.contrib.auth.decorators import login_required
@login_required
def home(request):
	
	pr=profilepic.objects.all().filter(user=request.user)
	c={"img":pr}
	return render(request,"home.html",c)
def signin(request):
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		user=authenticate(username=username,password=password)
		if user is not None:
			login(request,user)
			return redirect('/home')
		else:
			return redirect('/signin')
	else:
		return render(request,"login.html")
def signout(request):
	logout(request)
	return redirect("/signin")
def signup(request):
	if request.method=='POST':
	  username=request.POST['username']
	  password=request.POST['password']
	  confirmpassword=request.POST['confirmpassword']
	  if (password==confirmpassword):
	      user=User.objects.create_user(username=username,password=password)
	      user.save()
	      login(request,user)
	      return redirect('/signin')
	  else:
	      return redirect('/signup')
	else:
	  return render(request,'signup.html')
	
def upload(request):
	if request.user.is_authenticated:
		if request.method=='POST':
			pr=profilepic.objects.all().filter(user=request.user)
			pr.delete()
			image=request.FILES['image']
			userpro=profilepic(user=request.user,image=image)
			userpro.save()
			return redirect('/home')
		else:
			return redirect('/home')
	else:
		return redirect('/home')