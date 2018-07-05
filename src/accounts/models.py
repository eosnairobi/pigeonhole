
from django.db import models
# from django.db.models.signals import post_save
# from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
import uuid
from django.utils import timezone


# Custom User Model
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    joined = models.DateTimeField(default=timezone.now)
