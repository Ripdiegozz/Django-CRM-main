import django_filters
from django_filters import DateFilter
from .models import Record

class RecordFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="fecha_inicio")
    end_date = DateFilter(field_name="fecha_entrega")
    class Meta:
        model = Record
        fields = '__all__'
        exclude = ['first_name', 'last_name', 'created_at', 'precio', 'fecha_inicio', 'fecha_entrega', 'laboratorio', 'tipo_lente', 'formula_lente', 'add_formula']