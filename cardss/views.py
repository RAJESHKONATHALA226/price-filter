from django.shortcuts import render
from .models import product
from .forms import choiceform
# Create your views here.

def visited(request):
    products=product.objects.all()
    fm=choiceform()
    citys=products

    if request.method == "POST":
        fm=choiceform(request.POST)
        if fm.is_valid():
            st=fm.cleaned_data['choicefile']
            if st=="low":
                citys=products.order_by('pricess')
            elif st=="high":
                citys=products.order_by('-pricess')
            else:
                citys=products
    return render(request,"index.html",{"form":fm,"const":citys})
