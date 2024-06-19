from django.shortcuts import render # type: ignore
from .models import Product

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request,'PLP_Ecommerce/product_list.html',context)
