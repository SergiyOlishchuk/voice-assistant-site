from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    image = models.ImageField(
        upload_to="users_images", blank=True, null=True, verbose_name="Фото профіля"
    )

    openAI_token = models.CharField(max_length=300, verbose_name="OpenAI токен")

    class Meta:
        db_table = "users"
        verbose_name = "Користувача"
        verbose_name_plural = "Користувачі"

    def __str__(self) -> str:
        return self.username
