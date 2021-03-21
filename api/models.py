from django.db import models
import string
import random

def generate_random_code():
    length = 6

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Room.objects.filter(code = code).count() == 0:
            break
    return code

class Room(models.Model):
    code = models.CharField(max_length = 8, default="", unique=True)
    host = models.CharField(max_length = 50, unique=True)
    guest_pause_permission = models.BooleanField(null=False, default=False)
    guest_votes_skip = models.IntegerField(null=False, default=2)
    date_created = models.DateTimeField(auto_now=True)