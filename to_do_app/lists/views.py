from .models import List
from .forms import TodoForm

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from django.views.generic import UpdateView



def index(request):
    item_list = List.objects.order_by('-date')

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        
    form = TodoForm()

    page = {
        'forms' : form,
        'list' : item_list,
        'title' : 'TO-DO LIST',
    }
    return render(request, 'list.html', page)

def remove(request, item_id):
    item = List.objects.get(id = item_id)
    item.delete()
    messages.info(request, 'item removed!!')
    return redirect('index')



def update_status(request, item_id):
    item = List.objects.get(id= item_id)
    item.complete = not item.complete
    item.save()
    messages.info(request, 'status updated!!')
    return redirect('index')


def edit(request, pk):
    item_list = get_object_or_404(List, pk=pk)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=item_list)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TodoForm(instance=item_list)

    return render(request, 'edit.html', {'form':form})
