from django.contrib import admin
from .models import Company,Employee
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'company')
    search_fields = ('name',)
    list_filter = ('company',)

admin.site.register(Company)
admin.site.register(Employee,EmployeeAdmin)
