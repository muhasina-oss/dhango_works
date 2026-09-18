from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from json import loads

# Create your views here.
@method_decorator(csrf_exempt,name="dispatch")

class AdditionView(View):
  
  def post(self,request):
    
    form_data = loads(request.body)
    
    n1 = int(form_data.get("num1"))
    n2 = int(form_data.get("num2"))
    
    result = n1 +n2
    
    response_data = {
      "message":f"result for adding {n1},{n2} = {result}"
    }
    
    return JsonResponse(response_data)

@method_decorator(csrf_exempt,name="dispatch")  
class SubtractionView(View):
  
  def post(self,request):
    
    form_data = loads(request.body)
    
    n1 = int(form_data.get("num1"))
    n2 = int(form_data.get("num2"))
    
    result = n1-n2
    
    response_data = {
      "message" : f"result for subtraction {n1},{n2} = {result}"
    }
    return JsonResponse(response_data)
  
@method_decorator(csrf_exempt,name="dispatch")  
class MultiplicationView(View):
  
  def post(self,request):
    
    form_data = loads(request.body)
    
    n1 = int(form_data.get("num1"))
    n2 = int(form_data.get("num2")) 
    
    result = n1 * n2
    
    respose_data = {
      "message" : f"multiplication of num1 = {n1},num2  ={n2} = result = {result}"
    }
    
    return JsonResponse(respose_data)

@method_decorator(csrf_exempt,name="dispatch")  
class DivisionView(View):
  
  def post(self,request):
    
    form_data = loads(request.body)
    
    n1 = int(form_data.get("num1"))
    n2 = int(form_data.get("num2"))
    
    result = n1 / n2
    
    response_data = {
      "message ": f"result for division num1 = {n1} num2 = {n2} result = {result}"
    }
    
    return JsonResponse(response_data)
  
  
@method_decorator(csrf_exempt,name="dispatch")
class FactorialView(View):
  
  def post(self,requset):
    
    form_data = loads(self.request.body)
    
    number = int(form_data.get("number"))
    
    result =1
    
    for num in range(1,number+1):
      
      result*=num
      
    response_data = {
      "operation":f"factorial of number {number} = {result}"
      
    }
    
    return JsonResponse(response_data)
  
@method_decorator(csrf_exempt,name="dispatch")
class PrimenumberView(View):
  
  def post(self,request):
    
    form_data = loads(request.body)
    
    number = int(form_data.get("number"))
    
    result = True
    
    for num in range(2,number):
      
      if num%number==0:
        
        result = False
        
        break
      
    else:
      
      result = True
      
    response_data = {
        "operation": "prime_check",
        "number": number,
        "is_prime": result
    }
    return JsonResponse(response_data)
  
@method_decorator(csrf_exempt,name="dispatch")
class PerfectNumberView(View):
  
  def post(self,request):
    
    form_data = loads(request.body)
    
    number = int(form_data.get("number"))
    
    divisors = []
    
    result = 0
    
    for num in range(1,number):
      
      if number%num==0:
        
        divisors.append(num)
            
    result = sum(divisors)
    
    response_data = {
      "operation":"perfect number check",
      "number":number,
      "divisors":divisors,
      "divisors_sum":result  
    }
    
    return JsonResponse(response_data)
