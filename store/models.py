from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    pub_date = models.DateTimeField("date published", default=timezone.now)

    def __str__(self):
        return self.name
    
class Compra(models.Model):
    produto = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    data = models.DateTimeField(default=timezone.now)
    # Você pode adicionar mais campos, como usuário, valor total, etc.
    def __str__(self):
        return f"Compra de {self.quantidade}x {self.produto.name} em {self.data.strftime('%d/%m/%Y %H:%M')}"