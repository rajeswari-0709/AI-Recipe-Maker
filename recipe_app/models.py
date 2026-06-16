from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    ingredients = models.TextField()

    recipe = models.TextField()

    image = models.ImageField(
        upload_to="ingredients/",
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.created_at}"