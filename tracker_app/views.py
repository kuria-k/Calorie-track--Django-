from django.shortcuts import render, redirect, get_object_or_404
from .models import FoodItem
from .forms import FoodItemForm

def home(request):
    items = FoodItem.objects.all()
    total_calories = sum(item.calories for item in items)
    return render(request, 'tracker_app/home.html', {
        'items': items,
        'total_calories': total_calories
    })

def add_food(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        calories = request.POST.get('calories')
        meal_type = request.POST.get('meal_type')
        date = request.POST.get('date') 

        FoodItem.objects.create(
            name=name,
            calories=calories,
            meal_type=meal_type,
            date=date  
        )
        # return redirect('home')
    return render(request, 'tracker_app/input.html')

def view_food(request):
    items = FoodItem.objects.all()
    total_calories = sum(item.calories for item in items)
    return render(request, 'tracker_app/data.html', {
        'items': items,
        'total_calories': total_calories
    })


def delete_food(request, item_id):
    item = get_object_or_404(FoodItem, id=item_id)
    item.delete()
    return redirect('data')

# def edit_food(request, item_id):
#     item = get_object_or_404(FoodItem, id=item_id)
#     if request.method == 'POST':
#         form = FoodItemForm(request.POST, instance=item)
#         if form.is_valid():
#             form.save()
#             return redirect('view_food')
#     else:
#         form = FoodItemForm(instance=item)
#     return render(request, 'tracker_app/edit.html', {'form': form, 'item': item})




