# sexyshop/urls.py
from django.contrib import admin
from django.urls import path
from loja import views  # Importe as views do seu app 'loja'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Rota para a página inicial
    # Outras rotas que você tenha criado
]

