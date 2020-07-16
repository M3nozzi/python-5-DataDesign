from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField('Name', max_length=50)
    last_login = models.DateTimeField('Last login', auto_now=True)
    email = models.CharField('e-mail', max_length=254)
    password = models.CharField('Password', max_length=50)


class Agent(models.Model):
    raise NotImplementedError


class Event(models.Model):
    raise NotImplementedError


class Group(models.Model):
    raise NotImplementedError


class GroupUser(models.Model):
    raise NotImplementedError
