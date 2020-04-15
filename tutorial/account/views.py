from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import RegisterForm,EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required




def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()

    else:
       form=RegisterForm()
    return render(request,'account/register.html',{'form':form})


@login_required
def profile(request):
    return render(request,'account/profile.html',{'user':request.user})



@login_required
def edit_profile(request):

    if request.method=='POST':
        form=EditProfileForm(request.POST,instance=request.user)
        if form.is_valid:

            form.save()
            return reverse('account:profile')

    else:
        form = EditProfileForm(instance=request.user)

    return render(request,'account/edit_profile.html',{'form':form})



@login_required
def password_change(request):
    if request.method=='POST':
        form=PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return reverse('account:profile')
        else:
            return reverse('account:password_change')

    else:
        form=PasswordChangeForm(user=request.user)

    return render(request,'account/password_change.html',{'form':form})
