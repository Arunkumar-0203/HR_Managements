from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserType(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)


class Applicant_Reg(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=100)
    address = models.CharField(max_length=100)


class HR_Reg(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    code = models.CharField(max_length=100)


class Vacancy(models.Model):
    hr = models.ForeignKey(HR_Reg, on_delete=models.CASCADE)
    vacancy = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    status = models.CharField(max_length=100, null=True)


class Apply_Vacancy(models.Model):
    user = models.ForeignKey(Applicant_Reg, on_delete=models.CASCADE)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    cv = models.ImageField(upload_to='images/')
    status = models.CharField(max_length=100)


class Interview(models.Model):
    apply = models.ForeignKey(Apply_Vacancy, on_delete=models.CASCADE)
    place = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    status = models.CharField(max_length=100, null=True)


class Accept_App(models.Model):
    vacancy = models.ForeignKey(Apply_Vacancy, on_delete=models.CASCADE)
    desc = models.CharField(max_length=100)
    letter = models.ImageField(upload_to='images/')
    status = models.CharField(max_length=100, null=True)


class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    accept = models.ForeignKey(Accept_App, on_delete=models.CASCADE)
    empid = models.CharField(max_length=100)
    fname = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    religion = models.CharField(max_length=100)
    bloodgroup = models.CharField(max_length=100)
    maritalstatus = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    mob = models.CharField(max_length=100)
    presentadd = models.CharField(max_length=100)
    permanentadd = models.CharField(max_length=100)
    moderecuirt = models.CharField(max_length=100)
    dateofjoin = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    reportingboss = models.CharField(max_length=100)
    basicsalary = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images/', null=True)


class Leave(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leavetype = models.CharField(max_length=100)
    fromdate = models.CharField(max_length=100)
    noday = models.CharField(max_length=100)
    enddate = models.CharField(max_length=100)
    leaveperiod = models.CharField(max_length=100)
    reason = models.CharField(max_length=100)
    status = models.CharField(max_length=100, null=True)


class EmpAttandance(models.Model):
    hr = models.ForeignKey(HR_Reg, on_delete=models.CASCADE, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    status = models.CharField(max_length=100)


class AddWork(models.Model):
    hr = models.ForeignKey(HR_Reg, on_delete=models.CASCADE, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images/', null=True)
    status = models.CharField(max_length=100, null=True)


class AddWorkStatus(models.Model):
    addwork = models.ForeignKey(AddWork, on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images/')
    status = models.CharField(max_length=100)


class AttReport(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    present = models.CharField(max_length=100)
    absent = models.CharField(max_length=100)
    gdate = models.CharField(max_length=100, null=True)


class HrReport(models.Model):
    hr = models.ForeignKey(HR_Reg, on_delete=models.CASCADE, null=True)
    noemployee = models.CharField(max_length=100)
    noworks = models.CharField(max_length=100)
    date = models.CharField(max_length=100, null=True)


