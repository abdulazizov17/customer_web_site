from django.shortcuts import render, get_object_or_404, redirect
from customers.models import Customer
from django.db.models import Q
from customers.forms import CustomerForm
from typing import Optional



def customer_list(request):
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
    }
    return render(request,'customers/home.html', context)


def customer_detail(request, customer_id):
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
def customer_create(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    contex = {
        'form': form
    }
    return render(request, 'customers/add-customer.html', contex)


def customer_update(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    form = CustomerForm(instance=customer)
    if request.method == "POST":

        if request.method == 'POST':
            form = CustomerForm(request.POST, request.FILES, instance=customer)
            if form.is_valid():
                form.save()
                return redirect('customer_detail', customer_id)
    context = {
        'form': form,
        'customers': customer,
        }
    return render(request, 'customers/edit-customer.html', context)

def customer_delete(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    if customer:
        customer.delete()
        return redirect('customer_list')

