from django.shortcuts import render

from my_app.models import Product


# Create your views here.

def product_list(request):
    products = Product.objects.all()
    context = {
        "products_list": products,
    }
    return render(request, "product_list.html", context)

def get_product_by_id(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        "product": product,
    }
    return render(request, "product_details.html", context)
