from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
def concluir_compra(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    quantity = request.POST.get("quantity") or 1
    try:
        quantity = int(quantity)
    except (TypeError, ValueError):
        quantity = 1
    # Atualiza o estoque
    if product.stock >= quantity:
        product.stock -= quantity
        product.save()
    return render(request, "store/compra_realizada.html")
from django.shortcuts import render, get_object_or_404
from .models import Product

def product_list(request):
    latest_product_list = Product.objects.order_by("-pub_date")[:5]
    context = {"latest_product_list": latest_product_list}
    return render(request, "store/index.html", context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, "store/detail.html", {"product": product})

def carrinho(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    carrinho_vazio = False
    # Tenta obter a quantidade do POST ou GET
    quantity = request.POST.get("quantity") or request.GET.get("quantity") or 1
    try:
        quantity = int(quantity)
    except (TypeError, ValueError):
        quantity = 1
    if request.method == "POST" and request.POST.get("remove") == "1":
        product = None
        carrinho_vazio = True
    context = {"product": product, "quantity": quantity, "carrinho_vazio": carrinho_vazio}
    return render(request, "store/carrinho.html", context)