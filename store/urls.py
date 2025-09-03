
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.product_list, name="product_list"),
    path("<int:product_id>/", views.product_detail, name="product_detail"),
    path("carrinho/<int:product_id>/", views.carrinho, name="carrinho"),
    path("concluir_compra/<int:product_id>/", views.concluir_compra, name="concluir_compra"),
]