from django.shortcuts import render , redirect
from app.forms import (
    RegistrationForm ,
    EditProfileForm ,

    )

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm ,PasswordChangeForm
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required


# def home_page(request):
#
#     return render(request,'app/home.html')

def SignUp(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/app')
    else :
        form = RegistrationForm()

        args = {'form' : form}
        return render(request ,'app/signup.html',args)


def profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user' : user}
    return render(request, 'app/profile.html' , args)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST , instance = request.user)

        if form.is_valid():
            form.save()
            return redirect('/app/profile')


    else:
        form = EditProfileForm(instance=request.user)
        args ={'form' :form}
        return render(request, 'app/edit_profile.html', args)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST , user = request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request , form.user)
            return redirect('/app/profile')

        else:
            return redirect('/app/change-password')

    else:
        form = PasswordChangeForm(user=request.user)
        args ={'form' :form}
        return render(request, 'app/change_password.html', args)
