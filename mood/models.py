from django.db import models

# Create your models here.
class Mood(models.Model):
    mood = models.CharField(max_length=25)

    def __str__(self):
        return self.mood

    class Meta:
        verbose_name_plural = 'Statuses'
