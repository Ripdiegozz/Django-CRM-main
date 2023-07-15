from django.db import models
from django.utils import timezone

now = timezone.now()

# Create your models here.
class Record(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=50)
	last_name =  models.CharField(max_length=50)
	cedula =  models.BigIntegerField()
	fecha_inicio = models.DateField(auto_now=False, auto_now_add=False)
	fecha_entrega =  models.DateField(auto_now=False, auto_now_add=False)
	tipo_lente =  models.CharField(max_length=1000)
	laboratorio =  models.CharField(max_length=250)
	precio =  models.FloatField()
	add_formula = models.BooleanField(default=False)
	formula_lente =  models.CharField(max_length=1000)

	def __str__(self):
		return(f"{self.first_name} {self.last_name}")
