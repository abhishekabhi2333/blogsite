from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,FormView,TemplateView
from.forms import SignupForm,SigninForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.core.mail import send_mail
# Create your views here.

# class Home(View):
#     def get(self,request):
#         return render(request,"home.html")

class Home(TemplateView):
    template_name="home.html"

# class Signup(View):
#     def get(self,request):
#         form=SignupForm()
#         return render(request,"reg.html",{'form':form})
#     def post(self,request):
#         form_data=SignupForm(request.POST)
#         if form_data.is_valid():
#             form_data.save()
            
#             messages.success(request,"user registered successfully")
#             return redirect("Home")
#         else:
#             print(form_data.errors)
#             messages.error(request,"registration failed")
#             return redirect("reg")
class Signup(CreateView):
    model=User
    form_class=SignupForm
    template_name="reg.html"
    success_url=reverse_lazy('Home')

    def post(self,request,*args,**kwargs):
        form_data=self.form_class(request.POST)
        if form_data.is_valid():
            email_id=form_data.cleaned_data.get('email')
            uname=form_data.cleaned_data.get('username')
            pwd=form_data.cleaned_data.get('password1')
            msg="You are registered in BlogApp.\n Your username:"+str(uname)+"\n Password:"+str(pwd)
            form_data.save()
            send_mail(
                'BlogApp Registration',
                msg,
                'abhishekabhi2333@gmail.com',
                [email_id],
                fail_silently=True

            )
            messages.success(request,'Registration Completed!!!')
            return redirect('Home')
        else:
            messages.error(request,'Registration Failed')
            return render(request,"reg.html",{'form':form_data})    


# class Signin(View):
#     def get(self,request):
#         form=SigninForm()
#         return render(request,"log.html",{'form':form})
#     def post(self,request):
#         uname=request.POST.get('username')
#         psw=request.POST.get('password')
#         user=authenticate(request,username=uname,password=psw)
#         if user:
#             login(request,user)
#             return redirect("uhome")
#         else:
#             return redirect("log")  
class Signin(FormView):
    form_class=SigninForm  
    template_name="log.html"
    def post(self,request):
        uname=request.POST.get('username')
        psw=request.POST.get('password')
        user=authenticate(request,username=uname,password=psw)
        if user:
            login(request,user)
            return redirect("uhome")
        else:
            return redirect("log")  

class SignOut(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("log")
