from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    message = models.TextField()
    
    time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-time']

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.pk)])

    def __str__(self):
        return self.message
