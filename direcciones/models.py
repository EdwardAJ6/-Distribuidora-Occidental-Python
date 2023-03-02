from django.db import models
from usuario.models import User

class DirrecionesEnvios(models.Model):
    user = models.ForeignKey(User,null=False,blank=False, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=200)
    localidad = models.CharField(max_length=100,null=False,blank=False)
    barrio = models.CharField(max_length=100)
    default = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.localidad
    
    @classmethod
    def set_default_false(self, user):
        DirrecionesEnvios.objects.filter(user=user).filter(default=True).update(default=False)

    def set_default(self):
        self.default = True
        self.save()   
         
    class Meta:
        verbose_name = 'Dirrecion de Envio'
        verbose_name_plural = 'Dirreciones de Envios'
        db_table = 'DirrecionesEnvios'

    @property
    def direcccionFull(self):
        return '{} - {} - {}'.format(self.direccion,self.localidad,self.barrio)