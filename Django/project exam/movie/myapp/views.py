from django.shortcuts import render,redirect,get_object_or_404
from .models import Movies,User,Booking

# Create your views here.

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('password')

        createUser = User(
            name = name,
            email = email,
            contact = contact,
            password = password
        )
        createUser.save()
        return redirect('/login')
    return render(request,'registor.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        getUser = User.objects.filter(email=email,password=password)

        if getUser.count() == 1:
            request.session['id'] = getUser.get().id
            return redirect('/')
        else :
            e = "Email or Password is wrong"
            return render(request,'login.html',{'e':e})
    return render(request,'login.html')

def dashboard(request):
    data = Movies.objects.all()
    return render(request,'dashboard.html',{'data':data})

def addMovie(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        time = request.POST.get('time')
        price = request.POST.get('price')
        image = request.FILES.get('image')

        createMovies = Movies(
            name = name,
            time = time,
            price = price,
            image = image
        )
        createMovies.save()
        return redirect('/')
    return render(request,'add.html')

def booking(request, id):
    data = Booking.objects.filter(MovieId=id)
    userid = request.session.get('id')
    seat_range =  list(map(str, range(1, 10)))
    return render(request, 'showBooking.html', {'data': data, 'movieid': id, 'userid': userid ,'seat_range': seat_range})

def updateT(request,movieid,userid):
    data = Booking.objects.filter(MovieId = movieid,userId=userid)
    disable = Booking.objects.filter(MovieId = movieid)
    seat_range =  list(map(str, range(1, 10)))
    user = get_object_or_404(User, id=userid)
    movies = get_object_or_404(Movies, id=movieid)

    # for booking in disable:
    #     print(f'MovieId: {booking.MovieId}, UserId: {booking.userId}, Seat: {booking.sheet}')  
    
    print(data.count())
    
    if data.count() != 0:
        print('update')
        if request.method == 'POST':
            book = request.POST.getlist('book')
            print(book)
            Booking.objects.filter(MovieId=movieid,userId=userid).update(
                userId=userid,
                sheet=','.join(book),
                MovieId=movieid
            )
            return redirect(f'/booking/{movieid}')
    elif data.count() == 0:
        print('create')
        if request.method == 'POST':
            book = request.POST.getlist('book')
            print(book)
            booking = Booking(
                userId=user,
                sheet=','.join(book),
                MovieId=movies
            )
            booking.save()
            return redirect('/')
    return render(request,'booking.html',{'data':disable,'movieid':movieid,'userid':int(userid),'seat_range': seat_range})


def logout(request):
    del request.session['id']
    return redirect('/')