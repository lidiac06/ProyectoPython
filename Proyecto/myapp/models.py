from datetime import timezone
from django.db import models

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=50, unique=True)
    mail = models.EmailField(max_length=70, unique=True)
    genero_fav = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return f"{self.nombre_usuario}"

class Libro(models.Model):
    titulo = models.CharField(max_length=70)
    autor = models.CharField(max_length=50)
    genero = models.CharField(max_length=30)
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.titulo} - {self.autor} - {self.rating}"

class Review(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name="reviews")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    contenido = models.TextField()

    def __str__(self):
        return f"{self.usuario} - {self.libro}"

