

from django.contrib.auth.models import User
from django.shortcuts import render
from django.template import loader
from django.views.generic import TemplateView

from HR.models import Employee, Leave, AddWork, AddWorkStatus, AttReport, EmpAttandance


class IndexView(TemplateView):
    template_name = 'employee/emp_index.html'


class MyAccount(TemplateView):
    template_name = 'employee/my_account.html'

    def get_context_data(self ,**kwargs):
        context = super(MyAccount,self).get_context_data(**kwargs)
        context['user'] = self.request.user
        if self.request.user.is_active:
            employee = Employee.objects.get(user_id=self.request.user.id)
            context['employee'] = employee
        return context

    def post(self,request,*args,**kwargs):
        user = User.objects.get(id=self.request.user.id)
        employee = Employee.objects.get(user_id=self.request.user.id)
        if request.POST['profile'] == "profile":

            employee.maritalstatus = request.POST['mari']
            employee.mob = request.POST['mobile']
            employee.presentadd = request.POST['paddress']
            employee.save()
            return render(request,'employee/my_account.html',{'message':"Profile Updated"})
        else:
            user.username = request.POST['username']
            user.set_password(request.POST['password'])
            user.save()
            return render(request,'employee/my_account.html',{'message':"Updated Username and Password"})


class ApplyLeave(TemplateView):
     template_name = 'employee/apply_leave.html'

     def post(self, request, *args, **kwargs):
         types = request.POST['type']
         frodate = request.POST['fdate']
         noday = request.POST['nday']
         endd = request.POST['edate']
         period = request.POST['period']
         reason = request.POST['reason']
         employee = Employee.objects.get(user_id=self.request.user.id)

         add = Leave()
         add.employee = employee
         add.leavetype = types
         add.fromdate = frodate
         add.enddate = endd
         add.noday = noday
         add.leaveperiod = period
         add.reason = reason
         add.status = 'Apply'
         add.save()
         messages = "Successfully Applied"
         return render(request, 'employee/apply_leave.html', {'message': messages})


class LeaveAppStatus(TemplateView):
     template_name = 'employee/leave_app_status.html'

     def get_context_data(self, **kwargs):
         context = super(LeaveAppStatus, self).get_context_data(**kwargs)
         user = self.request.user.id
         post = Leave.objects.filter(employee__user=user)
         context['post'] = post
         return context


class MyNewWork(TemplateView):
    template_name = 'employee/new_work_view.html'

    def get_context_data(self, **kwargs):
        context = super(MyNewWork, self).get_context_data(**kwargs)
        user = self.request.user.id
        post = AddWork.objects.filter(employee__user=user)
        context['post'] = post
        return context


class UpdateWorkStatus(TemplateView):
    template_name = 'employee/update_work_status.html'

    def get_context_data(self, **kwargs):
        context = super(UpdateWorkStatus, self).get_context_data(**kwargs)
        id = self.request.GET['id']
        post = AddWork.objects.get(pk=id)
        context['post'] = post
        return context

    def post(self, request, *args, **kwargs):
        descri = request.POST['desc']
        cdate = request.POST['date']
        empid = request.POST['emp']
        photo = request.FILES['image']
        print(empid)

        joballo = AddWorkStatus.objects.filter(addwork=empid).count()

        if joballo>0:
            joballo.photo = photo
            joballo.date = cdate
            joballo.description = descri
            joballo.save()
        else:
           add = AddWorkStatus()
           employee = AddWork.objects.get(pk=empid)
           add.addwork = employee
           add.date = cdate
           add.description = descri
           add.photo = photo
           add.status = 'Updated'
           add.save()
        messages = "Work Status Updated Successfully"
        return render(request, 'employee/update_work_status.html', {'message': messages})


class AttendanceReport(TemplateView):
    template_name = 'employee/view_attendance_report.html'

    def get_context_data(self, **kwargs):
        context = super(AttendanceReport, self).get_context_data(**kwargs)
        user = self.request.user.id
        post = AttReport.objects.filter(employee__user=user)
        context['post'] = post
        return context

    def post(self, request, *args, **kwargs):
        # template = loader.get_template('employee/view_attendance_report.html')
        user = self.request.user.id
        if request.method=='POST':
          search = self.request.POST['srh']
          if search:
                match = AttReport.objects.filter(gdate=search, employee__user=user).count()
                if match>0:
                    match = AttReport.objects.get(gdate=search, employee__user=user)
                    return render(request,'employee/view_attendance_report.html', {'post': match})
                else:
                   messages = "There Is No Date of Attendance Submit"
                   return render(request, 'employee/view_attendance_report.html', {'message': messages})
          else:
              messages = "There Is No Date of Attendance Submit"
              return render(request, 'employee/view_attendance_report.html', {'message': messages})
        else:
            messages = "Please Enter Any Value"
            return render(request, 'employee/view_attendance_report.html', {'message': messages})



class AttendanceDetails(TemplateView):
    template_name = 'employee/attendance_details.html'

    def get_context_data(self, **kwargs):
        context = super(AttendanceDetails, self).get_context_data(**kwargs)
        user = self.request.user.id
        post = EmpAttandance.objects.filter(employee__user=user)
        context['post'] = post
        return context