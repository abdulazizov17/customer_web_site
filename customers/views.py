from django.shortcuts import render, get_object_or_404, redirect
from customers.models import Customer
from django.db.models import Q
from customers.forms import CustomerForm
from django.core.paginator import Paginator
from django.views import View
import csv
import datetime
import json
from django.http import HttpResponse
import openpyxl

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
        # paginator = Paginator(customers, 2)
        # page_number = request.GET.get("page")
        # page_obj = paginator.get_page(page_number)
        search = request.GET.get('q')
        order = request.GET.get('order', 'recent')
        if search:
            customers = Customer.objects.filter(Q(full_name__icontains=search)) | Q(email__icontains=search)
        if order == 'recent':
            customer = Customer.objects.all().order_by('-joined')
        else:
            customer = Customer.objects.all()
        context = {
            'customers': customer,
            'custom':customers
            # 'customer_page': page_obj,
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
        contex = {
            'form':form
        }
        return render(request, 'customers/add-customer.html', contex)

    def post(self, request):
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('customer_list')


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






class ExportData(View):
    def get(self, request):
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        format = request.GET.get('format')
        if format == 'csv':
            meta = Customer._meta
            field_names = [field.name for field in meta.fields]
            response = HttpResponse(content_type='text/csv')

            response['Content-Disposition'] = f'attachment; filename={Customer._meta.object_name}-{date}.csv'
            writer = csv.writer(response)
            writer.writerow(field_names)
            for obj in Customer.objects.all():
                writer.writerow([getattr(obj, field) for field in field_names])


        elif format == 'json':
            response = HttpResponse(content_type='application/json')
            data = list(Customer.objects.all())
            response.write(json.dumps(data, indent=4, default=str))
            response['Content-Disposition'] = f'attachment; filename={Customer._meta.object_name}-{date}.json'




        elif format == 'xlsx':
            response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = f'attachment; filename="{Customer._meta.object_name}-{date}.xlsx"'
            workbook = openpyxl.Workbook()
            worksheet = workbook.active
            worksheet.title = 'Customers'
            header = ['ID', 'Full Name', 'Email', 'Addres', 'Slug', 'Phone Number']

            worksheet.append(header)
            customers = Customer.objects.all()
            for obj in customers:
                worksheet.append([obj.id, obj.full_name, obj.email, obj.address, obj.slug, obj.phone])

            workbook.save(response)
            return response

        # header

        else:
            response = HttpResponse(status=404)
            response.content = 'Bad Request'

        return response