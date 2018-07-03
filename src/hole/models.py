from django.db import models
import uuid
from accounts.models import User


class Message(models.Model):
    """The message, to be placed on a user's PigeonHole
       Basically, each message has a sender(User instance),
       (a) recipient(s) (User instance), content(TextField) and
       time of creation.
       Let's keep it Simple and Stupid for now
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    recipients = models.ManyToManyField(User)
    content = models.TextField()

    def __str__(self):
        return self.id
