from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
# Create your views here.
class AboutView(View):
  
  def get(self,request):
    
    response_data = {
      "id": 1,
      "full_name": "Muhasina PH",
      "title": "Software Developer & Educator",
      "bio": "A passionate developer and researcher building scalable applications...",
      "email": "hussinmuhasina@gmail.com",
      "github_url": "https://github.com/muhasina",
      "linkedin_url": "https://linkedin.com/in/muhasina",
      "resume_download_url": "https://api.google.com/media/resume.pdf"
      }
    return JsonResponse(response_data)
  
class EducationView(View):
  
  def get(self,request):
    
    response_data = [
        {
          "id": 1,
          "institution": "MG University",
          "degree": "Bvoc Software Development and system administration",
          "start_date": "2023-08-01",
          "end_date": "2026-05-01",
          "grade_or_cgpa": "8.33",
          "description": "Focused on software engineering and data structures."
        }
      ]
    return JsonResponse(response_data,safe=False)

class ProjectView(View):
  
  def get(self,request):
    
    response_data =[
                        {
                          "id": 1,
                          "title": "DietLense",
                          "short_description": "AI-powered food recognition and nutritional analysis app.",
                          "long_description": "Built using Gemini models to analyze nutritional data from images...",
                          "technologies_used": ["Python", "Django", "Google GenAI SDK"],
                          "live_url": "https://dietlense.example.com",
                          "github_url": "https://github.com/yourusername/dietlense",
                          "image_url": "https://api.yourdomain.com/media/projects/dietlense_cover.jpg",
                          "featured": "true"
                        },
                        {
                          "id": 2,
                          "title": "Interview Prep Blog",
                          "short_description": "Educational application for programming interviews.",
                          "long_description": "A platform for practicing technical interview questions and Python concepts.",
                          "technologies_used": ["Python", "Django REST Framework", "JavaScript"],
                          "live_url": "https://prep.example.com",
                          "github_url": "https://github.com/yourusername/interview-prep",
                          "image_url": "https://api.yourdomain.com/media/projects/prep_cover.jpg",
                          "featured": "False"
                        }
                      ]
    return JsonResponse(response_data,safe=False)
  
class SkillsView(View):
  
  def get(self,request):
    
    response_data = [
        {
          "id": 1,
          "category": "Backend",
          "name": "Django REST Framework",
          "proficiency_percentage": 90,
          "icon_url": "https://api.yourdomain.com/media/icons/drf.png"
        },
        {
          "id": 2,
          "category": "Languages",
          "name": "Python",
          "proficiency_percentage": 95,
          "icon_url": "null"
        },
        {
          "id": 3,
          "category": "Frontend",
          "name": "JavaScript",
          "proficiency_percentage": 85,
          "icon_url": "https://api.yourdomain.com/media/icons/js.png"
        }
      ]
    return JsonResponse(response_data,safe=False)
  
class CertificaionView(View):
  
  def get(self,request):
    
    response_data = [
        {
          "id": 1,
          "name": "Advanced Python & Django Specialization",
          "issuing_organization": "Tech Institute",
          "issue_date": "2024-01-15",
          "expiration_date": "null",
          "credential_id": "CERT-12345",
          "credential_url": "https://certificates.example.com/12345"
        }
      ]
    return JsonResponse(response_data,safe=False)
