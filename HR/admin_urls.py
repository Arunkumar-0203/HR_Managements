from django.urls import path

from HR.admin_views import IndexView, ApproveView, RejectView, NewHRView, NewApplicantView, HR_ManagerView, \
    ApplicantView, MyEmployee, HRReport, DetailsEmployee, WorkDetails

urlpatterns = [

    path('',IndexView.as_view()),
    path('new_HR_view', NewHRView.as_view()),
    path('new_applicant_view', NewApplicantView.as_view()),
    path('approve', ApproveView.as_view()),
    path('reject', RejectView.as_view()),
    path('HR_manager_view', HR_ManagerView.as_view()),
    path('applicant_view', ApplicantView.as_view()),
    path('my_employee', MyEmployee.as_view()),
    path('hr_report', HRReport.as_view()),
    path('details_employee', DetailsEmployee.as_view()),
    path('work_details', WorkDetails.as_view()),

]
def urls():
      return urlpatterns,'admin','admin'