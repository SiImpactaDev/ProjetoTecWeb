from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def avisos(request):
	return render(request, 'avisos.html')

def atividades(request):
	return render(request, 'atividades.html')

def boletim(request):
	return render(request, 'boletim.html')
	
def alterarCadastro(request):
	return render(request, 'alterarCadastro.html')

def exercicios(request):
	return render(request, 'exercicios.html')
	
def entregaPendentes(request):
	return render(request, 'entregaAluno.html')