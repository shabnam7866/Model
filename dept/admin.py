from django.contrib import admin
from.models import Department,Employee,Adhar,Product
# Register your models here.

admin.site.register(Department)
# class DepartmentAdmin(admin.ModelAdmin):
#     list_display=['D_id','D_name']

admin.site.register(Employee)
# class EmployeeAdmin(admin.ModelAdmin):
#     list_display=['E_name','E_dept','email','Adhar',]
    
admin.site.register(Adhar)
# class AdharAdmin(admin.ModelAdmin):
#     list_display=['number']
    
admin.site.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display=['price']
