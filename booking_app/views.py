from django.shortcuts import render
from django.contrib import messages
from .models import Person

# Create your views here.

def index(request):
    
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        email = request.POST.get('email')
        comments = request.POST.get('comments')
        #print(f"{user_name}\n\n{email}\n\n\n\n")
        p = Person(user_name=user_name, email=email, comments=comments)
        p.save()
        messages.add_message(request, messages.INFO, "Form submitted!!")
        
    
    return render(request, 'booking_app/html/index.html')