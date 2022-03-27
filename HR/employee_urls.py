from django.urls import path

from HR.employee_views import IndexView, MyAccount, ApplyLeave, LeaveAppStatus, MyNewWork, UpdateWorkStatus, \
    AttendanceReport, AttendanceDetails

urlpatterns = [

    path('',IndexView.as_view()),
    path('my_account', MyAccount.as_view()),
    path('apply_leave', ApplyLeave.as_view()),
    path('leave_app_status', LeaveAppStatus.as_view()),
    path('my_new_work', MyNewWork.as_view()),
    path('update_work_status', UpdateWorkStatus.as_view()),
    path('attendance_report', AttendanceReport.as_view()),
    path('attendance_details', AttendanceDetails.as_view()),

]
def urls():
      return urlpatterns,'employee', 'employee'