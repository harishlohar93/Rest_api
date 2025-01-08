from django.contrib import admin
from .models import Company, Employee
# Register your models here.


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['company_id', 'name', 'location', 'about', 'type', 'added_date', 'active']
    list_filter = ['company_id', 'name', 'location', 'type', 'added_date', 'active']
    search_fields = ['company_id', 'name', 'location', 'type', 'added_date', 'active']
    list_per_page = 10
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['employee_id', 'company_id', 'name', 'email', 'phone', 'about', 'position', 'added_date', 'active']
    list_filter = ['employee_id', 'company_id', 'name', 'email', 'phone', 'position', 'added_date', 'active']
    search_fields = ['employee_id', 'company_id', 'name', 'email', 'phone', 'position', 'added_date', 'active']
    list_per_page = 10
admin.site.register(Company , CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)