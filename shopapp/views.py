from django.shortcuts import render
from shopapp.models import Product, Category, BussinesData, Promo

# Create your views here.
def index(request):
    shop_data = BussinesData.objects.all().first()
    products = Product.objects.all()
    categories = Category.objects.all()
    promo = Promo.objects.all()


    data = { 'shop_data': shop_data, 'products': products, 'categories': categories, 'promo': promo }

    return render(request, "shopapp/index.html", data)