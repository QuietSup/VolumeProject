from django.urls import path
from pins import views


app_name = 'pins'

urlpatterns = [
    path('explore', views.explore, name='explore'),
    path('pin/<int:pinId>/like/', views.add_like, name='add_like'),
    path('pin/<int:pinId>/unlike/', views.remove_like, name='add_like'),

    path('<slug:slug>/<int:pin_id>', views.show_pin, name='show_pin'),

    path('create_pin', views.create_pin, name='create_pin'),
]