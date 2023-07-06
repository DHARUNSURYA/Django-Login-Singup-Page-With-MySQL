from django.shortcuts import render,redirect
from .forms import data
from .models import User

# Create your views here.
def home(request):
    return render(request,'home.html')
def singup(request):
    if request.method=='POST':
        form=data(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect ('login')
            except:
                pass
    else:  
        form=data()     
    
    return render(request,'singup.html',{'form':form})

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        
        user=User.objects.filter(username=username,password=password).first()
        
        
        if user:
            return redirect('home')
        else:
            return render(request,'login.html')
    
    return render(request,'login.html')
     