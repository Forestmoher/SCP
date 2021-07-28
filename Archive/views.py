from django.shortcuts import render, redirect, get_object_or_404
from .forms import ItemForm
from .models import Item, ObjectClass


def home(request):
    return render(request, 'Archive/Archive_home.html')


def create_item(request):
    form = ItemForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('Archive_create')
    context = {'form': form}
    return render(request, 'Archive/Archive_create.html', context)


def items_list(request):
    items = Item.objects.all()
    context = {'items': items}
    return render(request, 'Archive/Archive_items_list.html', context)
