from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
# Create your views here.
class MohanlalView(View):
  
  def get(self,request):
    
    response_data = {
      "name":"Mohan lal",
      "Language":"Malayalam",
      "age":65,
      "Filims": 670
    }
    
    return JsonResponse(response_data)

class MammoottyView(View):
  
  def get(sel,request):
    
    response_data =  {
      "name":"Mammootty",
      "Language":"Malayalam",
      "age":70,
      "Filims": 590
    }
    return JsonResponse(response_data)
  
class DileepView(View):
  
  def get(self,request):
    
    response_data = {
      "name":"Dileep",
      "Language":"Malayalam",
      "age":55,
      "filims":300
    }
    return JsonResponse(response_data)
  
class JayaramMovieView(View):
  
  def get(self,request):
    
    response_data ={
      "name":"Jayaram", 
      "Language":"Malayalam", 
      "age":57, 
      "films":370
    }
    
    return JsonResponse(response_data)
  
class AsifAliMovieView(View):
  
  def get(self,request):
    
    response_data = {
      "name":"Asif Ali",
      "language":"Malayalam",
      "age":38,
      "filims":250
    }
    
    return JsonResponse(response_data)
  
class FahadFasilMovie(View):
  
  def get(self,request):
    
    response_data = {
      "name":"Fahad Fasil",
      "language":"Malayalam",
      "age":40,
      "filims":270      
    }
    
    return JsonResponse(response_data)
  
class KunchakoBobanMovieView(View):
  
  def get(self,request):
    
    response_data = {
      "name":"Kunchako Boban",
      "language":"Malayalam",
      "age":47,
      "filims":350      
    }  
    
    return JsonResponse(response_data)
  
  
class NivinPaulyMovie(View):
  
  def get(Self,request):
    
    response_data = {
      "name":"Nivin Pauly",
      "language":"Malayalam",
      "age":42,
      "filims":290      
    }
    return JsonResponse(response_data)

class JayasuryaView(View):
  
  def get(self,request):
    
    response_data = {
      "name":"Jayasurya",
      "language":"Malayalam",
      "age":43,
      "filims":340      
    }
    return JsonResponse(response_data)
  
class VijayView(View):
  
  def get(self,request):
    
    response_data = {
      "name":"Vijay",
      "language":"Tamil",
      "age":58,
      "filims":500      
    }  
    return JsonResponse(response_data)
  
class YashView(View):
  
  def get(self,request):
    
    response_data = {
      "name":"Yash",
      "language":"Kannada",
      "age":35,
      "filims":150     
    }  
    
    return JsonResponse(response_data)
  
class PrabhudevaView(View):
  
  def get(self,request):
    
    response_data = {
      "name":"Prabhudeva",
      "language":"Tamil",
      "age":46,
      "filims":105   
    }
    return JsonResponse(response_data)
  
class PrithviRajView(View):
  
  def get(self,request):
    
    response_data = {
      "name":"Prithvi Raj",
      "language":"Malayalam",
      "age":46,
      "filims":350    
    }
    return JsonResponse(response_data)
  
class SharukhKhanView(View):
  
  def get(self,request):
    
    response_data = {
      "name":"Sharukh Khan",
      "language":"Hindi",
      "age":60,
      "filims":550     
    }
    return JsonResponse(response_data)
  
class MamithaBaijuView(View):
  
  def get(self,request):
    
    response_data = {
      "name":"Mamitha Baiju",
      "language":"Malayalam",
      "age":24,
      "filims":60      
    }
    return JsonResponse(response_data)