from django.shortcuts import render
from .models import BreakFast , Lunch , Dinner
from .forms import OrdersForm

# Create your views here.
def home(request):
    return render(request , 'index.html')



def breakfast_meals(request):
    breakfast_info = BreakFast.objects.all()
    context = {'meals' : breakfast_info}
    return render(request , 'breakfast.html' , context)

def breakfast_details(request , id):
    breakfast_details = BreakFast.objects.get(id=id)
    if request.method == 'POST':
        form = OrdersForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.order_name = breakfast_details
            myform.save()
    else :
        form = OrdersForm()

    context = { 'mealdetail' : breakfast_details  , 'form' : form }
    return render(request , 'breakfast_detail.html' , context)




def lunch_meals(request):
    lunch_info = Lunch.objects.all()
    context = {'lunch_meals' : lunch_info}
    return render(request , 'lunch.html' , context )



def lunch_details(request , id):
    lunch_details = Lunch.objects.get(id=id)
    if request.method == 'POST':
        form = OrdersForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.order_name_lunch = lunch_details
            myform.save()
    else :
        form = OrdersForm()
    context = {'lunchdetail' : lunch_details , 'form' : form }
    return render(request , 'lunch_detail.html' , context)




def dinner_meals(request):
    dinner_info = Dinner.objects.all()
    context = {'dinner_meals' : dinner_info}
    return render(request , 'dinner.html' , context )

def dinner_details(request , id):
    dinner_details = Dinner.objects.get(id=id)
    if request.method == 'POST':
        form = OrdersForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.order_name_dinner = dinner_details
            myform.save()
    else :
        form = OrdersForm()
    context = {'dinnerdetail' : dinner_details , 'form' : form}
    return render(request , 'dinner_detail.html' , context)
