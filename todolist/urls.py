from django.urls import path
from todolist.views import show_todolist, logout_user, login_user
from todolist.views import register, create_todolist, show_json, show_todolist_ajax, add_todolist_ajax



app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_todolist, name='create-task'),
    path('json/', show_json, name='json'),
    path('ajax/', show_todolist_ajax, name='ajax'),
    path('send/', add_todolist_ajax, name = 'send'),
]
