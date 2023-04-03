from django.contrib import admin
from django.urls import path
from e_police_app import views

urlpatterns = [
    path ('',views.index),
    path ('adminpage/', views.admin,name='admin'),
    path ('about/',views.about),
    path ('policestation/',views.policestaion),
    path ('citizen/',views.citizen),
    path ('inspectormodule/',views.inspectormodule),
    path ('visitor/', views.visitor),
    path ('userlogout/', views.userlogout),
    path ('complaint_status/', views.complaint_status),
    path ('complaint/', views.complaint),
    path ('contactus/', views.contactus),
    path ('emergency_information/', views.emergency_information),
    path ('FIR_status/', views.FIR_status),
    path ('FIR/', views.FIR),
    path ('give_feedback/', views.give_feedback),
    path ('rules_regulation/', views.rules_regulation),
    path ('search_policestation/', views.search_policestation),
]