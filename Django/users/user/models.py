from typing import Any

from django.db import models

# Create your models here.

class TelegramUser(models.Model):
   telegram_id = models.BigIntegerField(verbose_name="Telegram id", unique=True, primary_key=True)
   full_name = models.CharField(verbose_name= "Ism", max_length=255, null=True)
   username = models.CharField(verbose_name="Telegram username", max_length=255, null=True)
   def __str__(self):
       return self.full_name


class UserInfo(models.Model):
   phone = models.CharField(max_length=12, primary_key=True)
   user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE, primary_key=True)
   email = models.CharField(max_length=255)

   def __str__(self):
      return self.phone