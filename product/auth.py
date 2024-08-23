from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import FormView
from product.authentication_form import AuthenticationForm
from product.forms import SendingEmailForm
from customers.forms import LoginForm,RegisterForm
from customers.templates.customers import registrat

# def login_page(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data.get('email')
#             password = form.cleaned_data.get('password')
#             user = authenticate(request,email=email,password=password)
#             if user:
#                 login(request, user)
#                 return redirect('customer_list')
#             else:
#                 messages.error(request, 'Invalid username or password')
#     else:
#         form = LoginForm()
#     return render(request,'product/registrat/login.html',{'form':form})


class LoginPage(LoginView):
    redirect_authenticated_user = True
    form_class = AuthenticationForm
    template_name = 'customers/registrat/login.html'

    def get_success_url(self):
        return reverse_lazy('customers')

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid email or password')
        return self.render_to_response(self.get_context_data(form=form))


# def register_page(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             # password = form.cleaned_data.get('password')
#             # user.is_active = True
#             # user.is_superuser = True
#             # user.is_staff = True
#             # user.set_password(password)
#             user.save()
#             login(request, user)
#             return redirect('customer_list')
#         else:
#             messages.error(request, 'Invalid username or password')
#     else:
#         form = RegisterForm()
#
#     return render(request, 'product/registrat/register.html',{'form':form})


class RegisterPage(FormView):
    template_name = 'customers/registrat/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('customers')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        send_mail(
            'User Succesfully Registered',
            'Test body',
            [user.email],
            fail_silently=False
        )
        login(self.request, user,backend='django.contrib.auth.backends.ModelBackend')
        return super().form_valid(form)

def logout_page(request):
    if request.method == 'POST':
        logout(request)
        return redirect('customer_list')

class LogoutPage(LogoutView):
    next_page = reverse_lazy('login')  # Redirects to the login page after logout

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, 'You have successfully logged out.')
        return super().dispatch(request, *args, **kwargs)


class SendingEmail(View):
    sent = False

    def get(self, request, *args, **kwargs):
        form = SendingEmailForm()
        context = {
            'form': form,
            'sent': self.sent
        }
        return render(request, 'product/send-email.html', context)

    def post(self, request, *args, **kwargs):
        form = SendingEmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            recipient_list = form.cleaned_data['recipient_list']
            send_mail(
                subject,
                message,
                recipient_list,
                fail_silently=False
            )
            self.sent = True
            context = {
                'form': form,
                'sent': self.sent
            }
            return render(request, 'product/send-email.html', context)

