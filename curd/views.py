from distutils.log import error
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
from . forms import *
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from .serializers import *


class ListCategory(generics.ListCreateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

class  DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

class ListProduct(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class ListBlog(generics.ListCreateAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer

class DetailBlog(generics.RetrieveUpdateDestroyAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer




       




def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user=form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("login")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})


def login_request(request):
    newform=AuthenticationForm()
    if request.method=="POST":
        
        print(newform)    
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.info(request, f"you are logged in as {{username}}.")
            return redirect('/')
        else:
            messages.error(request,"invalid username or password")
    
    
    return render(request,"login.html",{"login_form":newform})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("register")

@login_required(login_url='login')
def add_blog(request):
    addform=BlogaddForm()
    if request.method=="POST":
        addform=BlogaddForm(request.POST,request.FILES)
        if addform.is_valid():
            addform=addform.save(commit=False)
            addform.user=request.user
            addform.save()
            return redirect('/')
            
        else:
            addform=BlogaddForm()
    
    return render(request,"addblog.html",{'form':addform})

def allblog(request):
    show_all=Blog.objects.all()
    return render(request,"allblog.html",{'all':show_all})

@login_required(login_url='login')
def editblog(request,id):
    get_id=Blog.objects.get(id=id)
    updateform=BlogaddForm(request.POST or None,request.FILES or None, instance=get_id)
    if request.method=="POST":
        if updateform.is_valid():
            updateform.save()
            return redirect('/')
    return render(request,"editblog.html",{'form':updateform})

@login_required(login_url='login')
def deleteblog(request,id):
    db=Blog.objects.get(id=id)
    db.delete()
    return redirect("/")

@login_required(login_url='login')
def detail(request,id):
    detail=Blog.objects.get(id=id)
    return render(request,"detail.html",{'desc':detail})
    
@login_required(login_url='login')
def myblog(request):
    user=request.user
    post=Blog.objects.filter(user=user).order_by('-id')


    data = {} 
    data['post'] = post 
    return render(request,'myblog.html',data)

@login_required(login_url='login')
def profile(request):
    user=request.user
    return render(request,"profile.html",{'user':request.user})
