from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import ContactForm
from .models import Project
# Create your views here.
def home(request):
    form = ContactForm()
    projects = Project.objects.all()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message sent successfully.")
            return redirect('/')

    return render(request, 'home.html', {
        'form': form,
        'projects': projects
    })
def contact(request):
    if request.method=="POST":
        print('post')
        name=request.POST.get('name')
        email=request.POST.get('email')
        content=request.POST.get('content')
        number=request.POST.get('number')
        print(name,email,number,content)
        if len(name)> 1 and len(name)<30:
            pass
        else:
            messages.error(request,'Length of name should be greater than 2 and less than 30 words')
            return render(request,'home.html')
        if len(email)>1 and len(email)<30:
            pass
        else:
            messages.error(request,'invalid email try again')
            return render(request,'home.html')
        if len(number)>2 and len(number)<13:
            pass
        else:
            messages.error(request,'invalid number try again')
            return render(request,'home.html')
        ins=Contact(name=name,email=email,content=content,number=number)
        ins.save()
        messages.success(request,'Thank you for connecting me || your message have been saved')
        print('data has been saved to database')
        print('the request is no pass')

    return render(request,'home.html')
def project_detail(request, id):
    project = Project.objects.get(id=id)
    return render(request, 'project_detail.html', {'project': project})     


