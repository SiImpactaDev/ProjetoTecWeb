"""projetoWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from apps.core.views import *
from apps.aluno.views import *

urlpatterns = [
	url(r'^$', index, name='index'),
	url(r'^aluno/avisos/', avisos, name='avisos'),
	url(r'^aluno/atividades/', atividades, name='atividades'),
	url(r'^aluno/boletim/', boletim, name='boletim'),
	url(r'^aluno/alterar-cadastro/', alterarCadastro, name='alterarCadastro'),
	url(r'^aluno/entrega-pendentes', entregaPendentes, name='entregaPendentes'),
    url(r'^aluno/exercicios', exercicios, name='exercicios'),
	url(r'^admin/', admin.site.urls),
]
