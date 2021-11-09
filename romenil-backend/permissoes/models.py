from django.contrib.auth.models import User
from django.db import models

CARGO_CHOICES = (
    ('desenvolvedor', 'desenvolvedor'),
    ('administrador', 'administrador'),
)

class Cargo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cargo = models.CharField(max_length=50, choices=CARGO_CHOICES)
    