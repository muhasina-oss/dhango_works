from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
# Create your views here.

class HelloWorldView(View):
  
  def get(self,request):
    
    response_data = {"message":"hello world"}
    return JsonResponse(response_data)
  
class GoodMorningView(View):
  
  def get(self,request):
    
    response_data = {"message":"Good Morning"}
    return JsonResponse(response_data)
  
class GoodAtferNoonView(View):
  
  def get(self,request):
    response_data = {"message":"Good After Noon"}
    return JsonResponse(response_data)
  
class GoodEvening(View):
  
  def get(self,request):
    
    response_data = {"message":"Good Evening"}
    
    return JsonResponse(response_data)
  
class GoodNight(View):
  
  def get(self,request):
    
    response_data = {"message":"Good Night"}
    
    return JsonResponse(response_data)