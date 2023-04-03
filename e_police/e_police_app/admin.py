from django.contrib import admin
from .models import signupmodels,visitormodels,contactusmodels,emergencyinformationmodels,complationmodels,searchpolicestationmodels,givefeedbackmodels,firmodels


# Register your models here.

class signup_admin (admin.ModelAdmin):

    list_display = ['role','username','password']

class visitor_admin (admin.ModelAdmin):

    list_display = ['firstname','lastname','username','city','mobile','visitdate']

class contactus_admin (admin.ModelAdmin):

    list_display = ['username','mobile','comments']

class emergencyinformation_admin (admin.ModelAdmin):

    list_display = ['firstname','lastname','username','city','state','zip','address','file']

class complation_admin (admin.ModelAdmin):

    list_display = ['firstname','lastname','username','city','address','mobile','complaintdate']

class searchpolicestation_admin (admin.ModelAdmin):

    list_display = ['firstname','lastname','username','city','state','policestationname']

class givefeedback_admin (admin.ModelAdmin):

    list_display = ['firstname','lastname','username','city','state','zip','comments']

class fir_admin (admin.ModelAdmin):

    list_display = ['firstname','lastname','username','city','state','zip','firdate']

admin.site.register(signupmodels,signup_admin)
admin.site.register(visitormodels,visitor_admin)
admin.site.register(contactusmodels,contactus_admin)
admin.site.register(emergencyinformationmodels,emergencyinformation_admin)
admin.site.register(complationmodels,complation_admin)
admin.site.register(searchpolicestationmodels,searchpolicestation_admin)
admin.site.register(givefeedbackmodels,givefeedback_admin)
admin.site.register(firmodels,fir_admin)
