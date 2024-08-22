from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Product

class ProductListView(ListView):
    model = Product
    template_name = 'product/product-list.html'
    context_object_name = 'products'
    ordering = ['-id']

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product-details.html'
    context_object_name = 'product'

    def get_object(self):
        product_id = self.kwargs.get("product_id")
        return get_object_or_404(Product, id=product_id)

class ProductCreateView(CreateView):
    model = Product
    template_name = 'product/add.html'
    fields = ['name', 'description', 'price', 'category', 'discount', 'quantity']
    success_url = reverse_lazy('product_list')

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product/edit.html'
    fields = ['name', 'description', 'price', 'category', 'discount', 'quantity']
    success_url = reverse_lazy('product_list')

    def get_object(self):
        product_id = self.kwargs.get("product_id")
        return get_object_or_404(Product, id=product_id)

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product/product-list.html'
    success_url = reverse_lazy('product_list')

    def get_object(self):
        product_id = self.kwargs.get("product_id")
        return get_object_or_404(Product, id=product_id)

class ProductListTemplateView(TemplateView):
    template_name = 'product/product-list.html'

    def get_context_data(self, **kwargs):
        contex = super(ProductListTemplateView, self).get_context_data(**kwargs)
        products = Product.objects.all()
        # paginator = Paginator(products, 2)
        # page_number = self.request.GET.get("page")
        # page_obj = paginator.page(page_number)
        # contex['products'] = page_obj
        # return contex
        contex['products'] = products
        return contex

