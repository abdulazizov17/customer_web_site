from msilib.schema import ListView
from django.shortcuts import get_object_or_404, redirect

from django.shortcuts import render
from django.core.paginator import Paginator
from product.models import Product, AttributeValue
from django.views import View
from product.forms import ProductForm
# Create your views here.


# def product_list(request):
#     products = Product.objects.all()
#     paginator = Paginator(products,3)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     contex = {
#         'products' : page_obj
#     }
#     return render(request,'product/product-list.html',contex)

class ProductListView(View):
    def get(self, request):
        products = Product.objects.all()
        paginator = Paginator(products,3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        contex = {
            'products': page_obj
        }
        return render(request, 'product/product-list.html', contex)

class ProductDetailView(View):
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)

        if request.method == 'POST':
            form = ProductForm(request.POST, instance=product)
            if form.is_valid():
                form.save()
                return redirect('product_detail', customer_id=product.id)
        else:
            form = ProductForm()
        context = {
            'form': form,
            'products': product,
        }
        return render(request, 'product/product-details.html', context)


class ProductCreateView(View):

    def get(self, request):
        form = ProductForm()
    def post(self, request):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
        contex = {
            'form': form
        }
        return render(request, 'product/add.html', contex)


class ProductUpdateView(View):

    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        form = ProductForm(instance=product)
        return render(request, 'product/edit.html', {'form':form, 'product': product})

    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', product_id)


class ProductDeleteView(View):
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        if product:
            product.delete()
            return redirect('product_list')


class ProductGridView(View):
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        paginator = Paginator(product, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        contex = {'product': page_obj}
        return render(request, 'product/product-grid.html', contex)