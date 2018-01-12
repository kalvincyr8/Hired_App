from __future__ import unicode_literals
import re
import bcrypt
from django.db import models

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[A-Za-z]\w+$')

class UserManager(models.Manager):
    def loginVal(self, postData):
        results = {'status': True, 'errors':[], 'user': None}
        users = self.filter(email = postData['email'])

        if len(users) < 1:
            results['status'] = False
        else:
            if bcrypt.checkpw(postData['password'].encode(), users[0].password.encode()):
                results['user'] = users[0]
            else:
                results['status'] = False
        return results

    def creator(self, postData):
        user = self.create(
            first_name = postData['first_name'],
            last_name = postData['last_name'],
            email = postData['email'],
            password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()),
        )
        return user

    def validate(self, postData):
        results = {'status': True, 'errors':[]}
        if len(postData['first_name']) < 2:
            results['errors'].append('First Name needs to be at least 2 charcters long.')
            results['status'] = False
        if len(postData['last_name']) < 2:
            results['errors'].append('Last Name needs to be at least 2 charcters long.')
            results['status'] = False
        if not re.match("[^@]+@[^@]+\.[^@]+", postData['email']):
            results['errors'].append('Email is not valid.')
            results['status'] = False
        if postData['password'] != postData['password_confirm']:
            results['errors'].append('passwords do not match.')
            results['status'] = False

        if len(postData['password']) < 8:
            results['errors'].append('passwords must be at least 8 charcters.')
            results['status'] = False

        if len(self.filter(email = postData['email'])) > 0:
            results['errors'].append('User already exsits.')
            results['status'] = False

        if not re.match(NAME_REGEX, postData['first_name']) or not re.match(NAME_REGEX, postData['last_name']):
            results['errors'].append('Names must be charcters only.')
            results['status'] = False

        return results


class User(models.Model):
    first_name = models.CharField(max_length=48)
    last_name = models.CharField(max_length=48)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
