from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Feedback(models.Model):
    name = models.TextField()
    email = models.EmailField()
    content = models.TextField(null=False)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}: {}...".format(self.name, self.content[:30])

    class Meta:
        ordering = ['-submitted_at', ]


class FeedbackEmail(models.Model):
    """
    Email to which to send feedback.
    """
    email = models.EmailField(null=False)

    def __str__(self):
        return self.email
