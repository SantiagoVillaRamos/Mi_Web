from django.db import models
from django.utils.timezone import now
# Create your models here.
class PorfolioForm(models.Model):
    subtitle = models.CharField(max_length=200, verbose_name='Subtitulo')
    description = models.TextField(verbose_name='Descripcion')
    image = models.ImageField(upload_to='media', verbose_name='Imagen')
    url = models.URLField(blank=True, null=True, verbose_name='Link')
    created = models.DateTimeField(default=now, verbose_name='fecha de crecion')
    updated = models.DateTimeField(auto_now=True, verbose_name='fecha de actualizacion')
    
    
    class Meta:
        verbose_name = 'Portafolio'
        verbose_name_plural = 'portafolios'
        ordering = ['-created']
       
    
    def __str__(self):
        return self.subtitle