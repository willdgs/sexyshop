from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('categoria/<int:categoria_id>/', views.produtos_por_categoria, name='produtos_por_categoria'),
    path('produto/<int:produto_id>/', views.detalhe_produto, name='detalhe_produto'),
]
