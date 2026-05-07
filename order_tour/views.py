from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms 



def update_order_view(request, id):
    order_id = get_object_or_404(models.Orders, id = id)
    if request.method == 'POST':
        form = forms.OrdersForm(request.POST, instance= order_id)
        if form.is_valid():
            form.save()
            return redirect('/orders_list/')
    else:
        form = forms.OrdersForm(instance= order_id) 
    return render(request, 'update_order.html',
    {
    'form': form, 
    'order_id': order_id
    })


def delete_order_view(request, id):
    order_id = get_object_or_404(models.Orders, id=id)
    order_id.delete()
    return redirect('/orders_list/')


def create_order_view(request):
    if request.method == 'POST':
        form = forms.OrdersForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/orders_list/') 
    else:
        form = forms.OrdersForm()
    return render(request, 'create_order.html', {'form': form})

def orders_list_view(request):
    if request.method == 'GET':
        orders = models.Orders.objects.all().order_by('-id')
    return render(request, 'orders_list.html', {'orders': orders})