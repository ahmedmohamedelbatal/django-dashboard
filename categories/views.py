from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Category
from .forms import CategoryForm

@login_required(login_url='login')
def categories(request):
  categories = Category.objects.all()
  return render(request, 'categories/categories.html', {'categories': categories})


@login_required(login_url='login')
def add_category(request):
  if request.method == 'POST':
    form = CategoryForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect("/categories/")
  else:
    form = CategoryForm()
  return render(request, 'categories/add_category.html', {'form': form})


@login_required(login_url='login')
def edit_category(request, id):
  product = Category.objects.get(id=id)
  if request.method == 'POST':
    form = CategoryForm(request.POST, request.FILES, instance=product)
    if form.is_valid():
      form.save()
      return redirect('/categories/')
  else:
      form = CategoryForm(instance=product)
  return render(request, 'categories/edit_category.html', {'form': form})


def delete_category(request, id):
  delete_category = Category.objects.get(id = id)
  delete_category.delete()
  return redirect('/categories/')