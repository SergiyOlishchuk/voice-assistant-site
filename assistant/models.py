from django.db import models

from users.models import User

# Create your models here.
class History(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='Користувач')
    text = models.TextField(verbose_name='Текст', blank=True, null=True)
    from_user = models.BooleanField(verbose_name='Від користувача')
    creating_timestamp = models.DateTimeField(verbose_name='Час створення', auto_now_add=True)
    
    class Meta:
        db_table = "history"
        verbose_name = "Історія"
        verbose_name_plural = "Історія"
    