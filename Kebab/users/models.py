from django.db import models

# Create your models here.
from django.db import models

class Visit(models.Model):
    total_visits = models.PositiveIntegerField(default=0)  # Счетчик посещений

    def __str__(self):
        return f"Total Visits: {self.total_visits}"
