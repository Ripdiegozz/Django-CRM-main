from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import SignUpForm, AddRecordForm
from .models import Record
from .filters import RecordFilter

def home(request):
	records = Record.objects.all()
	# Filter
	myFilter = RecordFilter(request.GET, queryset=records)
	records = myFilter.qs
	# Pagination
	page_number = request.GET.get('page', 1)
	paginator = Paginator(records, 10)

	try:
		regitros = paginator.page(page_number)
	except PageNotAnInteger:
		regitros = paginator.page(1)
	except EmptyPage:
		regitros = paginator.page(paginator.num_pages)

	# Check to see if logging in
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		# Authenticate
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "Haz iniciado sesión!")
			return redirect('home')
		else:
			messages.success(request, "Hubo un error iniciando sesión, intenta de nuevo...")
			return redirect('home')
	else:
		return render(request, 'home.html', {'records':regitros, 'myFilter':myFilter})


def logout_user(request):
	logout(request)
	messages.success(request, "Haz cerrado sesión...")
	return redirect('home')


def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "Te haz registrado satisfactoriamente! Bienvenido!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})


def customer_record(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		customer_record = Record.objects.get(id=pk)
		return render(request, 'record.html', {'customer_record':customer_record})
	else:
		messages.success(request, "Necesitas iniciar sesión para ver esta página...")
		return redirect('home')

def customer_record_formula(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		customer_record = Record.objects.get(id=pk)
		customer_formula = customer_record.formula_lente.replace('\n', '<br>')
		return render(request, 'formula_record.html', {'customer_record':customer_record, 'customer_formula':customer_formula })
	else:
		messages.success(request, "Necesitas iniciar sesión para ver esta página...")
		return redirect('home')


def delete_record(request, pk):
	if request.user.is_authenticated:
		delete_it = Record.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Registro eliminado correctamente...")
		return redirect('home')
	else:
		messages.success(request, "Necesitas iniciar sesión para hacer eso...")
		return redirect('home')


def add_record(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Registro añadido!")
				return redirect('home')
		return render(request, 'add_record.html', {'form':form})
	else:
		messages.success(request, "Necesitas iniciar sesión...")
		return redirect('home')


def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "El registro ha sido actualizado!")
			return redirect('home')
		return render(request, 'update_record.html', {'form':form})
	else:
		messages.success(request, "Necesitas iniciar sesión...")
		return redirect('home')
