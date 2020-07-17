from django.db import models

from django.core.validators import EmailValidator, MinLengthValidator, validate_ipv4_address
from django.core.exceptions import ValidationError

def confirm_level(level):
    if level not in ['CRITICAL', 'DEBUG', 'ERROR', 'WARNING', 'INFO']:
        raise ValidationError('This level is not allowed')


class User(models.Model):
    name = models.CharField('Name', max_length=50)
    last_login = models.DateTimeField('Last login', auto_now=True)
    email = models.CharField('e-mail', max_length=254, validators=[EmailValidator()])
    password = models.CharField('Password', max_length=50, validators=[MinLengthValidator(8)])

    def __str__(self):
        return self.name

class Agent(models.Model):
    name = models.CharField('Name', max_length=50)
    status = models.BooleanField('Status')
    env = models.CharField('Env', max_length=20)
    version = models.CharField('Version', max_length=5)
    address = models.GenericIPAddressField('IP Address', max_length=39, validators=[validate_ipv4_address])

    def __str__(self):
        return self.name

class Event(models.Model):
    level = models.CharField('Level', max_length=20, validators=[confirm_level])
    data = models.TextField('Data')
    arquivado = models.BooleanField('Archived')
    date = models.DateField('Date',auto_now=True)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

def __str__(self):
    return self.level

class Group(models.Model):
    name = models.CharField('Name', max_length=50)

    def __str__(self):
        return self.name
    
 
class GroupUser(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)