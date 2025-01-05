from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Message(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='emisor')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receptor')
    text = models.CharField(max_length=500)

    def __str__(self):
        return str(self.creation_date) + ' - ' + str(self.from_user)