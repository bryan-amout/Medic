from django.shortcuts import render, redirect
from medicoapp.models import Contact, Application, member
from medicoapp.forms import ApplicationForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        if member.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            Members = member.objects.get(
                username=request.POST['username'],
                password=request.POST['password']
                )
            return render(request, 'index.html',{'members':Members})
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def inner(request):
    return render(request,'inner-page.html')
def about(request):
    return render(request,'about.html')
def doctor(request):
    return render(request,'doctor.html')
def departments(request):
    return render(request,'departments.html')
def contact(request):
    if request.method == 'POST':
        all = Contact(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            message=request.POST['message']
            )
        all.save()
        return redirect('/Contact')
    else:
        return render(request,'Contact.html')
def application(request):
    if request.method == 'POST':
        all = Application(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            AppointmentDate=request.POST['phone'],
            Department=request.POST['phone'],
            Doctor=request.POST['phone'],
            message=request.POST['message']
            )
        all.save()
        return redirect('/show')
    else:
        return render(request,'application.html')




def show(request):
    info = Application.objects.all()
    return render(request, 'show.html', {'data':info})

def delete(request,id):
    myappointment = Application.objects.get(id = id)
    myappointment.delete()
    return redirect('/show')

def edit(request,id):
    appointments = Application.objects.get(id = id)
    return render(request,'edit.html',{'x':application})
def update(request,id):
    if request.method == 'POST':
        applications = Application.objects.get(id=id)
        form = ApplicationForm(request.POST, instance=applications)
        if form.is_valid():
            form.save()
            return redirect('/show')
        else:
            return render(request,'edit.html')
    else:
        return render(request,'edit.html')
def register(request):
    if request.method == 'POST':
        members = member(
            name=request.POST['name'],
            username=request.POST['username'],
            password=request.POST['password']
        )
        members.save()
        return redirect('/login')
    else:
        return render(request,'register.html')


def login(request):
    return render(request,'login.html')

