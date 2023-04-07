from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from products.models import Product
from accounts.models import Profile

@login_required(login_url='login')
def index(request):
  products = Product.objects.all()
  products_count = Product.objects.all().count()
  
  profiles = Profile.objects.all()
  profiles_count = Profile.objects.all().count()
  
  context = {'products': products, 'products_count': products_count, 'profiles': profiles, 'profiles_count': profiles_count}
  return render(request, 'index.html', context)