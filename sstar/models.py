from django.db import models
from ckeditor.fields import RichTextField
from django.db.models import ForeignKey
from djmoney.models. fields import MoneyField
from django.contrib.auth.models import User
import datetime


# Create your models here.

DepartmentList = (
    ('Human Resource', 'Human Resource'),
    ('Sales', 'Sales'),
    ('Marketing', 'Marketing'),
)

role = (
    ('Manager', 'Manager'),
    ('Cashier', 'Cashier'),
    ('Admin', 'Admin'),

)

resident = (
    ('Africa', 'Africa'),
    ('Europe', 'Europe'),
    ('Asia', 'Asia'),
    ('America', 'America'),

)

class Department(models.Model):
    Department = models.CharField(max_length=200, primary_key=True, choices=DepartmentList)

    def __str__(self):
        return self.Department



class Employee(models.Model):
    full_name = models.CharField(max_length=200)
    role = models.CharField(max_length=200, choices=role)
    email = models.CharField(max_length=200, primary_key=True)
    Department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name


class Announcements(models.Model):
    logo = models.ImageField(upload_to='Announcements/')
    headline = models.CharField(max_length=200)
    date_registered = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.headline

class Customer(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, primary_key=True)
    resident = models.CharField(max_length=15, choices=resident)
    national_id = models.IntegerField()
    date_registered = models.DateField(auto_now_add=True)
    insurance_duration = models.DateTimeField(auto_now_add=False)
    business_type = models.CharField(max_length=200)
    about = RichTextField(blank=True, null=True)
    license = models.FileField(upload_to='License/')

    def __str__(self):
        return self.name

class Compansation(models.Model):
    amount = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    registered_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.amount


class MonthlyInstallment(models.Model):
    amount = MoneyField(max_digits=14, decimal_places=2, default_currency='dollars')
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    registered_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.amount

class TabHeader(models.Model):
    button_name = models.CharField(max_length=200)

    def __str__(self):
        return self.button_name





class Tab(models.Model):
    button_name = models.ForeignKey(TabHeader, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Tabs/')
    description = RichTextField(blank=True, null=True)

    def __str__(self):
        return str(self.button_name)

# Categories of Insurance
class Category(models.Model):
    name = models.CharField(max_length= 100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Insurance(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='Insurance/')

    def __str__(self):
        return self.name



