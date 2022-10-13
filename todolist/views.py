import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render
from todolist.models import ListToDo
from todolist.forms import TaskForm
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    return response

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todo_list = ListToDo.objects.all()
    context = {
        'todo_list': data_todo_list,
        'tasks':  data_todo_list,
        'user': request.user,
    }

    return render(request, "todolist.html", context)

@login_required(login_url='/wishlist/login/')
def show_todolist_ajax(request):
    context = {
    }
    return render(request, "todolist_ajax.html", context)


def show_json(request):
    user = request.user
    data_todo_list = ListToDo.objects.filter(user=user)
    return HttpResponse(serializers.serialize("json", data_todo_list), content_type="application/json")

def create_todolist(request):
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            t = form.cleaned_data["title"]
            d = form.cleaned_data["description"]
            dt = datetime.datetime.now()
            updated = ListToDo(title=t, description =d, date = dt)
            updated.save()
            request.user.todolist.add(updated)
            return redirect('todolist:show_todolist')
    context = {
        'form': form,
    }
    return render(request, "create-task.html", context)

def add_todolist_ajax(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        new_task = ListToDo.objects.create(
            title = title,
            description = description,
            date = datetime.datetime.now(),
            user = request.user,
            )
        new_task.save()
        return HttpResponse("")
    return render(request, 'create-task.html')



