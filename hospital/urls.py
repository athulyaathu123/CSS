"""
URL configuration for hospital project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from doctor.views import first_request
from doctor.views import second_request,demo
from account.views import home,Logview
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first',first_request),
    path('second',second_request),
    path('demo',demo),
    path('home',home,name="home"),
    path('acc/',include("account.urls")),
    path('doc/',include("doctor.urls")),
    path('',Logview.as_view(),name="login")
    
   
    
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
