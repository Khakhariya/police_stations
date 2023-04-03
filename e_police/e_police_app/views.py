from django.shortcuts import render,redirect
from .forms import signupForm,visitorForm,complationForm,emergencyinformationForm,complationForm,searchpolicestationForm,givefeedbackForm,firForm,contactusForm
from .models import signupmodels
from django.contrib.auth import logout
from django.core.mail import send_mail
from e_police import settings

# Create your views here.

def index(request):

    use = request.session.get('username')
    role =  request.session.get('role')

    if request.method == 'POST':
        if request.POST.get ('signup') == 'signup':
            user = signupForm(request.POST)
            if user.is_valid():
                user.save()
                print ('user created successfully')

                # Mail Sending code :-
                subject = 'Account Created successfully'
                msg = 'Dear User, \n\nThank you for create an account on our site \nYou will get benefits in your farm \nAnd Your problem will be solved by our exert team \n\nFor More information Contact Us on \n+91 91234 56789'
                Mail = settings.EMAIL_HOST_USER
                user_mail = [request.POST['username']]

                send_mail(subject=subject, message=msg,
                              from_email=Mail, recipient_list=user_mail)

            else:
                print (user.errors)
        if request.POST.get ('login') == 'login':
            unm = request.POST['username']
            pas = request.POST['password']

            log_var = signupmodels.objects.filter(username=unm,password=pas)
            user = signupmodels.objects.get(username=unm)
            if log_var:
                print ('login successfully.')
                request.session['username'] =unm
                request.session['role'] = user.role
                return redirect('admin')
            else :
                print ('Error! Login Failed')


    return render (request,'index.html',{'use':use,'role':role})

def userlogout (request):


    logout(request)

    return redirect ('/')

def admin(request):

    use = request.session.get('username')
    role =  request.session.get('role')

    return render (request,'admin.html',{'use':use,'role':role})

def policestaion(request):

    use = request.session.get('username')
    role =  request.session.get('role')
    
    return render (request,'policestation.html',{'use':use,'role':role})

def citizen(request):
    
    use = request.session.get('username')
    role =  request.session.get('role')

    return render (request,'citizen.html',{'use':use,'role':role})

def inspectormodule(request):

    use = request.session.get('username')
    role =  request.session.get('role')
    
    return render (request,'inspectotmodule.html',{'use':use,'role':role})

def visitor(request):

    use = request.session.get('username')
    role =  request.session.get('role')


    if request.method == 'POST':
        emvar = visitorForm(request.POST)
        if emvar.is_valid():
            emvar.save()
            print ('Data Uploaded Successfully.')
        else :
            print (emvar.errors)

    return render (request,'visitor.html',{'use':use,'role':role})

def complaint_status(request):

    use = request.session.get('username')
    role =  request.session.get('role')

    return render (request,'complaint_status.html',{'use':use,'role':role})

def complaint(request):

    use = request.session.get('username')
    role =  request.session.get('role')

    if request.method == 'POST':
        emvar = complationForm(request.POST)
        if emvar.is_valid():
            emvar.save()
            print ('Data Uploaded Successfully.')
        else :
            print (emvar.errors)

    return render (request,'complaint.html',{'use':use,'role':role})

def contactus(request):

    use = request.session.get('username')
    role =  request.session.get('role')

    if request.method == 'POST':
        emvar = contactusForm(request.POST)
        if emvar.is_valid():
            emvar.save()
            print ('Data Uploaded Successfully.')
        else :
            print (emvar.errors)

    return render (request,'Contactus.html',{'use':use,'role':role})

def emergency_information(request):

    use = request.session.get('username')
    role =  request.session.get('role')

    if request.method == 'POST':
        emvar = emergencyinformationForm(request.POST,request.FILES)
        if emvar.is_valid():
            emvar.save()
            print ('Data Uploaded Successfully.')
        else :
            print (emvar.errors)

    return render (request,'emergency_information.html',{'use':use,'role':role})

def FIR_status(request):

    use = request.session.get('username')
    role =  request.session.get('role')

    return render (request,'FIR_status.html',{'use':use,'role':role})

def FIR(request):

    use = request.session.get('username')
    role =  request.session.get('role')

    if request.method == 'POST':
        emvar = firForm(request.POST)
        if emvar.is_valid():
            emvar.save()
            print ('Data Uploaded Successfully.')
        else :
            print (emvar.errors)

    return render (request,'FIR.html',{'use':use,'role':role})

def give_feedback(request):

    use = request.session.get('username')
    role =  request.session.get('role')

    if request.method == 'POST':
        emvar = givefeedbackForm(request.POST)
        if emvar.is_valid():
            emvar.save()
            print ('Data Uploaded Successfully.')
        else :
            print (emvar.errors)

    return render (request,'give_feedback.html',{'use':use,'role':role})

def rules_regulation(request):

    use = request.session.get('username')
    role =  request.session.get('role')

    return render (request,'rules_regulation.html',{'use':use,'role':role})

def search_policestation(request):

    use = request.session.get('username')
    role =  request.session.get('role')

    if request.method == 'POST':
        emvar = searchpolicestationForm(request.POST)
        if emvar.is_valid():
            emvar.save()
            print ('Data Uploaded Successfully.')
        else :
            print (emvar.errors)

    return render (request,'search_policestation.html',{'use':use,'role':role})

def about(request):

    use = request.session.get('username')
    role =  request.session.get('role')

    return render (request,'about.html',{'use':use,'role':role})