from django.db import models

class Line(models.Model):
    # description = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    # link = models.CharField(max_length=255)
    image = models.ImageField(upload_to='portfolio/sites')
    status = models.BooleanField(default=False, verbose_name='Status', help_text='Ativado ou desativado')

class Background(models.Model):
    image = models.ImageField(upload_to='portfolio/images')
    status = models.BooleanField(default=False, verbose_name='Status', help_text='Ativado ou desativado')
