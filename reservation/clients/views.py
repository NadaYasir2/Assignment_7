from django.shortcuts import render , reverse
from django.http import HttpResponse , HttpResponseRedirect
from . import forms

product_List = []
def index(request):
    return HttpResponse("<h1> Welcome 😊 </h1>")

def header(request):
    return render(request, 'header.html')

def add (requst):
    return render(requst, 'add.html')


def addproduct(request):
    if request.method == "POST":
        f = forms.ProductForm(request.POST)
        if f.is_valid():
            # Process the form data (e.g., save to database)
            # Redirect to a success page or the same page to display the form again
            product_List.append(f.cleaned_data)
            return HttpResponseRedirect(reverse("Product:addproduct"))  # Redirect to the same page
    else:
        f = forms.ProductForm()  # Instantiate the form for GET request

    # Render the product.html template with the product_List context and the form
    return render(request, "product.html", {"product_List": product_List, 'form': f})