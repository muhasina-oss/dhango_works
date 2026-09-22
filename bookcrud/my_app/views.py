from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from my_app.models import Books
from json import loads
# Create your views here.
@method_decorator(csrf_exempt,name="dispatch")
class BookCreateListView(View):
  
  def get(self,request):
    
    qs = Books.objects.all().values()
    
    book = list(qs)
    
    return JsonResponse(book,safe=False)
  
  def post(self,request):
    
    form_data = loads(request.body)
    
    Books.objects.create(
      title = form_data.get("title"),
      author = form_data.get("author"),
      price = form_data.get("price"),
      pages = form_data.get("pages"),
      publications = form_data.get("publications"),
    )
    
    respose_data = {"message":"book created..."}
    
    return JsonResponse(respose_data)
  
@method_decorator(csrf_exempt,name="dispatch")
class BooksRetrieveUpdateDeleteView(View):
  
  def get(self,request,pk=None):
    
    qs = Books.objects.filter(id=pk).values()
    
    book = list(qs)
    
    return JsonResponse(book,safe=False)
  
  def delete(self,request,pk=None):
    
    Books.objects.filter(id=pk).delete()
    
    response_data = {"message":"book deleted..."}
    
    return JsonResponse(response_data)
  
  
  