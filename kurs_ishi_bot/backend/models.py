from django.db import models


class BotUser(models.Model):
    chat_id = models.IntegerField(unique=True, auto_created=True, null=True, blank=True)
    full_name = models.CharField(max_length=255, auto_created=True, null=True, blank=True)


class Product(models.Model):
    class TextChoice(models.TextChoices):
        SAMSUNG = 'Samsung'
        LG = 'Lg'
        SHIVAKI = 'Shivaki'
        ARTEl = 'Artel'
    title = models.CharField(verbose_name = 'Nomi', max_length=255, null = True, default='-')
    price = models.PositiveBigIntegerField(verbose_name='Narxi', null = True, default=0)
    brand = models.TextField(verbose_name='Brend', max_length=255, choices=TextChoice.choices)
    count = models.PositiveIntegerField(verbose_name='Qolgan', null = True, default=0)

