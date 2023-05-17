from django.shortcuts import render
from basicApp.forms import Existing_User_Form, Addon_Form

from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.



def home(request):
    return render(request, 'basicApp/home.html')


def registeration(request):

    registered = False

    if request.method == 'POST':
        user_form = Existing_User_Form(data=request.POST)
        add_on = Addon_Form(data=request.POST)


        if user_form.is_valid() and add_on.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = add_on.save(commit=False)
            profile.user = user 

            if 'DP' in request.FILES:
                print('found it')
                profile.DP = request.FILES['DP']
            
            profile.save()

            registered = True
        
        else:
            print(user_form.errors, add_on.errors)

    else:
        user_form = Existing_User_Form()
        add_on = Addon_Form()

    return render(request, 'basicApp/register.html', {'user_form':user_form, 'add_on':add_on, 'registered':registered})


def user_login_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse("home page"))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Login Failed :(")
            print("Username is {} and Password is {}".format(username,password))
            return HttpResponse("Invalid login details entered!!!")
    else:
        return render(request, 'basicApp/login.html',{})
    


@login_required
def user_logout_view(request):
    logout(request)
    return render(request, 'basicApp/thank.html', {})

@login_required
def special(request):
    return HttpResponse("You have sucesfully logged in !")

    
