from django.urls import path
from .views import *


urlpatterns = [
    path('register',RegisterView.as_view(),name='rg'),
    # path('login',Log.as_view(),name='lg'),

    path('add',add,name='add'),
    path('count',count,name='count'),
    path('addman',Addmanager.as_view(),name='addman'),
    path('viewmanager',Viewmanger.as_view(),name='managerview'),
    path('deletemanager/<int:mid>',Deletemanager.as_view(),name="delman"),
    # path('editmanager/<int:mid>',Mangerform.as_view(),name="editm")
    path('editman/<int:mid>',Editmanager.as_view(),name="editman"),
    path('reg',Regview.as_view(),name="reg"),
    path('lgout',Logoutview.as_view(),name="lgout"),
    path('demo',demo,name="de")
    
    
]

