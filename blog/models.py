from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Cosplay(models.Model):
    # Opciones para el selector
    CATEGORIA_CHOICES = [
        ('LOAN', 'Loan'),
        ('BELA', 'Bela'),
        ('DUO', 'Loan + Bela'),
    ]

    title = models.CharField(max_length=100, verbose_name="Título del Cosplay")
    image = models.ImageField(upload_to='cosplays/', verbose_name="Foto")
    category = models.CharField(max_length=4, choices=CATEGORIA_CHOICES, default='LOAN')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Cosplay"
        verbose_name_plural = "Cosplays"

    def __str__(self):
        return f"{self.title} - {self.get_category_display()}"
