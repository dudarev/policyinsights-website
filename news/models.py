from django.db import models

# Create your models here.


class News(models.Model):
    link = models.URLField()
    link_text = models.TextField()
    description = models.TextField()
    time_published = models.DateTimeField()

    class Meta:
        verbose_name_plural = "News"
        ordering = ['-time_published', ]

    def __str__(self):
        return "{} - {}".format(self.link_text, self.description)
