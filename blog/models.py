from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha Creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha Modificado")
  
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ["-created"]
    
    def __str__(self):
        return self.name
        #return "Nombre: {}" . format(self.name)
        


# Creo el modelo para Post

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    content = models.TextField(verbose_name="Contenido")
    published = models.DateTimeField(verbose_name="Publicado", default = now)
    image = models.ImageField(upload_to='blog', verbose_name='Imagen', null=True, blank=True)
    author = models.ForeignKey(User, verbose_name="Autor", on_delete= models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name="Categorias", related_name="get_posts")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha Creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha Modificado")


    class Meta:
        verbose_name = "Entrada"
        verbose_name_plural = "Entradas"
        ordering = ["-created"]
    
    def __str__(self):
        #return "Nombre: {}" . format(self.name)
        return self.title

        

         
