from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    profesion = models.CharField(max_length=100, blank=True, null=True) #opcional

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
#----------------------------------------------     
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
#----------------------------------------------    
class DatoCurioso(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
#----------------------------------------------
class Comentario(models.Model):
    nombre =models.CharField(max_length=100)
    comentario = models.TextField()
    dato = models.ForeignKey(DatoCurioso, on_delete=models.CASCADE, related_name="comentarios")

    def __str__(self):
        return f"Comentario de {self.nombre} sobre {self.dato}"