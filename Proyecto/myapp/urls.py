from django.urls import path
from Proyecto.myapp.views import listar_libros, post_create



urlpatterns = [
    path('post_list', listar_libros, name="listar_libros"),



   
]