from django.shortcuts import render
from django.views.generic import TemplateView

from HR.models import Vacancy, Applicant_Reg, Apply_Vacancy, Interview, Accept_App, Employee


class IndexView(TemplateView):
    template_name = 'applicants/app_index.html'


class VacancyView(TemplateView):
    template_name = 'applicants/vacancy_view.html'

    def get_context_data(self, **kwargs):
        context = super(VacancyView,self).get_context_data(**kwargs)
        post = Vacancy.objects.filter(status='new')
        context['post'] = post
        return context


class ApplyVacancy(TemplateView):
    template_name = 'applicants/apply_vacancy.html'

    def post(self, request,*args,**kwargs):
        id = request.GET['id']
        vacancy = Vacancy.objects.get(pk=id)
        ima = request.FILES['image']
        user = self.request.user.id
        users = Applicant_Reg.objects.get(user=user)

        add = Apply_Vacancy()
        add.user = users
        add.vacancy = vacancy
        add.cv = ima
        add.status = 'Apply'
        add.save()
        messages = "Successfully Applied"
        return render(request, 'applicants/apply_vacancy.html', {'message': messages})


class InterviewCall(TemplateView):
    template_name = 'applicants/interview_call.html'

    def get_context_data(self, **kwargs):
        context = super(InterviewCall,self).get_context_data(**kwargs)
        user = self.request.user.id
        post = Interview.objects.filter(apply__user__user=user, status='Interview')
        context['post'] = post
        return context


class AcceptAppli(TemplateView):
    template_name = 'applicants/application_accepted.html'

    def get_context_data(self, **kwargs):
        context = super(AcceptAppli,self).get_context_data(**kwargs)
        user = self.request.user.id
        post = Accept_App.objects.filter(vacancy__user__user=user, status='Sent Offer')
        context['post'] = post
        return context


class EmployeeDetails(TemplateView):
    template_name = 'applicants/employee_details.html'

    def get_context_data(self, **kwargs):
        context = super(EmployeeDetails,self).get_context_data(**kwargs)
        user = self.request.user.id
        post = Employee.objects.filter(accept__vacancy__user__user=user, accept__status='Add As Employee')
        context['post'] = post
        return context
