from django.urls import path
from . import views

urlpatterns = [
    path('orders_list/', views.orders_list_view, name='or_list'),
    path('orders_list/<int:id>/delete/', views.delete_order_view, name='del_order'),
    path('orders_list/<int:id>/update/', views.update_order_view, name='upd_order'),
    path('create_order/', views.create_order_view, name='cr_order'),
]

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
