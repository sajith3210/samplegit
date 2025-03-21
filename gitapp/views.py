from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import RegisterForm
# Create your views here.

def index(request):
    if request.method=="GET":
        return render(request,'index.html')
    

def login(request):
    if request.method=="GET":
        return render(request,'login.html')
    
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save user to database
            login(request, user)  # Log the user in
            return redirect("home")  # Redirect to home page
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})