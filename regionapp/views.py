from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import NeighbourHood, Profile, Business, Post
from .forms import UpdateProfileForm, NeighbourHoodForm, PostForm,BusinessForm

def signin(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You have successfuly loged in")
            return redirect ("index")
    return render(request,'registration/login.html')
def register(request):
    if request.method == "POST":
        username=request.POST["username"]
       
        email=request.POST["email"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]
        if password1 !=password2:
            messages.error(request,'Password do not match')
            return render('registration/register')
        new_user=User.objects.create_user(
            username=username,
           
            email=email,
            password=password1,
        )
        new_user.save()
        return render (request,'registration/login.html')
    return render(request,'registration/signup.html')

def signout(request):
    logout(request)
    return render(request,'landing.html')

def landing(request):
    return render(request, 'landing.html')

@login_required(login_url='login')
def index(request):
    posts = Post.objects.all()
    regions = NeighbourHood.objects.all()

    return render(request,'index.html',{'regions':regions,'posts':posts})


@login_required(login_url='login')
def create_region(request):
    if request.method == 'POST':
        form = NeighbourHoodForm(request.POST, request.FILES)
        if form.is_valid():
            region= form.save(commit=False)
            region.admin = request.user.profile
            region.save()
            return redirect('index')
    else:
        form = NeighbourHoodForm()
    return render(request, 'add_region.html', {'form': form})

def create_post(request):
    posts = Post.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            
            post.user = request.user.profile
            post.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'post.html', {'form': form,'posts':posts})

@login_required(login_url='login')
def profile(request, username):
    return render(request, 'profile.html')


@login_required(login_url='login')
def edit_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile', user.username)
    else:
        form = UpdateProfileForm(instance=request.user.profile)
    return render(request, 'editprofile.html', {'form': form})

def single_region(request, region_id):
    region = NeighbourHood.objects.get(id=region_id)
    business = Business.objects.filter(neighbourhood=region)
    posts = Post.objects.filter(region=region)
    posts = posts[::-1]
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            b_form = form.save(commit=False)
            b_form.neighbourhood = region
            b_form.user = request.user.profile
            b_form.save()
            return redirect('single-region', region.id)
    else:
        form = BusinessForm()
    params = {
        'region': region,
        'business': business,
        'form': form,
        'posts': posts
    }
    return render(request, 'single-region.html', params)
def hoods(request):
    all_hoods = NeighbourHood.objects.all()
    all_hoods = all_hoods[::-1]
    params = {
        'all_hoods': all_hoods,
    }
    return render(request, 'all_hoods.html', params)
def join_hood(request, id):
    neighbourhood = get_object_or_404(NeighbourHood, id=id)
    request.user.profile.neighbourhood = neighbourhood
    request.user.profile.save()
    return redirect('hood')


def leave_hood(request, id):
    hood = get_object_or_404(NeighbourHood, id=id)
    request.user.profile.neighbourhood = None
    request.user.profile.save()
    return redirect('hood')




@login_required(login_url='login')
def search_business(request):
    if request.method == 'GET':
        name = request.GET.get("title")
        results = Business.objects.filter(name__icontains=name).all()
        print(results)
        message = f'name'
        params = {
            'results': results,
            'message': message
        }
        return render(request, 'results.html', params)
    else:
        message = "You haven't searched for any image category"
    return render(request, "results.html")
