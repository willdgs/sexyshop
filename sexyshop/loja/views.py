from django.shortcuts import render, get_object_or_404  # type: ignore
from .models import Produto, Categoria

# Página inicial com todos os produtos
def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'loja/lista_produtos.html', {'produtos': produtos})

# Produtos filtrados por categoria
def produtos_por_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    produtos = Produto.objects.filter(categoria=categoria)
    return render(request, 'loja/produtos_por_categoria.html', {
        'categoria': categoria,
        'produtos': produtos
    })

# Detalhes de um único produto
def detalhe_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    return render(request, 'loja/detalhe_produto.html', {'produto': produto})
# Página inicial
def home(request):
    categorias = Categoria.objects.all()
    produtos = Produto.objects.all()[:6]  # Produtos em destaque
    return render(request, 'loja/home.html', {
        'categorias': categorias,
        'produtos': produtos
    })
