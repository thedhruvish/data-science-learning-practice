from django.shortcuts import render, redirect, get_object_or_404
from .models import user_details

def create(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        number = request.POST['number']
        gender = request.POST['gender']
        hobby =  request.POST.getlist('hobby')
        city = request.POST['city']
        image = request.FILES.get('image')
        print(image)

        user = user_details(
            name=name,
            email=email,
            password=password,
            number=number,
            gender=gender,
            hobby=",".join(hobby),
            city=city,
            image=image
        )
        user.save()
        return redirect('/show')  
    return render(request, 'create.html')

def show(request):
    users = user_details.objects.all()
    return render(request, 'show.html', {'users': users})

def update(request, userid):
    user = get_object_or_404(user_details, pk=userid)
    print(user.hobby)
    user.hobby = user.hobby.split(",")
    print(user.hobby)
    return render(request, 'create.html', {'user': user})

def update_data(request, userid):
    user = get_object_or_404(user_details, pk=userid)
    if request.method == 'POST':
        user.name = request.POST['name']
        user.email = request.POST['email']
        user.password = request.POST['password']
        user.number = request.POST['number']
        user.gender = request.POST['gender']
        hobby = request.POST.getlist('hobby')
        user.hobby = ",".join(hobby)
        user.city = request.POST['city']
        image = request.FILES.get('image')
        if image:
            user.image = image
        user.save()
        return redirect('/show')
    return render(request, 'create.html', {'user': user})

def delete(request, userid):
    user = get_object_or_404(user_details, pk=userid)
    user.delete()
    return redirect('/show')
