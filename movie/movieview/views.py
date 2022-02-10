from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .form import CreateUserForm
from django.contrib import auth
from .form import ReviewsForm
from django.contrib.sites.models import Site
from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import MovieDetail, MovieLink, MovieActor, InTheater, MovieStars, CastCrew, Reviews, Genres, PloteKewords


def index(request):
    form = CreateUserForm()
    movies = MovieDetail.objects.filter(is_slider=True)
    movie_detail = MovieDetail.objects.filter(is_slider=False)
    actor_detail = MovieActor.objects.all()
    youtube_link = MovieLink.objects.all()
    in_theater = InTheater.objects.all()

    context = {
        'movies': movies,
        'movie_detail': movie_detail,
        'actor_detail': actor_detail,
        'youtube_link': youtube_link,
        'in_theater': in_theater,
        'form': form
    }
    return render(request, 'movieview/index.html', context)


def moviesingle(request, id):
    moviename = MovieDetail.objects.filter(id=id)
    moviestar = MovieStars.objects.all()
    moviecast = CastCrew.objects.all()
    user_reviews = Reviews.objects.all().order_by('-id')
    movie_genres = Genres.objects.all()
    plot_word = PloteKewords.objects.all()
    if request.method == 'POST':
        form = ReviewsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            if request.user.is_authenticated:
                form.user = request.user
                form.moviename = moviecast
                form.save()
            else:
                return redirect("login")
    form = ReviewsForm()
    context = {
        'moviename': moviename,
        'moviestar': moviestar,
        'moviecast': moviecast,
        'user_reviews': user_reviews,
        'form': form,
        'movie_genres': movie_genres,
        'plot_word': plot_word
    }
    return render(request, 'movieview/moviesingle.html', context)


def moviegrid(request):
    return render(request, 'movieview/moviegrid.html')


def movielist(request):
    return render(request, 'movieview/movielist.html')


def moviegridfw(request):
    return render(request, 'movieview/moviegridfw.html')


def seriessing(request):
    return render(request, 'movieview/seriessingle.html')


def celebritygrid(request):
    return render(request, 'movieview/celebritysingle.html')


def celebritygrid1(request):
    return render(request, 'movieview/celebritygrid01.html')


def celebritygrid02(request):
    return render(request, 'movieview/celebritygrid02.html')


def celebritylist(request):
    return render(request, 'movieview/celebritylist.html')


def bloglist(request):
    return render(request, 'movieview/bloglist.html')


def bloggrid(request):
    return render(request, 'movieview/bloggrid.html')


def blogdetail(request):
    return render(request, 'movieview/blogdetail.html')


def userfavoritegrid(request):
    return render(request, 'movieview/userfavoritegrid.html')


def userfavoritelist(request):
    return render(request, 'movieview/userfavoritelist.html')


def userprofile(request):
    return render(request, 'movieview/userprofile.html')


def userrate(request):
    return render(request, 'movieview/userrate.html')


def landing(request):
    return render(request, 'movieview/landing.html')


def comingsoon(request):
    return render(request, 'movieview/comingsoon.html')


def signuppage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account is just created for ' + user)
                return redirect('index')

        context = {'form': form}

        return render(request, 'movieview/index.html', context)


def loginpage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password1')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'User name Or password is incorrect')

        return render(request, 'header.html')


def logoutuser(request):
    logout(request)
    return redirect('login')