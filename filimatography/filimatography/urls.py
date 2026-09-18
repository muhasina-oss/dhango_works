"""
URL configuration for filimatography project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from biography.views import MohanlalView,MammoottyView,DileepView,JayaramMovieView,AsifAliMovieView
from biography.views import FahadFasilMovie,NivinPaulyMovie,KunchakoBobanMovieView,JayasuryaView
from biography.views import VijayView,YashView,PrabhudevaView,PrithviRajView,SharukhKhanView,MamithaBaijuView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mohanlal/',MohanlalView.as_view()),
    path('mammootty/',MammoottyView.as_view()),
    path('dileep/',DileepView.as_view()),
    path('jayaram/',JayaramMovieView.as_view()),
    path('asifali/',AsifAliMovieView.as_view()),
    path('fahadfasil/',FahadFasilMovie.as_view()),
    path('nivinpauly/',NivinPaulyMovie.as_view()),
    path('kunchakoboban/',KunchakoBobanMovieView.as_view()),
    path('jayasurya/',JayasuryaView.as_view()),
    path('vijay/',VijayView.as_view()),
    path('yash/',YashView.as_view()),
    path('prabhudeva/',PrabhudevaView.as_view()),
    path('prithwiraj/',PrithviRajView.as_view()),
    path('sharukh/',SharukhKhanView.as_view()),
    path('mamithabaiju/',MamithaBaijuView.as_view())
]
