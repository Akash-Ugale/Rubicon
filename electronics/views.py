from django.shortcuts import render,HttpResponse
from .models import Product,Customer
from .forms import ProductForm
# Create your views here.
def home(request):
    data = None
    data1 = None
    if request.method == "POST":
        form = ProductForm(request.POST)  # data insert through form
        if form.is_valid():    
            form.save()
        data = Product.objects.all()
    else:
        form = ProductForm()
        data = Product.objects.all()
        data1 = Customer.objects.all()
    
        
    return render(request, 'electronics/home.html',{'data':data,'data1':data1,'form':form})


