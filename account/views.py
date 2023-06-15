from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import View
from .forms import RegisterForm,Managerform,Regform,Logform
from django.contrib import messages
from .models import Manager
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator





def signin_required(fn):
    def inner(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fn(request,*args,**kwargs)
        else:
            messages.error(request,"login required")
            return redirect("login")
    return inner


# Create your views here.
def register(request):
    return render(request,"register.html")

def demo(request):
    return render(request,"demo.html")

def home(request):
    user=request.user
    name="Athulya"
    names=["Anandhu","amal","anu"]
    # students=[
    #     {"name":"Anagha","age":22,"course":"MCA"},
    #     {"name":"Anu","age":22,"course":"BCA"},
    #     {"name":"Amal","age":22,"course":"btech"},
    # ]
    students=[]
    teachers=[
        {"name":"Anagha","age":40,"qualification":"MCA"},
        {"name":"Anu","age":37,"qualification":"BCA"},
        {"name":"Amal","age":26,"qualification":"btech"},
    ]
    return render(request,"home.html",{"data":name,"list":names,"stu":students,"teach":teachers,"us":user})


def Login(request):
    if request.method=="GET":
        return render(request,"login.html")
    elif request.method=="POST":
        print(request.POST)
        uname=request.POST.get("uname")
        pasword=request.POST.get("pswd")
        return HttpResponse("post request:"+uname+","+pasword)


   
def add(request):
    if request.method=="GET":
        return render(request,"addition.html")
    elif request.method=="POST":
        print (request.POST)
        n1=int(request.POST.get("n1"))
        n2=int(request.POST.get("n2"))
        add= n1+n2
        return HttpResponse("Value After Addition : "+str(add))
        # return render(request,"addition.html",{"add":add})


def count(request):
    if request.method=="GET":
        return render(request,"count.html")
    elif request.method=="POST":
        print (request.POST)
        wd=request.POST.get("cname")
        
        count = dict()
        word = wd.split()
        
        for i in word:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
                
        fc = str(count)
        # return HttpResponse("count of string :"+fc)
    return render(request,"count.html",{"count":count})


# class Log(View):
#     def get(self,request,*args,**kwargs):
#         form =Login()
#         return render(request,"login.html",{"lg":form})
#     def post(self,request,*args,**kwargs):
#         form_data=Login(data=request.POST)
#         print(form_data)
#         return HttpResponse("login successfully")
        
        
        
@method_decorator(signin_required,name="dispatch") 
class RegisterView(View):
    def get(self,request,*args,**kwargs):
        form =RegisterForm()
        return render(request,"register.html",{"rg":form})
    def post(self,request,*args,**kwargs):
        form_data=RegisterForm(data=request.POST)
        print(form_data)
        return HttpResponse("posted")
    
@method_decorator(signin_required,name="dispatch") 
class Addmanager(View):
    def get(self,request,*args,**kwargs):
        form=Managerform()
        return render(request,"addmanager.html",{"form":form})
    def post(self,request,*args,**kwargs):
        FIRST_NAME=request.POST.get("FIRST_NAME")
        SECOND_NAME=request.POST.get("SECOND_NAME")
        DOB=request.POST.get("DOB")
        PHONE=request.POST.get("PHONE")
        EMAIL=request.POST.get("EMAIL")
        QUALIFICATION=request.POST.get("QUALIFICATION")
        Manager.objects.create(FIRST_NAME=FIRST_NAME,SECOND_NAME=SECOND_NAME,DOB=DOB,PHONE=PHONE,EMAIL=EMAIL,QUALIFICATION=QUALIFICATION)
        messages.success(request,"manager details added !!")
        return redirect("home")
        # return HttpResponse("submitted values : "+fname+','+sname+','+dob+','+phone+','+email+','+qualification)
        
        
@method_decorator(signin_required,name="dispatch") 
class Viewmanger(View):
    def get(self,request,*args,**kwargs):
        res=Manager.objects.all()
        return render(request,"viewmanager.html",{"data":res})
        
@method_decorator(signin_required,name="dispatch") 
class Deletemanager(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("mid")
        man=Manager.objects.get(id=id)
        man.delete()
        return redirect("managerview")
        
        
        
@method_decorator(signin_required,name="dispatch")         
class Editmanager(View):
    def get(self,request,*args,**kwargs):
        mid=kwargs.get("mid")
        man=Manager.objects.get(id=mid)
        form=Managerform(initial={"FIRST_NAME":man.FIRST_NAME,"SECOND_NAME":man.SECOND_NAME,"DOB":man.DOB,"PHONE":man.PHONE,"EMAIL":man.EMAIL,"QUALIFICATION":man.QUALIFICATION})
        return render(request,"editmanager.html",{"form":form})
    def post(self,request,*args,**kwargs):
        mid=kwargs.get("mid")
        man=Manager.objects.get(id=mid)
        form_data=Managerform(data=request.POST)
        if form_data.is_valid():
            fnm=form_data.cleaned_data.get("FIRST_NAME")
            snm=form_data.cleaned_data.get("SECOND_NAME")
            dob=form_data.cleaned_data.get("DOB")
            ph=form_data.cleaned_data.get("PHONE")
            em=form_data.cleaned_data.get("EMAIL")
            qli=form_data.cleaned_data.get("QUALIFICATION")
            man.FIRST_NAME=fnm
            man.SECOND_NAME=snm
            man.DOB=dob
            man.PHONE=ph
            man.EMAIL=em
            man.QUALIFICATION=qli
            man.save()
            messages.success(request,"manager details updated")
            return redirect("managerview")
        else:
            return render(request,"editmanager.html",{"form":form_data})
        
        
        
class Regview(View):
    def get(self,request):
        form=Regform()
        return render(request,"reg.html",{"form":form})
    def post(self,request):
        form_data=Regform(data=request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect("login")
        else:
            return render(request,"reg.html",{"form":form_data})
        
        
        
class Logview(View):
    def get(self,request):
        form=Logform()
        us=request.user
        return render(request,"log.html",{"form":form,"user":us})
    def post(self,request):
        form_data=Logform(data=request.POST)
        if form_data.is_valid():
            user=form_data.cleaned_data.get("username")
            pswd=form_data.cleaned_data.get("password")
            user_ob=authenticate(request,username=user,password=pswd)
            if user_ob:
                login(request,user_ob)
                messages.success(request,"Login Successfull !!")
                return redirect("home")
            else:
                messages.error(request,"Login Failed !! Invalid username and password")
                return render(request,"log.html",{"form":form_data})
            
            
class Logoutview(View):
    def get(self,request):
        logout(request)
        return redirect("login")

    
    
    

        
       
        