from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
import datetime
from .models import Record

class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'ejemplo@gmail.com'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombres'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellidos'}))


	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'Usuario'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Requerido. 150 Caracteres o menos. Letras, digitos y @/./+/-/_ únicamente.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Contraseña'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Tu contraseña no puede ser muy similar a tu otra información personal.</li><li>Tu contraseña debe contener al menos 8 caracteres.</li><li>Tu contraseña no puede ser una usada comúnmente.</li><li>Tu contraseña no puede ser enteramente numérica.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirmar contraseña'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Ingresa de nuevo la contraseña, para verificación.</small></span>'	




# Create Add Record Form
class AddRecordForm(forms.ModelForm):
	first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Nombres", "class":"form-control"}), label="")
	last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Apellidos", "class":"form-control"}), label="")
	cedula = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Cédula", "class":"form-control"}), label="")
	fecha_inicio = forms.DateField(required=True, widget=forms.widgets.DateInput(attrs={"name":"Fecha del Pedido", "type":"date", "class":""}), label="Fecha del pedido:")
	fecha_entrega = forms.DateField(required=True, widget=forms.widgets.DateInput(attrs={"type":"date", "class":""}), label="Fecha de entrega del pedido:")
	tipo_lente = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Tipo de lente", "class":"form-control", "maxlength":"1000"}), label="")
	laboratorio = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Laboratorio", "class":"form-control"}), label="")
	precio = forms.FloatField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Precio", "class":"form-control"}), label="")
	add_formula = forms.BooleanField(required=False, widget=forms.widgets.CheckboxInput(attrs={"class":"form-check-input", "id":"add_prescription_check"}), label="Añadir fórmula")
	formula_lente = forms.CharField(required=False, widget=forms.widgets.Textarea(attrs={"placeholder":"Formula", "class":"form-control d-none", "rows":"8", "maxlength":"1000", "id":"prescription_field"}), label="")


	class Meta:
		model = Record
		exclude = ("user",)