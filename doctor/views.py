from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import View
from .forms import AdmitForm,Calculator,Patientform,Docterform
from django.contrib import messages
from .models import Patient,Doctor
from django.utils.decorators import method_decorator



#decorators

def signin_required(fn):
    def inner(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fn(request,*args,**kwargs)
        else:
            messages.error(request,"login required")
            return redirect("login")
    return inner

# Create your views here.

def first_request(request):
    return HttpResponse("<h1>Hello World</h1>")

def second_request(request):
    return HttpResponse("<h1>Welcome To Django</h1>")

def demo(request):
    return render(request,"demo.html")



@method_decorator(signin_required,name="dispatch")   
class Addpatient(View):
    def get(self,request,*args,**kwargs):
        return render(request,"addpatient.html")
    def post(self,request,*args,**kwargs):
        name=request.POST.get("name")
        age=request.POST.get("age")
        address=request.POST.get("addr")
        phone=request.POST.get("phone")
        Patient.objects.create(name=name,age=age,address=address,phone=phone)
        messages.success(request,"patient details added !!")
        return redirect("home")
    
    
@method_decorator(signin_required,name="dispatch")      
class Addprescription(View):
    def get(self,request,*args,**kwargs):
        return render(request,"addprescription.html")
    def post(self,request,*args,**kwargs):
        disease=request.POST.get("dname")
        datede=request.POST.get("ddate")
        prescription=request.POST.get("pname")
       
        return HttpResponse("submitted values : "+disease+','+datede+','+prescription)
    
    
@method_decorator(signin_required,name="dispatch")      
class Add(View):
    def get(self,request,*args,**kwargs):
        return render(request,"add.html")
    def post(self,request,*args,**kwargs):
        print (request.POST)
        n1=int(request.POST.get("n1"))
        n2=int(request.POST.get("n2"))
        add= n1+n2
        # return HttpResponse("Value After Addition : "+str(add))
        return render(request,"add.html",{"add":add})
    
    
@method_decorator(signin_required,name="dispatch")       
class Count_str(View):
    def get(self,request,*args,**kwargs):
        return render(request,"count.html")
    def post(self,request,*args,**kwargs):
        print (request.POST)
        wd=request.POST.get("cname")
        
        counts = dict()
        word = wd.split()
        
        for i in word:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
                
        fc = str(counts)
        # return HttpResponse("count of string :"+fc)
        return render(request,"strcount.html",{"counts":counts})
    
    
@method_decorator(signin_required,name="dispatch")      
class AdmitView(View):
    def get(self,request,*args,**kwargs):
        form =AdmitForm()
        return render(request,"admitreq.html",{"frm":form})
    def post(self,request,*args,**kwargs):
        form_data=AdmitForm(data=request.POST)
        if form_data.is_valid():
            # return HttpResponse("posted")
            name=form_data.cleaned_data.get("name")
            ag=form_data.cleaned_data.get("age")
            dis=form_data.cleaned_data.get("disease")
            dt=form_data.cleaned_data.get("date")
            adno=form_data.cleaned_data.get("admission_no")
            otp=form_data.cleaned_data.get("otp")
            print(name,ag,dis,dt,adno,otp)
            messages.success(request,"Submission Successfull !!")
            messages.error(request,"Data not stored")
            return redirect("home")
        else:
            messages.error(request,"Invalid data submission failed !!")
            return render(request,"admitreq.html",{"frm":form_data})
        
@method_decorator(signin_required,name="dispatch")          
class Calcu(View):
    def get(self,request,*args,**kwargs):
        form = Calculator()
        return render(request,"calculator.html",{"frm":form})
    def post(self,request,*args,**kwargs):
        form_data=Calculator(data=request.POST)
        if form_data.is_valid():
            value=form_data.cleaned_data.get("value")
            res=eval(value)
            return render(request,"calculator.html",{"cal":res})
        
        
        
@method_decorator(signin_required,name="dispatch")      
class Viewpatient(View):
     def get(self,request,*args,**kwargs):
        res=Patient.objects.all()
        return render(request,"viewpatient.html",{"data":res})
        
    
@method_decorator(signin_required,name="dispatch")    
class Deletepatient(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pid")
        pat=Patient.objects.get(id=id)
        pat.delete()
        return redirect("viewpat")
    
    
@method_decorator(signin_required,name="dispatch")     
class Editpatient(View):
    def get(self,request,*args,**kwargs):
        pid=kwargs.get("pid")
        pt=Patient.objects.get(id=pid)
        form=Patientform(initial={"name":pt.name,"age":pt.age,"address":pt.address,"phone":pt.phone})
        return render(request,"editpatient.html",{"form":form})
    def post(self,request,*args,**kwargs):
        pid=kwargs.get("pid")
        pt=Patient.objects.get(id=pid)
        form_data=Patientform(data=request.POST)
        if form_data.is_valid():
            nm=form_data.cleaned_data.get("name")
            ag=form_data.cleaned_data.get("age")
            addr=form_data.cleaned_data.get("address")
            ph=form_data.cleaned_data.get("phone")
            pt.name=nm
            pt.age=ag
            pt.address=addr
            pt.phone=ph
            pt.save()
            messages.success(request,"patient details updated")
            return redirect("viewpat")
        else:
            return render(request,"editpatient.html",{"form":form_data})
        
        
@method_decorator(signin_required,name="dispatch")        
class DoctorAform(View):
    def get(self,request):
        
            form=Docterform()
            return render(request,"adddoctor.html",{"form":form})
    def post(self,request):
        form_data=Docterform(data=request.POST,files=request.FILES)
        if form_data.is_valid():
            form_data.save()
            messages.success(request,"Doctor Registerd")
            return redirect("home")
        else:
            return render(request,"adddoctor.html",{"form":form_data})
        
        
@method_decorator(signin_required,name="dispatch") 
class Doctorview(View):
     def get(self,request):
        res=Doctor.objects.all()
        return render(request,"viewdoctor.html",{"data":res})
    
    
@method_decorator(signin_required,name="dispatch") 
class Deletedoctor(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pid")
        doc=Doctor.objects.get(id=id)
        doc.delete()
        return redirect("viewdoc")
    
@method_decorator(signin_required,name="dispatch") 
class Editdoctor(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("did")
        doc=Doctor.objects.get(id=id)
        form=Docterform(instance=doc)
        return render(request,"editdoctor.html",{"form":form})
    def post(self,request,*args,**kwargs):
        id=kwargs.get("did")
        doc=Doctor.objects.get(id=id)
        form_data=Docterform(data=request.POST,instance=doc,files=request.FILES)
        if form_data.is_valid():
            form_data.save()
            messages.success(request,"doctor updated !!")
            return redirect("viewdoc")
        else:
            return render(request,"editdoctor.html",{"form":form_data})
