from django.urls import path

from HR.hr_views import IndexView, AddVacancy, VacancyApplication, DownloadFile, AddInterview, AcceptApplication, \
    InterviewView, OfferLetter, VacancyFilled, AddEmployee, Declined, MyEmployee, EmployeeEdit, ViewLeave, AcceptLeave, \
    RejectLeave, EmployeeAttendance, AllocateWork, ViewWorkStatus, MYWorkAllocate, EmployeeSalary, LeaveDetails, \
    AttendanceDetails, EmpAttendance, GenerateAttReport, HRReport

urlpatterns = [

    path('',IndexView.as_view()),
    path('add_vacancy', AddVacancy.as_view()),
    path('vacancy_application', VacancyApplication.as_view()),
    path('download', DownloadFile.as_view()),
    path('interview', AddInterview.as_view()),
    path('accept_application', AcceptApplication.as_view()),
    path('interview_view', InterviewView.as_view()),
    path('offer_letter', OfferLetter.as_view()),
    path('vacancy_filled', VacancyFilled.as_view()),
    path('add_employee', AddEmployee.as_view()),
    path('declined', Declined.as_view()),
    path('my_employee', MyEmployee.as_view()),
    path('employee_edit', EmployeeEdit.as_view()),
    path('view_leave', ViewLeave.as_view()),
    path('accept_leave', AcceptLeave.as_view()),
    path('reject_leave', RejectLeave.as_view()),
    path('employee_attendance', EmployeeAttendance.as_view()),
    path('allocate_work', AllocateWork.as_view()),
    path('view_work_status', ViewWorkStatus.as_view()),
    path('my_work_allocate', MYWorkAllocate.as_view()),
    path('employee_salary', EmployeeSalary.as_view()),
    path('leave_details', LeaveDetails.as_view()),
    path('attendance_details', AttendanceDetails.as_view()),
    path('emp_attendance', EmpAttendance.as_view()),
    path('generate_att_report', GenerateAttReport.as_view()),
    path('hr_report', HRReport.as_view()),

]
def urls():
      return urlpatterns,'hr', 'hr'