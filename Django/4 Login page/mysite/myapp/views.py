from django.shortcuts import render,redirect
from myapp.models import user_data
# Create your views here.
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = user_data.objects.filter(email=email, password=password)
        if (user.count()) == 1:
            return render(request,'dashboard.html',{"user":user})
        else:
            error = "Wrong the User name or Password"
            return render(request,'login.html',{"error":error})

    return render(request,'login.html')

def signup_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = user_data(
            name = name,
            email = email,
            password = password,
        )
        user.save()
        return redirect('/login')
    return render(request,'signup.html')

def dashboard_view(request):
    return render(request,'dashboard.html')