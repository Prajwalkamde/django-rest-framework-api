from django.db import models

# Create your models here.
company_type = (
    ('IT', 'IT'),
    ('Non IT', 'Non IT')
)

position_choice = (
    ('Web Developer', 'Web Developer'),
    ('Android Developer', 'Android Developer'),
    ('Frontend Developer', 'Frontend Developer'),
    ('Backend Developer', 'Backend Developer'),
)




class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    company_type = models.CharField(max_length=50, choices=company_type)
    location = models.CharField(max_length=100)
    about = models.TextField()
    size = models.IntegerField()
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    employee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    phone = models.IntegerField()
    address = models.CharField(max_length=200)
    position = models.CharField(max_length=50, choices=position_choice)

    def __str__(self):
        return self.name