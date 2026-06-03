from django.urls import path
from . import views

urlpatterns = [
    # Ruta vacia, muestra la lista de posts
    path('', views.lista_posts, name='lista_posts'),
    
    # Ruta /crear/: Muestra el formulario
    path('crear/', views.crear_post, name='crear_post'),

    # Ruta para ver el Post completo (detalle)
    path('posts/<int:post_id>/', views.detalle_post, name='detalle_post'),

    # Ruta para modificar Post (Update)
    path('post/<int:post_id>/editar/', views.editar_post, name='editar_post'),

    # Ruta para eliminar Post (Delete)
    path('post/<int:post_id>/eliminar/', views.eliminar_post, name='eliminar_post'),

    # Ruta para el registro de nuevos usuarios
    path('registro/', views.registro, name='registro'), 

]