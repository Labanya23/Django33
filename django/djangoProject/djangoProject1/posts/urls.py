from django.urls import path
form . import views

urlpatterns=[
    path(''),views.add_product,name='add_product'),
    path('update-product/<int:p-id>',views.update_product,name='update-product'),
]