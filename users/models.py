from django.contrib.auth.models import User
from django.db import models


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    section = models.TextField(null=True)

    def __str__(self):
        full_name = [self.user.first_name]

        if self.user.last_name:
            full_name.append(self.user.last_name)

        full_name.append(f"({self.user.username})")
        return " ".join(full_name)
