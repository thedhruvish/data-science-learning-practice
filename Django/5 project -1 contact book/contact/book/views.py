from django.shortcuts import render,redirect,HttpResponse
from .models import User,Contact,Track 
from datetime import datetime



import logging
logger = logging.getLogger(__name__)

logging.basicConfig(filename='user.log', encoding='utf-8', level=logging.INFO,format='%(asctime)s %(message)s')



#  your views here.
def login_view(request):
    try:
        if 'email' in request.session:
            return redirect('/dashboard/')
        else:
            if request.method == 'POST':
                email = request.POST.get('email')
                password = request.POST.get('password')            
                login_user = User.objects.filter(email=email, password=password)
                if login_user.count() == 1:
                    request.session['email'] = login_user.get().email
                    request.session['start'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    print('start  = ',request.session['start'])
                    logger.info(f"User {email} logged in at {request.session['start']}.")

                    return redirect('/dashboard/')
                else:
                    errorMSG = 'Your Email and Password is Wrong'
                    return render(request,'login.html',{"msg":errorMSG})                    
            return render(request,'login.html')
    except Exception as e:
        return render(request,'error.html',{'error':e})
    
def logout_view(request):
    convert = lambda a :  datetime.strptime(a, '%Y-%m-%d %H:%M:%S')
    try:
        if 'email' in request.session:
            email =  request.session['email']
            start =convert(request.session['start'])
            end =convert(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            logger.info(f"User {email} logged out at {end}.")
            logger.info(f"User {email} log in Duration: {end - start}.")
            t = Track(email=email,
                  login=start,
                  logout=end,
                  duration=str(end-start)
            )
            t.save()
            del request.session['email']
            del request.session['start']
            return redirect('/')
        else:
            return redirect('/')    
    except Exception as e:
        return render(request,'error.html',{'error':e})
    
def duration(request):
    data = Track.objects.all()
    return render(request,'duration.html',{'data':data})

def register_view(request):
    try:
        if 'email' in request.session:
            return redirect('/dashboard/')
        else:
            if request.method == 'POST':
                name = request.POST.get('name')
                email = request.POST.get('email')
                password = request.POST.get('password')

                new_user = User(
                    name=name,
                    email=email,
                    password=password
                )
                new_user.save()
                return redirect('/')
            return render(request,'register.html')
    except Exception as e:
        return render(request,'error.html',{'error':e})

def dashboard_view(request):
    try:
        if 'email' in request.session:
            return render(request,'dashboard.html')
        else:    
            return redirect('/')
    except Exception as e:
        return render(request,'error.html',{'error':e})

def add_contact_view(request):
    try:
        if 'email' in request.session:
            if request.method == 'POST':
                name = request.POST.get('name')
                email = request.POST.get('email')
                gender = request.POST.get("gender")
                city = request.POST.get("city")
                c_number =request.POST.get('c_number')
                address = request.POST.get('address')

                new_contact = Contact(
                    owner=request.session['email'],
                    name=name,
                    email=email,
                    gender=gender,
                    city=city,
                    c_number = c_number,
                    address = address
                )
                new_contact.save()
                return redirect('/view/')
            return render(request,'add_contact.html')
        else: 
            return redirect('/')
    except Exception as e:
        return render(request,'error.html',{'error':e})

def view_contact_view(request):
    try:
        if 'email' in request.session:
            contacts = Contact.objects.filter(owner=request.session['email'])
            return render(request,'view_contact.html',{'data':contacts})
        else:
            return redirect('/')
    except Exception as e:
        return render(request,'error.html',{'error':e})

def change_password_view(request):
    try:
        if 'email' in request.session:
            if request.method == 'POST':
                password = request.POST.get('password')
                checkUser = User.objects.filter(email=request.session['email'],password=password)

                if checkUser.count() == 1:
                    print('ok')
                    return redirect('/set_password')
                else:
                    return redirect('/logout/')
            return render(request,'change_password.html')
        else:
            return redirect('/')
    except Exception as e:
        return render(request,'error.html',{'error':e})

def set_new_password(request):
    try:
        if 'email' in request.session:
            if request.method == 'POST':
                new_password = request.POST.get('n_password')
                curr_new_password = request.POST.get('curr_new_password')

                oldpassword = User.objects.filter(email=request.session['email']).get().password

                if new_password == curr_new_password and oldpassword != new_password:
                    update = User.objects.filter(email=request.session['email']).update(password=new_password)
                    return redirect('/logout/')
                else:
                    msg = "Enter New Password"
                    return render(request,'new_password.html',{'error':msg})
            return render(request,'new_password.html')
        else:
            return redirect('/')
    except Exception as e:
        return render(request,'error.html',{'error':e})


def edit_contact_view(request,id):
    try:
        if 'email' in request.session:
            contact = Contact.objects.get(id=id)
            return render(request,'add_contact.html',{'user':contact})
        else:
            return redirect('/')
    except Exception as e :
        return render(request,'error.html',{'error':e})

    


def update_contact_view(request,id):
    try:
        if 'email' in request.session:
            if request.method == 'POST':
                name = request.POST.get('name')
                email = request.POST.get('email')
                gender = request.POST.get("gender")
                city = request.POST.get("city")
                c_number =request.POST.get('c_number')
                address = request.POST.get('address')

                update = Contact.objects.filter(id=id).update(
                    name=name,
                    email=email,
                    gender=gender,
                    city=city,
                    c_number = c_number,
                    address=address
                )
                return redirect("/view/")
        else:
            return redirect('/')
    except Exception as e:
        return render(request,'error.html',{'error':e})

def update_profile(request):
    try:
        if 'email' in request.session:
            if request.method == 'POST':
                email = request.POST['email']
                update = User.objects.filter(email=request.session['email']).update(email=email)
                return redirect('/logout/')
            return render(request,'profile.html')

        else:
            return redirect('/')
    except Exception as e:
        return render(request,'error.html',{'error':e})



