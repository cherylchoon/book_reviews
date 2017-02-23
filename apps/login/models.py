from __future__ import unicode_literals
from django.db import models
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
import bcrypt

onlyLetters = RegexValidator(r'^[a-zA-Z]+$', message='Must be letters only.')
def validateLengthGreaterThanTwo(value):
    if len(value) < 3:
        raise ValidationError('Must be longer than 2 characters'.format(value))

class UserManager(models.Manager):
    def login(self, object):
        email = object['email']
        password = object['password']
        user = User.objects.get(email=email)
        pw_hash = bcrypt.hashpw(password.encode(), user.password.encode())
        if pw_hash == user.password:
            return {'success': 'You have logged in succesfully!', 'username': user.first_name, 'user_id': user.id}
        else:
            return {'error': 'Username/Password does not match.'}

    def register(self, object, **kwargs):
        first_name = object['first_name']
        last_name = object['last_name']
        email = object['email']
        password = object['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        User.objects.create(first_name=first_name, last_name=last_name, email=email, password=pw_hash)
        user = User.objects.get(email=email)
        return {'success': 'You have registered succesfully!', 'user_id': user.id}

class User(models.Model):
    first_name = models.CharField(max_length=55, validators=[validateLengthGreaterThanTwo, onlyLetters])
    last_name = models.CharField(max_length=55, validators=[validateLengthGreaterThanTwo, onlyLetters])
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
