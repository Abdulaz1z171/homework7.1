from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from app.models import Product,Customer
from django.core.paginator import Paginator
from app.forms import CustomerModelForm
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q

# Create your views here.

def index(request):
    products = Product.objects.all()
    paginator = Paginator(products,3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj':page_obj,

    }
    return render(request, 'app/index.html',context)


def detail(request,pk):
    product = Product.objects.get(id=pk)


    context = {
        'product': product,

    }
    return render(request, 'app/e-commerce/product/product-details.html',context)
    
def product_list(request):
    products = Product.objects.all()
    paginator = Paginator(products, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,

    }
    return render(request,'app/e-commerce/product/product-list.html',context)

def product_details(request):
    return render(request,'app/e-commerce/product/product-details.html')

def product_grid(request):
    return render(request,'app/e-commerce/product/product-grid.html')


def customer(request):
    customers = Customer.objects.all().order_by('-created_at')
    search_query = request.GET.get('search')
    paginator = Paginator(customers, 7)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if search_query:
        page_obj = customers.filter(Q(name__icontains=search_query) | Q(email__icontains=search_query))

    context = {
        'page_obj': page_obj,


    }
    return render(request,'app/e-commerce/customers.html',context)

def customer_details(request,pk):
    customer = Customer.objects.get(id=pk)
    context = {
        'customer': customer
    }
    return render(request,'app/e-commerce/customer-details.html',context)





@login_required()
def customer_add(request):
    customers = Customer.objects.all()
    if request.method == 'POST':
        form = CustomerModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer')
    else:
        form = CustomerModelForm()
    context = {
        'customers': customers,
        'form':form,
    }
    return render(request, 'app/add-customer.html',context)

@login_required()
def delete_customer(request, pk):
    customer = Customer.objects.filter(id=pk).first()
    if customer:
        customer.delete()
        return redirect('customer')

    context = {
        'customer':customer,
    }
    return render('app/e-commerce/customers.html', context)

@login_required()
def edit_customer(request, pk):
    customer = Customer.objects.get(id=pk)
    form = CustomerModelForm(instance=customer)
    if request.method == 'POST':
        form = CustomerModelForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer')

    context = {
        'form': form,
        'customer': customer,
    }
    return render(request, 'app/update.html', context)


def to_login(request):
    username = request.POST["username"]
    email = request.POST["email"]
    password = request.POST["password"]
    # user = authenticate(request, username=username, password=password,email=email)
    my_user = User.objects.create_user(username,email,password)
    my_user.save()
    messages.success(request, 'You have successfully logged')
    return redirect('index')

def logout(request):
    return render(request,'app/simple/logout.html')

def register(request):
    return render(request,'app/simple/register.html')
