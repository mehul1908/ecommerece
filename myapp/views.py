from django.shortcuts import render , get_object_or_404 , redirect
from django.http import HttpResponse 
from django.views import View
from django.contrib.auth import logout
from . import forms
from . import models
# Create your views here.

def index(request):
    return render(request,'base.html')

class Login(View):
    def get(self , request):
        myform=forms.UserMasterForm()
        return render(request,'login.html',{'myform':myform})
    def post(self , request):
        data = get_object_or_404(models.UserMaster , userid=request.POST['userid'])
        if data.password==request.POST['password']:
            request.session['userid']=request.POST['userid']
            request.session['username']=models.UserProfile.objects.filter(userid=request.POST['userid'])[0].username
            return redirect('home')
        else:
            return HttpResponse("Invalid credentials")
        
class AddUserMaster(View):
    def get(self , request):
        myform=forms.UserMasterForm()
        return render(request , 'addusermaster.html' , {'myform':myform})
    def post(self , request):
        myform=forms.UserMasterForm(request.POST)
        if myform.is_valid():
            myform.save()
            return redirect("adduserprofile")
        else:
            return HttpResponse("Invalid Data")
        
class AddUserProfile(View):
    def get(self , request):
        myform=forms.UserProfileForm()
        return render(request , 'adduserprofile.html' , {'myform':myform})
    def post(self , request):
        myform=forms.UserProfileForm(request.POST)
        if myform.is_valid:
            myform.save()
            return redirect("login")
        else:
            return HttpResponse("Invalid Data")
        
def logouts(request):
    logout(request)
    return redirect('login')

class AddProdCat(View):
    def get(self , request):
        myform=forms.ProductCategoryForm()
        return render(request,'addprocat.html',{'myform':myform})
    def post(self,request):
        myform=forms.ProductCategoryForm(request.POST)
        if myform.is_valid():
            myform.save()
            return redirect('home')
        else:
            return HttpResponse("Invalid Details....")
        
def showProCat(request):
    data=models.ProductCategory.objects.all()
    return render(request,'showprocat.html',{'data':data})

class editprocat(View):
    def get(self , request, id):
        data=models.ProductCategory.objects.get(pcid=id)
        myform=forms.ProductCategoryForm(instance=data)
        return render(request,'editprocat.html',{'myform':myform})
    def post(self,request,id):
        data=models.ProductCategory.objects.get(pcid=id)
        myform=forms.ProductCategoryForm(request.POST ,instance=data)
        if myform.is_valid():
            myform.save()
            return redirect('showprocat')
        else:
            return HttpResponse("Invalid Details....")
        
def delprocat(request,id):
    data=models.ProductCategory.objects.get(pcid=id)
    data.delete()
    return redirect("showprocat")

#for product

class AddProd(View):
    def get(self , request):
        myform=forms.ProductForm()
        return render(request,'addpro.html',{'myform':myform})
    def post(self,request):
        myform=forms.ProductForm(request.POST)
        if myform.is_valid():
            myform.save()
            return redirect('home')
        else:
            return HttpResponse("Invalid Details....")
        
def showPro(request):
    data=models.Product.objects.all()
    return render(request,'showpro.html',{'data':data})

class editpro(View):
    def get(self , request, id):
        data=get_object_or_404(models.Product , pid=id)
        myform=forms.ProductForm(instance=data)
        return render(request,'editpro.html',{'myform':myform})
    def post(self,request,id):
        data=get_object_or_404(models.Product , pid=id)
        myform=forms.ProductForm(request.POST ,instance=data)
        if myform.is_valid():
            myform.save()
            return redirect('showpro')
        else:
            return HttpResponse("Invalid Details....")
        
def delpro(request,id):
    data=models.Product.objects.get(pid=id)
    data.delete()
    return redirect("showpro")

def showuser(request):
    data = models.UserProfile.objects.all()
    return render(request , 'showuser.html' , {'data':data})

class edituser(View):
    def get(self , request, id):
        data=models.UserProfile.objects.get(userid=id)
        myform=forms.UserProfileForm(instance=data)
        return render(request,'edituser.html',{'myform':myform})
    def post(self,request,id):
        data=models.UserProfile.objects.get(userid=id)
        myform=forms.UserProfileForm(request.POST ,instance=data)
        if myform.is_valid():
            
            myform.save()
            return redirect('showuser')
        else:
            return HttpResponse("Invalid Form")
def deluser(request,id):
    data=models.UserMaster.objects.get(userid=id)
    data.delete()
    return redirect("showuser")