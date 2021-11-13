from django.db import models

# Create your models here.


class Project(models.Model):
    """I'm projects."""
    name = models.CharField("name", max_length=200)
    title = models.TextField('text')
    image = models.ImageField(upload_to='image/', blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Loyiha"
        verbose_name_plural = "Loyihalar"

