import string
import random
from django.shortcuts import render
from .models import Passwords
from .forms import CreatePassword, ViewPassword, DeletePassword, ModifyPassword
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.

@login_required
def home(request):
    username = request.user.get_username()
    return render(request, "passwords/homepage.html", {"user": username})

@login_required
def pwrds(request):
    return render(request = request,
            template_name = 'passwords\main.html',
            context = {"passwords":Passwords.objects.all})

@login_required
def create(response):
    def gene(length=12, chars = string.ascii_letters + string.digits + "!@#$%&"):
        return ''.join(random.choice(chars) for _ in range(length))

    if response.method == "POST":
        form = CreatePassword(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            l = form.cleaned_data["length"]
            p = gene(l)
            new_pas = Passwords(account = n, password = p)
            new_pas.save()
            response.user.passwords.add(new_pas)
            return HttpResponseRedirect("/home")
    else:
        form = CreatePassword()

    return render(response, "passwords/create.html", {"form":form})

@login_required
def search(request):
    if request.method=="GET":

        form = ViewPassword(request.GET)
        submitbutt = request.GET.get('submit')
        if form.is_valid():
            fields = form.cleaned_data["accname"]
            results = Passwords.objects.filter(account__icontains = fields)
            context = {'form': form,
                       'results': results,
                       'submitbutt': submitbutt}

            return render(request, 'passwords/view_pas.html', context)

    else:
        form = ViewPassword()
    return render(request, 'passwords/view_pas.html', {'form':form})

@login_required
def delete(request):
    if request.method == "POST":
        form = DeletePassword(request.POST)
        if form.is_valid():
            name = form.cleaned_data["delaccname"]
            delpass = Passwords.objects.filter(account__icontains = name)
            if delpass in request.user.passwords.all():
                delpass.delete()
                return HttpResponseRedirect('/home')


    else:
        form = DeletePassword()

    return render(request, 'passwords/del_pass.html', {'form': form})

@login_required
def modify(request):
    if request.method == 'POST':
        form = ModifyPassword(request.POST)

        if form.is_valid():
            name = form.cleaned_data["modifaccname"]
            password =
