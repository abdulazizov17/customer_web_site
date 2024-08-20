from django.shortcuts import render, get_object_or_404, redirect
from customers.models import Customer
from django.db.models import Q
from customers.forms import CustomerForm
from django.core.paginator import Paginator
from django.views import View

# def customer_list(request):
#     customers = Customer.objects.all()
#     paginator = Paginator(customers, 2)
#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)
#     search = request.GET.get('q')
#     order = request.GET.get('order', 'recent')
#     if search:
#         customer = Customer.objects.filter(Q(full_name__icontains=search)) | Q(email__icontains=search)
#     if order == 'recent':
#         customer = Customer.objects.all().order_by('-joined')
#     else:
#         customer = Customer.objects.all()
#     context = {
#         'customers': customer,
#         'customer_page': page_obj,
#     }
#     return render(request,'customers/home.html', context)

class CustomerListView(View):
    def get(self, request):
        customers = Customer.objects.all()
        paginator = Paginator(customers, 2)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        search = request.GET.get('q')
        order = request.GET.get('order', 'recent')
        if search:
            customer = Customer.objects.filter(Q(full_name__icontains=search)) | Q(email__icontains=search)
        if order == 'recent':
            customer = Customer.objects.all().order_by('-joined')
        else:
            customer = Customer.objects.all()
        context = {
            'customers': customer,
            'customer_page': page_obj,
        }
        return render(request, 'customers/home.html', context)

# def customer_detail(request, customer_id):
#     customer = get_object_or_404(Customer, id=customer_id)
#
#     if request.method == 'POST':
#         form = CustomerForm(request.POST, instance=customer)
#         if form.is_valid():
#             form.save()
#             return redirect('customer_detail', customer_id=customer.id)
#     else:
#         form = CustomerForm()
#     context = {
#         'form': form,
#         'customer': customer,
#     }
#     return render(request, 'customers/customer-detail.html', context)

class CustomerDetailView(View):
    def get(self, request, customer_id):
        customer = get_object_or_404(Customer, id=customer_id)

        if request.method == 'POST':
            form = CustomerForm(request.POST, instance=customer)
            if form.is_valid():
                form.save()
                return redirect('customer_detail', customer_id=customer.id)
        else:
            form = CustomerForm()
        context = {
            'form': form,
            'customer': customer,
        }
        return render(request, 'customers/customer-detail.html', context)


# def customer_create(request):
#     form = CustomerForm()
#     if request.method == 'POST':
#         form = CustomerForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('customer_list')
#     contex = {
#         'form': form
#     }
#     return render(request, 'customers/add.html', contex)

class CustomerCreateView(View):

    def get(self, request):
        form = CustomerForm()
    def post(self, request):
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
        contex = {
            'form': form
        }
        return render(request, 'customers/add-customer.html', contex)


# def customer_update(request, customer_id):
#     customer = get_object_or_404(Customer, id=customer_id)
#     form = CustomerForm(instance=customer)
#     if request.method == "POST":
#
#         if request.method == 'POST':
#             form = CustomerForm(request.POST, request.FILES, instance=customer)
#             if form.is_valid():
#                 form.save()
#                 return redirect('customer_detail', customer_id)
#     context = {
#         'form': form,
#         'customers': customer,
#         }
#     return render(request, 'customers/edit.html', context)

class CustomerUpdateView(View):

    def get(self, request, customer_id):
        customer = get_object_or_404(Customer, id=customer_id)
        form = CustomerForm(instance=customer)
        return render(request, 'customers/edit-customer.html', {'form':form, 'customer': customer})

    def post(self, request, customer_id):
        customer = get_object_or_404(Customer, id=customer_id)
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_detail', customer_id)



# def customer_delete(request, customer_id):
#     customer = get_object_or_404(Customer, id=customer_id)
#     if customer:
#         customer.delete()
#         return redirect('customer_list')

class CustomerDeleteView(View):
    def get(self, request, customer_id):
        customer = get_object_or_404(Customer, id=customer_id)
        if customer:
            customer.delete()
            return redirect('customer_list')
