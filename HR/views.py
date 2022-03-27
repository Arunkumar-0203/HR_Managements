from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import TemplateView

from HR.models import UserType, Applicant_Reg, HR_Reg


class IndexView(TemplateView):
    template_name = 'index.html'


class AppRegister(TemplateView):
    template_name = 'registration.html'

    def post(self, request,*args,**kwargs):
        fullname = request.POST['name']
        address = request.POST['address']
        contact = request.POST['contact']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        try:
             user = User.objects.create_user(username=username,password=password,first_name=fullname,email=email,last_name=0)
             user.save()
             reg = Applicant_Reg()
             reg.user = user
             reg.address = address
             reg.contact = contact
             reg.save()
             usertype = UserType()
             usertype.user = user
             usertype.type = "user"
             usertype.save()
             return redirect('user_register')
        except:
             messages = "Register Successfully"
             return render(request,'registration.html',{'message':messages})


class HRRegister(TemplateView):
    template_name = 'hr_registration.html'

    def post(self, request,*args,**kwargs):
        fullname = request.POST['name']
        depart = request.POST['dept']
        code = request.POST['code']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        try:
             user = User.objects.create_user(username=username,password=password,first_name=fullname,email=email,last_name=0)
             user.save()
             reg = HR_Reg()
             reg.user = user
             reg.department = depart
             reg.code = code
             reg.save()
             usertype = UserType()
             usertype.user = user
             usertype.type = "hr"
             usertype.save()
             return redirect('hr_registration')
        except:
             messages = "Register Successfully"
             return render(request,'registration.html',{'message':messages})



class LoginView(TemplateView):
    template_name = 'login.html'

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password= request.POST['password']
        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            if user.last_name == '1':
                if user.is_superuser:
                    return redirect('/admin')
                elif UserType.objects.get(user_id=user.id).type == "user":
                    return redirect('/applicants')
                elif UserType.objects.get(user_id=user.id).type == "hr":
                    return redirect('/hr')
                else:
                    return redirect('/employee')
            else:
                return render(request,'login.html',{'message':" User Account Not Authenticated"})
        else:
            return render(request,'login.html',{'message':"Invalid Username or Password"})