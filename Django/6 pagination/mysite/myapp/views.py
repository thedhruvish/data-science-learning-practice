from django.shortcuts import render,redirect
from myapp.models import user_data
from django.core.paginator import Paginator
# Create your views here.
def login_view(request):  
    try:
        username = request.session['username']
        return redirect('/dashboard/')
    except:
     
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = user_data.objects.filter(email=email, password=password)
            if (user.count()) == 1:
                request.session['username'] = user.get().name
                return redirect('/dashboard/')
            else:
                error = "Wrong the User name or Password"
                return render(request,'login.html',{"error":error})
        return render(request,'login.html')
   
def signup_view(request):
    try:
        username = request.session['username']
        return redirect('/dashboard/')
    except:
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
            return redirect('/signup')
        return render(request,'signup.html')

def dashboard_view(request):
    # try:
    #     username = request.session['username']
    #     return render(request,'dashboard.html',{"username":username})
    # except:       
    #     return redirect('/login/')   
    # if 'username' in request.session:
    # else:
    print(request.GET.get('q'))
    if request.method == 'GET' and request.GET.get('q'):
        q = request.GET.get('q')
        data = user_data.objects.filter(name__icontains=q)
    else:
        data = user_data.objects.all()
        q=None
    paginator = Paginator(data, 2) # Display 25 objects per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print(page_obj)
    return render(request, 'dashboard.html', {'page_obj': page_obj,'q':q})
        

def logout_view(request):
    del request.session['username']
    return redirect('/login/')