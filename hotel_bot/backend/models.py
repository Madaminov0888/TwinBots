from django.db import models

class Hotel_rooms(models.Model):
    class Meta:
        verbose_name = 'Xona'
        verbose_name_plural = 'Xonalar'
    title = models.CharField(max_length=255, null = True, default='-')
    