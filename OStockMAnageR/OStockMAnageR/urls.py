"""OStockMAnageR URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from usuarios import views as VU

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', VU.pagina_inicial, name="pagina_inicial"),
    path('login/', VU.login_sistema, name="logar"),
    path('registrar_empresa/', VU.registrar_empresa, name="registrar_empresa"),
    path('recuperar_senha/', VU.recuperar_senha, name="recuperar_senha"),
    path('atualizar_senha/empresa/<int:perfil_id>/<str:numeracao>', VU.atualizar_senha_empresa, name="atualizar_senha"),
    path('atualizar_senha/funcionario/<int:perfil_id>/<str:numeracao>', VU.atualizar_senha_funcionario, name="atualizar_senha_funcionario"),
]
