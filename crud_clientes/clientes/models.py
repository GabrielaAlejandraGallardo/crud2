from django.db import models

# Create your models here.

class Clientes(models.Model):
    id=models.AutoField(primary_key=True)
    nom = models.CharField(max_length=40, verbose_name='Nombre')
    ap = models.CharField(max_length=40, verbose_name='Apellido Paterno')
    am = models.CharField(max_length=40, verbose_name='Apellido Materno')
    dir = models.TextField(null=True, verbose_name='Dirección')
    foto= models.ImageField(upload_to='imagenes/', verbose_name='Foto',null=True)
    
    def __str__(self):
        fila="Id: "+ str(self.id)+ "-"+ "Nombre: " +self.nom + "-" "Apellido Paterno: " +self.ap
        return fila 
    
    def delete(self, using=None, Keep_parents=False):
        self.foto.storage.delete(self.foto.name)
        super().delete()