from django.shortcuts import render
from ganeshapp.models import Employee
# Create your views here.
def emp_view(request):
    emp=Employee.objects.all()
    print(emp)
    return render(request,'ganeshapp/index.html',{'emp':emp})