from datetime import datetime, date

from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import TemplateView

from HR.download import download
from HR.models import Vacancy, HR_Reg, Apply_Vacancy, Interview, Accept_App, Employee, UserType, Leave, Applicant_Reg, \
    EmpAttandance, AddWork, AddWorkStatus, AttReport, HrReport


class IndexView(TemplateView):
    template_name = 'hr/hr_index.html'


class AddVacancy(TemplateView):
    template_name = 'hr/add_vacancy.html'
    def post(self, request,*args,**kwargs):

        vacancy = request.POST['vacancy']
        date = request.POST['date']
        name = request.POST['name']
        user = self.request.user.id
        users = HR_Reg.objects.get(user=user)

        add = Vacancy()
        add.hr = users
        add.vacancy = vacancy
        add.date = date
        add.name = name
        add.status = 'new'
        add.save()
        messages = "Successfully Added"
        return render(request, 'hr/add_vacancy.html', {'message': messages})


class VacancyApplication(TemplateView):
    template_name = 'hr/view_application.html'

    def get_context_data(self, **kwargs):
        context = super(VacancyApplication,self).get_context_data(**kwargs)
        user = HR_Reg.objects.get(user=self.request.user.id)
        post = Apply_Vacancy.objects.filter(vacancy__hr=user, status='Apply')
        context['post'] = post
        return context


class DownloadFile(View):
    def dispatch(self, request, *args, **kwargs):
        path = request.GET['path']
        download(request,path)
        return redirect('/kr/view_application.html')


class AddInterview(TemplateView):
    template_name = 'hr/interview.html'

    def get_context_data(self, **kwargs):
        context = super(AddInterview,self).get_context_data(**kwargs)
        id = self.request.GET['id']
        post = Apply_Vacancy.objects.get(pk=id)
        context['post'] = post
        return context

    def post(self, request,*args,**kwargs):

        place = request.POST['place']
        date = request.POST['date']
        time = request.POST['time']
        vacan = request.POST['vacancy']
        apply = Apply_Vacancy.objects.get(pk=vacan)

        add = Interview()
        add.apply = apply
        add.place = place
        add.date = date
        add.time = time
        add.status = 'Interview'
        add.save()
        app = Apply_Vacancy.objects.get(pk=vacan)
        app.status = 'Interview'
        app.save()
        messages = "Successfully Call For Interview"
        return render(request, 'hr/interview.html', {'message': messages})


class AcceptApplication(TemplateView):
    template_name = 'hr/accept_application.html'

    def get_context_data(self, **kwargs):
        context = super(AcceptApplication,self).get_context_data(**kwargs)
        id = self.request.GET['id']
        post = Apply_Vacancy.objects.get(pk=id)
        context['post'] = post
        return context

    def post(self, request,*args,**kwargs):

        des = request.POST['desc']
        latt = request.FILES['letter']
        vacan = request.POST['vacancy']
        apply = Apply_Vacancy.objects.get(pk=vacan)
        user = apply.user
        print(user)
        accept = Accept_App.objects.filter(vacancy__user=user, status='Add As Employee').count()
        if accept >0:
            accept.status = 'Add As Employee'
            accept.save()
            messages = "Cant sent offer letter he is already a employee!!!."
            return render(request, 'hr/view_application.html', {'message': messages})
        else:
           add = Accept_App()
           add.desc = des
           add.letter = latt
           add.vacancy = apply
           add.status = 'Sent Offer'
           add.save()
           ints = Interview.objects.get(apply=vacan)
           ints.status = 'Sent Offer'
           ints.save()
           app = Apply_Vacancy.objects.get(pk=vacan)
           app.status = 'Job Accept'
           va = app.vacancy.vacancy
           vaid = app.vacancy.id
           total = int(va)-1
           app.save()
           vac =Vacancy.objects.get(pk=vaid)
           if total==0:
             vac.vacancy = total
             vac.status = 'Vacancy Confirmed'
             vac.save()
             messages = "Vacancy Completely Filled"
             return render(request, 'hr/view_application.html', {'message': messages})
           else:
             vac.vacancy = total
             vac.save()
        messages = "One Application Is Accepted."
        return render(request, 'hr/view_application.html', {'message': messages})


