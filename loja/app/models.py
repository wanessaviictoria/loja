from django.db import models

class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_categoria
    
class Marca(models.Model):
    nome_marca = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_marca
    
class Produto(models.Model):
    nome_produto = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca,on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    preco = models.PositiveIntegerField()
    disponibilidade = models.BooleanField(default=True)

    def __str__(self):
        return f"Categoria: {self.categoria}, Marca: {self.marca }"
