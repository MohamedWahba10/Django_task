from django.shortcuts import render

def navbar(request):
    return render(request,'navbar/navbar.html')

def about(request):
    return render(request, 'about/index.html')

def products(request):
   
    products = [
        {'name': 'Product 1', 'price': 19.99},
        {'name': 'Product 2', 'price': 29.99},
        
    ]

    return render(request, 'products/products.html', {'myproducts': products})
