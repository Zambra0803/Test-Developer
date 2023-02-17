from django.urls import path
from .views import crear_listar_tarea, eliminar_tarea, editar_tarea

urlpatterns = [
    path('', crear_listar_tarea, name='crear_listar_tarea'),
    path('elimar_tarea/<int:id>/', eliminar_tarea, name='eliminar_tarea'),
    path('editar_tarea/<int:id>/', editar_tarea, name='editar_tarea')
    
]
