from django.shortcuts import render,redirect
from .models import Admin,Branch,Course,Inquiry

# Create your views here.

def login(request):    
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        login_user = Admin.objects.filter(email=email, password=password)
        if (login_user.count()) == 1:
            request.session['email'] = login_user.get().email
            request.session['image'] = login_user.get().image.url
            request.session['name'] = login_user.get().name
            return redirect('/dashboard')
        else:
            return redirect('/')

    return render(request,'login.html')


def dashboard(request):
    return render(request,'dashboard.html')

# Admin
def add_admin(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        contact = request.POST['contact']
        image=request.FILES['image']

        new_admin = Admin(
            name=name,
            email=email,
            password=password,
            contact=contact,
            image=image
        )
        new_admin.save()
        return redirect('/admin')

    return render(request,'add_admin.html')

def view_admin(request):
    data = Admin.objects.all()
    return render(request,'view_admin.html',{'data':data})

def update_admin(request,id):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        contact = request.POST['contact']
        if request.FILES.get('image'):
            Admin.objects.filter(id=id).update(image=request.FILES['image'])

        Admin.objects.filter(id=id).update(
            name=name,
            email=email,
            password=password,
            contact=contact,
        )
        return redirect('/admin')
    data = Admin.objects.get(id=id)
    return render(request,'add_admin.html',{'data':data})

def delete_admin(request,id):
    Admin.objects.filter(id=id).delete()
    return redirect('/admin')


#------------------------ Branch ----------------------

def view_Branch(request):
    data = Branch.objects.all()
    return render(request,'view_branch.html',{'data':data})

def add_Branch(request):
    if request.method == 'POST':
        b_name = request.POST['b_name']
        new_branch =Branch(
            b_name=b_name
        )
        new_branch.save()
        print('ok')
        return redirect('/branch')
    return render(request,'add_branch.html')

def update_Branch(request,id):
    if request.method == 'POST':
        b_name = request.POST['b_name']

        Branch.objects.filter(id=id).update(
            b_name=b_name
        )
        return redirect('/branch')
    data = Branch.objects.get(id=id)
    return render(request,'add_branch.html',{'data':data})

def delete_Branch(request,id):
    Branch.objects.filter(id=id).delete()
    return redirect('/branch')


#---------------------course----------------------------------

def view_course(request):
    data = Course.objects.all()
    return render(request,'view_course.html',{'data':data})

def add_course(request):
    if request.method == 'POST':
        c_name = request.POST['course']
        new_Course =Course(
            c_name=c_name
        )
        new_Course.save()
        return redirect('/course')
    return render(request,'add_course.html')

def update_course(request):
    if request.method == 'POST':
        b_name = request.POST['b_name']

        Course.objects.filter(id=id).update(
            b_name=b_name
        )
        return redirect('/course')
    return render(request,'add_course.html')

def delete_Course(request,id):
    Course.objects.filter(id=id).delete()
    return redirect('/course')


#-------------------------- Inquiry ----------------------------------


def add_inquiry(request):
    if request.method == 'POST':
        name = request.POST['name']
        contact = request.POST['contact']
        course = request.POST['course']
        branch = request.POST['branch']
        detail = request.POST['detail']
        inquiryby = request.POST['inquiryby']
        total_fee = request.POST['total_fee']
        date = request.POST['date']
        status = request.POST['status']                   

        new_inquiry = Inquiry(
            name=name,
            contact=contact,
            course=course,
            branch=branch,
            detail=detail,
            inquiryby=inquiryby,
            total_fee=total_fee,
            date=date,
            status=status
        )
        new_inquiry.save()
        return redirect('/inquiry')
    return render(request,'add_inquiry.html')

def view_inquiry(request):
    data = Inquiry.objects.all()
    return render(request,'view_inquiry.html',{'data':data})

def update_inquiry(request,id):
    if request.method == 'POST':
        name = request.POST['name']
        contact = request.POST['contact']
        course = request.POST['course']
        branch = request.POST['branch']
        detail = request.POST['detail']
        inquiryby = request.POST['inquiryby']
        total_fee = request.POST['total_fee']
        date = request.POST['date']
        status = request.POST['status']   

        Inquiry.objects.filter(id=id).update(
            name=name,
            contact=contact,
            course=course,
            branch=branch,
            detail=detail,
            inquiryby=inquiryby,
            total_fee=total_fee,
            date=date,
            status=status
        )
        return redirect('/inquiry')
    data = Inquiry.objects.get(id=id)
    return render(request,'add_inquiry.html',{'data':data})

def delete_inquiry(request,id):
    Inquiry.objects.filter(id=id).delete()
    return redirect('/inquiry')












































def register(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        gender=request.POST['gender']
        status=request.POST['status']
        branch=request.POST['branch']
        image=request.FILES['image']

        newUser = Admin(
            name=name,
            email=email,
            password=password,
            gender=gender,
            status=status,
            b_id=branch,
            image=image
        )
        newUser.save()
        return redirect('/dashboard/')

    return render(request,'register.html')


