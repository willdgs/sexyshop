from django.db import models # type: ignore

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=200)  # Corrigido o erro de sintaxe
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    estoque = models.IntegerField()  # Corrigido o erro do campo estoque
    imagem = models.ImageField(upload_to='produtos/')  # Adicionado campo de imagem
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