class Declined(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        declined = Apply_Vacancy.objects.get(pk=id)
        declined.status = 'Declined'
        declined.save()
        return redirect('/hr/view_application.html')


class InterviewView(TemplateView):
    template_name = 'hr/interview_view.html'

    def get_context_data(self, **kwargs):
        context = super(InterviewView,self).get_context_data(**kwargs)
        user = HR_Reg.objects.get(user=self.request.user.id)
        inter = Interview.objects.filter(apply__vacancy__hr=user, apply__status='Interview')
        context['inter'] = inter
        return context


class OfferLetter(TemplateView):
    template_name = 'hr/offer_letter_sent.html'

    def get_context_data(self, **kwargs):
        context = super(OfferLetter,self).get_context_data(**kwargs)
        user = HR_Reg.objects.get(user=self.request.user.id)
        offer = Accept_App.objects.filter(vacancy__vacancy__hr=user, status='Sent Offer')
        context['offer'] = offer
        return context


class VacancyFilled(TemplateView):
    template_name = 'hr/vacancy_filled.html'

    def get_context_data(self, **kwargs):
        context = super(VacancyFilled,self).get_context_data(**kwargs)
        user = HR_Reg.objects.get(user=self.request.user.id)
        offer = Accept_App.objects.filter(vacancy__vacancy__hr=user, vacancy__vacancy__status='Vacancy Confirmed')
        context['offer'] = offer
        return context


class AddEmployee(TemplateView):
     template_name = 'hr/add_employee.html'

     def get_context_data(self, **kwargs):
         context = super(AddEmployee, self).get_context_data(**kwargs)
         id = self.request.GET['id']
         offer = Accept_App.objects.get(pk=id)
         context['offer'] = offer
         return context

     def post(self, request, *args, **kwargs):
         fullname = request.POST['name']
         emailid = request.POST['emailid']
         username = request.POST['username']
         password = request.POST['password']
         ac = request.POST['acc']
         presentadd = request.POST['presentadd']
         empid = request.POST['emid']
         faname = request.POST['fname']
         mobile = request.POST['cont']
         DOB = request.POST['dob']
         sex = request.POST['gen']
         religion = request.POST['rel']
         blood = request.POST['blood']
         married = request.POST['mari']
         nation = request.POST['national']
         peradd = request.POST['paddress']
         moderec = request.POST['mrecruit']
         joindate = request.POST['datejoin']
         depat = request.POST['depart']
         boss = request.POST['rboss']
         basalary = request.POST['bsalary']
         image = request.FILES['photo']


         user = User.objects.create_user(username=username, password=password, first_name=fullname, email=emailid,
                                             last_name=1)
         user.save()
         reg = Employee()
         reg.user = user
         accept = Accept_App.objects.get(pk=ac)
         reg.accept = accept
         reg.empid = empid
         reg.presentadd = presentadd
         reg.fname = faname
         reg.dob = DOB
         reg.mob = mobile
         reg.gender = sex
         reg.religion = religion
         reg.bloodgroup = blood
         reg.maritalstatus = married
         reg.nationality = nation
         reg.permanentadd = peradd
         reg.moderecuirt = moderec
         reg.dateofjoin = joindate
         reg.department = depat
         reg.reportingboss = boss
         reg.basicsalary = basalary
         reg.photo = image

         reg.save()
         usertype = UserType()
         usertype.user = user
         usertype.type = "employee"
         usertype.save()
         f = Accept_App.objects.get(pk=ac)
         f.status = 'Add As Employee'
         f.save()
         messages = "Save Successfully"
         return render(request, 'hr/add_employee.html', {'message': messages})


class MyEmployee(TemplateView):
    template_name = 'hr/my_employees.html'

    def get_context_data(self, **kwargs):
        context = super(MyEmployee,self).get_context_data(**kwargs)
        user = self.request.user.id
        post = Employee.objects.filter(accept__vacancy__vacancy__hr__user=user, accept__status='Add As Employee')
        context['post'] = post
        return context


class EmployeeEdit(TemplateView):
    template_name = 'hr/edit_employee.html'

    def post(self,request,*args,**kwargs):
        id = self.request.GET['id']
        employee = Employee.objects.get(pk=id)
        if request.POST['profile'] == "profile":

            employee.empid = request.POST['id']
            employee.department = request.POST['depart']
            employee.save()
            return render(request,'hr/edit_employee.html',{'message':"Employee Profile Updated"})
        else:
            employee.basicsalary = request.POST['salary']
            employee.save()
            return render(request,'hr/edit_employee.html',{'message':"Salary Updated"})


class ViewLeave(TemplateView):
   template_name = 'hr/leave_view.html'

   def get_context_data(self, **kwargs):
       context = super(ViewLeave, self).get_context_data(**kwargs)
       user = self.request.user.id
       post = Leave.objects.filter(employee__accept__vacancy__vacancy__hr__user=user, status='Apply')
       context['post'] = post
       return context


class AcceptLeave(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        accept = Leave.objects.get(pk=id)
        accept.status = 'Accept'
        accept.save()
        return redirect('/hr/view_leave')


class RejectLeave(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        reject = Apply_Vacancy.objects.get(pk=id)
        reject.status = 'Reject'
        reject.save()
        return redirect('/hr/view_leave')


class EmployeeAttendance(TemplateView):
    template_name = 'hr/add_attendence.html'

    def get_context_data(self, **kwargs):
        context =  super(EmployeeAttendance, self).get_context_data(**kwargs)
        user = self.request.user.id
        emp = Employee.objects.filter(accept__vacancy__vacancy__hr__user=user)
        context['empl'] = emp
        lea = Leave.objects.filter(employee__accept__vacancy__vacancy__hr__user=user, status='Accept')
        context['leave'] = lea
        return context

    def post(self, request, *args, **kwargs):
        cdate = request.POST['date']
        empid = request.POST['emplo']
        now = request.POST['stat']
        user = self.request.user.id
        users = HR_Reg.objects.get(user=user)

        empo = Employee.objects.get(pk=empid)

        add = EmpAttandance()
        add.employee = empo
        add.hr = users
        add.date = cdate
        add.status = now
        add.save()
        messages = "Add Attendance Successfully"
        return render(request, 'hr/add_attendence.html', {'message': messages})


class AllocateWork(TemplateView):
    template_name = 'hr/allocate_work.html'

    def get_context_data(self, **kwargs):
        context =  super(AllocateWork, self).get_context_data(**kwargs)
        user = self.request.user.id
        emp = Employee.objects.filter(accept__vacancy__vacancy__hr__user=user)
        context['empl'] = emp
        return context

    def post(self, request, *args, **kwargs):
        descri = request.POST['desc']
        cdate = request.POST['date']
        empid = request.POST['emplo']
        photo = request.FILES['image']
        user = self.request.user.id
        users = HR_Reg.objects.get(user=user)

        employee = Employee.objects.get(pk=empid)

        add = AddWork()
        add.employee = employee
        add.date = cdate
        add.hr = users
        add.description = descri
        add.photo = photo
        add.status = 'Allocate'
        add.save()
        messages = "Work Allocated Successfully"
        return render(request, 'hr/allocate_work.html', {'message': messages})


class ViewWorkStatus(TemplateView):
    template_name = 'hr/view_work_status.html'

    def get_context_data(self, **kwargs):
        context =  super(ViewWorkStatus, self).get_context_data(**kwargs)
        user = self.request.user.id
        emp = AddWorkStatus.objects.filter(addwork__hr__user=user)
        context['empl'] = emp
        return context


class MYWorkAllocate(TemplateView):
    template_name = 'hr/my_work_allocation.html'

    def get_context_data(self, **kwargs):
        context =  super(MYWorkAllocate, self).get_context_data(**kwargs)
        user = self.request.user.id
        emp = AddWork.objects.filter(hr__user=user)
        context['empl'] = emp
        return context


class EmployeeSalary(TemplateView):
    template_name = 'hr/salary_structure.html'

    def get_context_data(self, **kwargs):
        context =  super(EmployeeSalary, self).get_context_data(**kwargs)
        user = self.request.user.id
        emp = Employee.objects.filter(accept__vacancy__vacancy__hr__user=user)
        context['empl'] = emp
        return context


class LeaveDetails(TemplateView):
    template_name = 'hr/leave_detatils.html'

    def get_context_data(self, **kwargs):
        context =  super(LeaveDetails, self).get_context_data(**kwargs)
        user = self.request.user.id
        lea = Leave.objects.filter(employee__accept__vacancy__vacancy__hr__user=user)
        context['leave'] = lea
        return context


class AttendanceDetails(TemplateView):
    template_name = 'hr/attendance_details.html'

    def get_context_data(self, **kwargs):
        context =  super(AttendanceDetails, self).get_context_data(**kwargs)
        user = self.request.user.id
        lea = EmpAttandance.objects.filter(hr__user=user)
        context['atten'] = lea
        return context


class EmpAttendance(TemplateView):
    template_name = 'hr/attendance_report.html'

    def get_context_data(self, **kwargs):
        context = super(EmpAttendance,self).get_context_data(**kwargs)
        user = self.request.user.id
        post = Employee.objects.filter(accept__vacancy__vacancy__hr__user=user, accept__status='Add As Employee')
        context['post'] = post
        return context


class GenerateAttReport(View):
    def dispatch(self, request, *args, **kwargs):
        i = self.request.GET['id']
        abs = Employee.objects.get(pk=i)
        id = abs.id
        present = EmpAttandance.objects.filter(employee_id=id, status='Present').count()
        absent = EmpAttandance.objects.filter(employee_id=id, status='Absent').count()
        print(present)
        print(absent)
        ass = AttReport()
        ass.present = present
        ass.absent = absent
        ass.employee = abs
        ass.gdate = date.today()
        ass.save()
        messages = "Generated Attendance Report Successfully"
        return render(request, 'hr/attendance_report.html', {'message': messages})


class HRReport(TemplateView):

    def dispatch(self, request, *args, **kwargs):
        user = self.request.user.id
        empo = Employee.objects.filter(accept__vacancy__vacancy__hr__user=user, accept__status='Add As Employee').count()
        work = AddWork.objects.filter(hr__user=user).count()
        report = HrReport.objects.filter(hr__user=user).count()
        if report>0:
            report = HrReport.objects.get(hr__user=user)

            report.noemployee = int(empo)
            report.noworks = int(work)
            report.date = date.today()
            report.save()
        else:
          rep = HrReport()
          rep.noemployee = empo
          rep.noworks = work
          rep.date = date.today()
          users = HR_Reg.objects.get(user=user)
          rep.hr = users
          rep.save()
        messages = "Generated HR Report Successfully"
        return render(request, 'hr/attendance_report.html', {'message': messages})




