from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from crm.models import Employee
from json import loads
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@method_decorator(csrf_exempt,name="dispatch")
class EmployeeListCreateView(View):
  
  def get(self,request):
    
    qs = Employee.objects.all().values()
    
    employees = list(qs)
    
    print(employees)
    
    return JsonResponse(employees,safe=False)
  
  def post(self,request):
    
    form_data = loads(request.body)
      
    Employee.objects.create(
      
      name=form_data.get("name"),
      department=form_data.get("department"),
      salary=form_data.get("salary"),
      location=form_data.get("location"),
      email=form_data.get("email"),
    )
    
    response_data = {"message":"employee created.."}
    
    return JsonResponse(response_data)
  
class EmployeeRetrieveUpdateDeleteView(View):
  
  def get(self,request,pk=None):
    
    qs = Employee.objects.filter(id=pk).values()
    
    employee = list(qs)
    
    return JsonResponse(employee,safe=False)