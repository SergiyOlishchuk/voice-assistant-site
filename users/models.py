from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return f"user_{instance.id}/{filename}"

class User(AbstractUser):
    image = models.ImageField(
        upload_to=user_directory_path, blank=True, null=True, verbose_name="Фото профіля"
    )

    token = models.CharField(max_length=300, verbose_name="OpenAI токен")

    class Meta:
        db_table = "users"
        verbose_name = "Користувача"
        verbose_name_plural = "Користувачі"

    def __str__(self) -> str:
        return self.username
