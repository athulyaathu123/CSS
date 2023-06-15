from django.urls import path
from .views import *


urlpatterns = [
    
    path('demo',demo,name="demo"),
    path('addpat',Addpatient.as_view(),name='addpat'),
    path('addpre',Addprescription.as_view(),name='addpre'),
    path('addc',Add.as_view(),name='addm'),
    path('strcount',Count_str.as_view(),name='counts'),
    path('adm',AdmitView.as_view(),name="adm"),
    path('calcu',Calcu.as_view(),name="cal"),
    path('viewpatient',Viewpatient.as_view(),name="viewpat"),
    path('deletepatient/<int:pid>',Deletepatient.as_view(),name="delpat"),
    path('editpa/<int:pid>',Editpatient.as_view(),name="editp"),
    path('adddoc',DoctorAform.as_view(),name="docadd"),
    path('viewdoc',Doctorview.as_view(),name="viewdoc"),
    path('deldoc/<int:pid>',Deletedoctor.as_view(),name="deldoc"),
    path('editdoc/<int:did>',Editdoctor.as_view(),name="editdoc")
    
    
]