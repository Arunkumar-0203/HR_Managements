from django.urls import path

from HR.applicant_views import IndexView, VacancyView, ApplyVacancy, InterviewCall, AcceptAppli, EmployeeDetails

urlpatterns = [

    path('',IndexView.as_view()),
    path('vacancy_view', VacancyView.as_view()),
    path('apply_vacancy', ApplyVacancy.as_view()),
    path('interview_call', InterviewCall.as_view()),
    path('accept_appli', AcceptAppli.as_view()),
    path('employee_details', EmployeeDetails.as_view()),

]
def urls():
      return urlpatterns,'applicants','applicants'