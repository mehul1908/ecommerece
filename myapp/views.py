from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from . import models,forms
from django.views import View
from django.contrib.auth import logout
import json
from datetime import datetime

def index(request):
    return render(request,'base.html')

class Login(View):
    def get(self,request):
        myform=forms.UserMasterForm()
        return render(request,'login.html',{'myform':myform})
    def post(self,request):
        uid=request.POST['userid']
        pwd=request.POST['password']
        userdata=models.UserMaster.objects.filter(userid=uid).filter(password=pwd)
        if userdata:
            for dt in userdata:
                request.session['userid']=dt.userid
                request.session['usertype']=dt.usertype
                uobj=get_object_or_404(models.UserProfile , userid=dt.userid)
                request.session['username']=uobj.username
            print("Userid is : ",request.session['userid'])
            print("Username is : ",request.session['username'])
            print("Usertype  : ",request.session['usertype'])
            return redirect("home")
        else:
            return HttpResponse("<h1>Invalid credentials.....</h1>")
        
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
            return redirect("home")
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

class Search(View):
    prolist=[]
    def get(self,request):
        data=models.ProductCategory.objects.all()
        return render(request,template_name="searchpro.html",context={'mydata':data})
    def post(self,request):
        pid=request.POST['pid']
        self.prolist.append(pid)
        request.session['cart']=self.prolist
        return redirect("home")

def getProduct(request):
    data=models.Product.objects.filter(pcid=request.GET['pcid'])
    mypro=[]
    for dt in data :
            prodict={'pid':dt.pid,'pdesc':dt.pdesc,'pname':dt.pname,'price':dt.price,'discount':dt.discount}
            mypro.append(prodict)
            # print(dt.pname+"-"+str(dt.price))
    prodata=json.dumps(mypro)
    return HttpResponse(prodata)

class CartMgmt(View):
    def get(self,request):
        cart=request.session['cart']
        mypro=[]
        totpr=0;
        totnp=0;
        for ct in cart:
            pro=models.Product.objects.get(pid=ct)
            netprice=pro.price-(pro.price*(pro.discount/100))
            totpr=totpr+pro.price
            totnp=totnp+netprice
            prodict={'pid':pro.pid,'pname':pro.pname,'price':pro.price,'disc':pro.discount,'netprice':netprice,'pdesc':pro.pdesc}
            mypro.append(prodict)
        return render(request,'cart.html',{'mydata':mypro,'totpr':totpr,'totnp':totnp})
    def post(self,request):
        try:
            oid=models.Order.objects.all().order_by('-ordid')[0].ordid
        except:
            oid=0;
        print("order id is : ",oid+1)
        orddt=datetime.today().date();
        # print("order date is : ",orddt)
        uid=models.UserMaster.objects.get(userid=request.session['userid'])
        # print("userid is : ",uid)
        chk=request.POST.getlist("chk")
        amt=0;
        for pro in chk:
            product=models.Product.objects.get(pid=pro)
            amt=amt+product.price-(product.price*(product.discount/100))
            request.session['cart'].remove(pro)
            request.session.modified=True
        # print("Amount is : ",amt)
        ord=models.Order(ordid=oid+1,orddt=orddt,amount=amt,userid=uid)
        ord.save();
        return redirect('showcart')


        
        return HttpResponse("Hi")

def deleteProduct(request,id):
    request.session['cart'].remove(id)
    request.session.modified=True
    return redirect('showcart')


def showOrder(request):
    utype=request.session['usertype']
    if(utype=='admin'):
        data=models.Order.objects.all();
    else:
        data=models.Order.objects.filter(userid=request.session['userid'])
    return render(request,'order.html',{'mydata':data})


class AddComplaint(View):
    def get(self,request):
        form=forms.ComplaintForm();
        return render(request,'addcomp.html',{'myform':form})
    def post(self,request):
        form=forms.ComplaintForm(request.POST)
        try:
            cid=models.Complaint.objects.all().order_by('-compid')[0].compid
        except:
            cid=0;
        compdt=datetime.today().date();
        if form.is_valid():
            desc=request.POST['compdesc']
            uid=models.UserMaster.objects.get(userid=request.session['userid'])
            obj=models.Complaint(compid=cid+1,compdesc=desc,compdt=compdt,response="",userid=uid)
            obj.save();
        return redirect('home')


def showComplaints(request):
    utype=request.session['usertype']
    if(utype=='admin'):
        data=models.Complaint.objects.all();
    else:
        data=models.Complaint.objects.filter(userid=request.session['userid'])
    return render(request,'showcomps.html',{'mydata':data})

class Response(View):
    def get(self,request,id):
        pass
    def post(self,request,id):
        pass