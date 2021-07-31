from django.urls import path
from Archive import views

urlpatterns = [
    path('', views.home, name='Archive_home'),
    path('create', views.create_item, name='Archive_create'),
    path('list', views.items_list, name='Archive_items_list'),
    path('classList', views.object_class_list, name='Archive_object_classes'),
    path('details/<int:pk>', views.item_detail, name='Archive_item_detail'),
    path('delete/<int:pk>', views.delete_item, name='Archive_delete_item'),
    path('update/<int:pk>', views.update_item, name='Archive_update_item'),
    path('addImage', views.image_search, name='Archive_add_image'),
]

