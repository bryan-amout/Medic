from django.shortcuts import render,redirect
from medicoapp.models import Contact

# Create your views here.
def index(request):
    return render(request,'index.html')
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
