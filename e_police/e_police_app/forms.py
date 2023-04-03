from django import forms
from .models import signupmodels,visitormodels,contactusmodels,emergencyinformationmodels,complationmodels,searchpolicestationmodels,givefeedbackmodels,firmodels

class signupForm (forms.ModelForm):

    class Meta :

        model = signupmodels
        fields = '__all__'

class visitorForm (forms.ModelForm):

    class Meta :

        model = visitormodels
        fields = '__all__'

class contactusForm (forms.ModelForm):

    class Meta :

        model = contactusmodels
        fields = '__all__'

class emergencyinformationForm (forms.ModelForm):

    class Meta :

        model = emergencyinformationmodels
        fields = '__all__'

class complationForm (forms.ModelForm):

    class Meta :

        model = complationmodels
        fields = '__all__'

class searchpolicestationForm (forms.ModelForm):

    class Meta :

        model = searchpolicestationmodels
        fields = '__all__'

class givefeedbackForm (forms.ModelForm):

    class Meta :

        model = givefeedbackmodels
        fields = '__all__'

class firForm (forms.ModelForm):

    class Meta :

        model = firmodels
        fields = '__all__'