from django.db import models
from django.contrib.auth.models import User

class ListToDo(models.Model):
    user= models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="todolist",null=True, blank=True)
    date= models.DateField(auto_now_add=True)
    title= models.CharField(max_length=200, null=True)
    description= models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
