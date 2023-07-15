from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
import datetime
from .models import Record

class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))


	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	




# Create Add Record Form
class AddRecordForm(forms.ModelForm):
	first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Nombres", "class":"form-control"}), label="")
	last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Apellidos", "class":"form-control"}), label="")
	cedula = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Cédula", "class":"form-control"}), label="")
	fecha_inicio = forms.DateField(required=True, widget=forms.widgets.DateInput(attrs={"name":"Fecha del Pedido", "type":"date", "class":""}), label="Fecha del pedido:")
	fecha_entrega = forms.DateField(required=True, widget=forms.widgets.DateInput(attrs={"type":"date", "class":""}), label="Fecha de entrega del pedido:")
	tipo_lente = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Tipo de lente", "class":"form-control", "maxlength":"1000"}), label="")
	laboratorio = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Laboratorio", "class":"form-control"}), label="")
	formula_lente = forms.CharField(required=True, widget=forms.widgets.Textarea(attrs={"placeholder":"Formula", "class":"form-control", "rows":"8", "maxlength":"1000"}), label="")
	precio = forms.FloatField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Precio", "class":"form-control"}), label="")


	class Meta:
		model = Record
		exclude = ("user",)