from django.shortcuts import render
from django.http import HttpResponse
from . import forms # . means the current dircetory
from first_app.forms import NewUserform
# Create your views here.

def form_name_view(request):
    form = forms.loginname()
    return render(request,'first_app/index.html',{'form':form})

def cart(request):
    from first_app.models import Users,category,pizzaselection
    #pizzamenu = pizzaselection.objects.order_by('pid')
    #pizzavalue = request.POST.get('1')
    #pizzamenu = pizzaselection.objects.values('pid')
    #for pizzai in pizzamenu:
    #        if pizzai == '1':
                #finalval = pizzaselection.objects.values('pizzavalue')
    #            pizzalist = {'pizza_selection':pizzamenu}
    #return render(request,'first_app/cart.html')#,context=pizzalist)
    return HttpResponse("Successfully ordered placed.")

def logout(request):
    return render(request,'first_app/index.html')

def welcome(request):
    form = forms.loginname()
    return render(request,'first_app/welcome.html')

def menu(request):
    from first_app.models import Users,category,pizzaselection
    pizzamenu = pizzaselection.objects.order_by('pid')
    pizzalist = {'pizza_selection':pizzamenu}
    return render(request,'first_app/menu.html',context=pizzalist)

def signup(request):

    registered = False
    form = NewUserform()

    if request.method == "POST":

        form = NewUserform(request.POST)

        if form.is_valid():
            form.save(commit=True)
            registered = True
            render(request,'first_app/form_name_view')
        else:
            print("Error Form Invalid Check Your Id and Password")

    return render(request,'first_app/signup.html',{'form':form,'registered':registered})
