from django.shortcuts import render, redirect
from .forms import ItemForm


def home(request):
    return render(request, 'Archive/Archive_home.html')


def create_item(request):
    form = ItemForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('Archive_create')
    context = {'form': form}
    return render(request, 'Archive/Archive_create.html', context)
