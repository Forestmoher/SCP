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


def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    context = {'number': item.item_number,
               'pk': item.pk,
               'object_class': item.object_class,
               'containment': item.containment_procedure,
               'name': item.code_name,
               'image': item.item_image
               }
    return render(request, 'Archive/Archive_item_detail.html', context)


def object_class_list(request):
    objects = ObjectClass.objects.all()
    context = {'objects': objects}
    return render(request, 'Archive/Archive_object_classes.html', context)


def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('Archive_items_list')
    context = {'item': item}
    return render(request, 'Archive/Archive_delete_item.html', context)


def update_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    form = ItemForm(request.POST or None, instance=item)
    context = {'form': form, 'item': item}
    if form.is_valid():
        form.save()
        return redirect('Archive_item_detail', item.pk)
    return render(request, 'Archive/Archive_update_item.html', context)

