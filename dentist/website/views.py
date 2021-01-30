from django.shortcuts import render
from django.core.mail import send_mail


def home(request):
    return render(request,  'home.html', {})

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        #send an Email
        send_mail(
            name, # name
            subject, # subject
            message, # Message
            ['email'], # from Email
            ['uphatori@gmail.com'], # to Email
        )

        return render(request, 'contact.html', {'name': name})
    else:
        return render(request, 'contact.html', {})
