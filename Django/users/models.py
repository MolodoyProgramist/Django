from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=100)
    #def __str__(self):
       


class User(models.Model):
    ROLES = (
        ('admin','Админ'),
        ('user', 'Пользователь'),
    )

    username = models.CharField(max_length=100)
    email = models.EmailField()
    role = models.CharField(max_length=20, choices=ROLES)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)




# Create your models here.
