from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import RegisterForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.views import LoginView

# Landing page - Login
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'  # Make sure your login.html is here

# Product list view
def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

# Product detail view
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/product_detail.html', {'product': product})

# Registration view
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('product_list')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})
