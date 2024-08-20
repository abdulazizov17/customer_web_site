from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product

# ListView - To display a list of products
class ProductListView(ListView):
    model = Product
    template_name = 'product/product-list.html'
    context_object_name = 'products'
    ordering = ['-id']  # Order by most recently created

# DetailView - To display details of a single product
class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product-details.html'
    context_object_name = 'product'

    def get_object(self):
        product_id = self.kwargs.get("product_id")
        return get_object_or_404(Product, id=product_id)

# CreateView - To create a new product
class ProductCreateView(CreateView):
    model = Product
    template_name = 'product/add.html'
    fields = ['name', 'description', 'price', 'category', 'discount', 'quantity']
    success_url = reverse_lazy('product_list')  # Redirect to product list after creation

# UpdateView - To update an existing product
class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product/edit.html'
    fields = ['name', 'description', 'price', 'category', 'discount', 'quantity']
    success_url = reverse_lazy('product_list')  # Redirect to product list after updating

    def get_object(self):
        product_id = self.kwargs.get("product_id")
        return get_object_or_404(Product, id=product_id)

# DeleteView - To delete an existing product
class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product/product-list.html'
    success_url = reverse_lazy('product_list')  # Redirect to product list after deletion

    def get_object(self):
        product_id = self.kwargs.get("product_id")
        return get_object_or_404(Product, id=product_id)
