from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from HR.models import HR_Reg, Applicant_Reg, Employee, HrReport, AddWork


class IndexView(TemplateView):
    template_name = 'admin/admin_index.html'


class ApproveView(View):
    def dispatch(self, request, *args, **kwargs):

        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.save()
        return render(request,'admin/admin_index.html',{'message':" Account Approved"})


class RejectView(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.is_active='0'
        user.save()
        return render(request,'admin/admin_index.html',{'message':"Account Removed"})


class NewHRView(TemplateView):
    template_name = 'admin/appr_HR_manager.html'

    def get_context_data(self, **kwargs):
        context = super(NewHRView,self).get_context_data(**kwargs)
        hr = HR_Reg.objects.filter(user__last_name='0',user__is_staff='0')
        context['hr'] = hr
        return context


class NewApplicantView(TemplateView):
    template_name = 'admin/appr_applicant.html'

    def get_context_data(self, **kwargs):
        context = super(NewApplicantView,self).get_context_data(**kwargs)
        user = Applicant_Reg.objects.filter(user__last_name='0',user__is_staff='0')
        context['user'] = user
        return context


class ApplicantView(TemplateView):
    template_name = 'admin/applicant_view.html'

    def get_context_data(self, **kwargs):
        context = super(ApplicantView,self).get_context_data(**kwargs)
        users = Applicant_Reg.objects.filter(user__last_name='1',user__is_staff='0',user__is_active='1')
        context['user'] =  users
        return context


class HR_ManagerView(TemplateView):
    template_name = 'admin/hr_view.html'

    def get_context_data(self, **kwargs):
        context = super(HR_ManagerView,self).get_context_data(**kwargs)
        hr = HR_Reg.objects.filter(user__last_name='1',user__is_staff='0',user__is_active='1')
        context['hr'] =  hr
        return context


class MyEmployee(TemplateView):
    template_name = 'admin/view_employee.html'

    def get_context_data(self, **kwargs):
        context = super(MyEmployee,self).get_context_data(**kwargs)
        post = Employee.objects.all()
        context['post'] = post
        return context


class HRReport(TemplateView):
    template_name = 'admin/hr_report.html'

    def get_context_data(self, **kwargs):
        context = super(HRReport,self).get_context_data(**kwargs)
        post = HrReport.objects.all()
        context['post'] = post
        return context


class DetailsEmployee(TemplateView):
    template_name = 'admin/employee_details.html'

    def get_context_data(self, **kwargs):
        context = super(DetailsEmployee,self).get_context_data(**kwargs)
        id = self.request.GET['id']
        print(id)
        post = Employee.objects.filter(accept__vacancy__vacancy__hr__id=id)
        context['post'] = post
        return context


class WorkDetails(TemplateView):
    template_name = 'admin/hr_works_view.html'

    def get_context_data(self, **kwargs):
        context = super(WorkDetails,self).get_context_data(**kwargs)
        id = self.request.GET['id']
        print(id)
        post = AddWork.objects.filter(hr__id=id)
        context['post'] = post
        return context