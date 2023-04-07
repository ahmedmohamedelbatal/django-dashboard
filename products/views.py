from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm

@login_required(login_url='login')
def products(request):
  products = Product.objects.all()
  context = {'products': products}
  return render(request, 'products/products.html', context)


@login_required(login_url='login')
def add_product(request):
  if request.method == 'POST':
    form = ProductForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect("/products/")
  else:
    form = ProductForm()
  return render(request, 'products/add_product.html', {'form': form})


@login_required(login_url='login')
def edit_product(request, id):
  product = Product.objects.get(id=id)
  if request.method == 'POST':
    form = ProductForm(request.POST, request.FILES, instance=product)
    if form.is_valid():
      form.save()
      return redirect('/products/')
  else:
    form = ProductForm(instance=product)
  return render(request, 'products/edit_product.html', {'form': form})


def delete_product(request, id):
  delete_product = Product.objects.get(id = id)
  delete_product.delete()
  return redirect('/products/')