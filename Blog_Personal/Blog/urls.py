from django.urls import path
from . import views

urlpatterns = [
    # Ruta vacia, muestra la lista de posts
    path('', views.lista_posts, name='lista_posts'),
    
    # Ruta /crear/: Muestra el formulario
    path('crear/', views.crear_post, name='crear_post'),
    path('posts/<int:post_id>/', views.detalle_post, name='detalle_post'),
]