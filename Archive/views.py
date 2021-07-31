from django.shortcuts import render, redirect, get_object_or_404
from .forms import ItemForm
from .models import Item, ObjectClass
import http.client
import json


def home(request):
    return render(request, 'Archive/Archive_home.html')


def create_item(request):
    form = ItemForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            item_number = form.cleaned_data['item_number']
            request.session['item_number'] = item_number
            request.session.modified = True
            form.save()
            return redirect('Archive_add_image')
    context = {'form': form}
    return render(request, 'Archive/Archive_create.html', context)


def image_search(request):
    conn = http.client.HTTPSConnection("contextualwebsearch-websearch-v1.p.rapidapi.com")

    headers = {
        'x-rapidapi-key': "8d08802391msh53283cf56cf01e7p13f93bjsn5ffc452d06e6",
        'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com"
    }
    item_number = request.session['item_number']

    conn.request("GET", "/api/Search/ImageSearchAPI?q=SCP-{}&pageNumber=1&pageSize=10&autoCorrect=true".format(item_number),
                 headers=headers)

    res = conn.getresponse()
    data = res.read().decode("utf-8")
    json_data = json.loads(data)

    image_list = []
    for key in json_data['value']:
        image_list.append(key['url'])

    context = {'image_list': image_list}
    return render(request, 'Archive/Archive_add_image.html', context)


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
               'description': item.item_description,
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


