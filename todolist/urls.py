from django.urls import path
from todolist.views import show_todolist, logout_user, login_user
from todolist.views import register, create_todolist



app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_todolist, name='create-task'),
]
