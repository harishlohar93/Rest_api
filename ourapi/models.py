from django.db import models 

# Create your models here.

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    about = models.TextField()
    type = models.CharField(choices=[('MNC', 'Multi National Company'), ('SME', 'Small Medium Enterprise'), ('Startup', 'Startup')], max_length=100)
    added_date = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True, null=True)
    


    
    def __str__(self):
        return self.name

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    about = models.CharField(max_length=100)
    position = models.CharField(max_length=100 , choices=[('HR', 'Human Resource'), ('TL', 'Team Leader'), ('DEV', 'Developer'), ('QA', 'Quality Analyst'), ('PM', 'Project Manager')])
    added_date = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True, null=True)
    
    def __str__(self):
        return self.name


