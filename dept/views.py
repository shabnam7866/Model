from django.shortcuts import render
from dept.models import *

# Create your views here.
def index(request):
    department=Department.objects.all()
    print("department: ", department)
    return render(request,'index.html',{"department":department})


def emp(request):
    employee=Employee.objects.all()
    print("employee: ", employee)
    return render(request,'emp.html',{"employee":employee})

def product(request):
    product=Product.objects.all()
    print("prod: ", product)
    return render(request,'product.html',{"product":product})
