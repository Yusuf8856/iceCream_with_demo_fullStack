from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.core.mail import send_mail


#Here is my actual responses...
def index(request):
    return render(request,'index.html')
    #return HttpResponse("Hello, world. You're at the home index.")

def about(request):
    return render(request,'about.html')
    #return HttpResponse("Hello, world. You're at the home about.")

def services(request):
    return render(request,'services.html')
    #return HttpResponse("Hello, world. You're at the home services.")

def cake(request):
    return render(request,'cake.html')

def softy(request):
    return render(request,'softy.html')

def iceCream(request):
    return render(request,'iceCream.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')

        # Save to DB
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()

        # Send email to admin
        send_mail(
            subject=f"New Contact Message from {name}",
            message=f"Name: {name}\nEmail: {email}\nPhone: {phone}\n\nMessage:\n{desc}",
            from_email=email,
            recipient_list=["yusufali2235@email.com"],  # Change to your real email
            fail_silently=False,
        )

        messages.success(request, "Your message has been sent successfully!")
        return redirect("/contact/")

    return render(request, 'contact.html')
    #return HttpResponse("Hello, world. You're at the home contact.")