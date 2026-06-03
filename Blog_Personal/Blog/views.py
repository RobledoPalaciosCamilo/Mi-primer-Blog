from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Perfil
from .forms import PostForm

# Create your views here.

def lista_posts(request):
    posteos = Post.objects.all().order_by('-fecha_creacion')
    return render(request, 'blog/lista_posts.html', {'lista_de_posteos': posteos})

# READ
def detalle_post(request, post_id):
    # Buscamos el post por su ID
    post = get_object_or_404(Post, id=post_id)

    return render(request, 'blog/detalle_post.html', {'post': post})

# CREATE
@login_required
def crear_post(request):
    # Si el usuario presiona el boton guardar (metodo POST)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() # Guarda en la DB
            return redirect('lista_posts')
    
    # Si el usuario solo entra a la pagina(metodo GET), le mostramos el formulario vacio 
    else:
        form = PostForm()

    return render(request, 'blog/crear_post.html', {'form': form})

# UPDATE
@login_required
def editar_post(request, post_id):
    # 1. buscamos en la DB por id
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        # 2. llenamos el formulario con los nuevos datos, pero actualizamos la instancia
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('detalle_post',post_id=post.id) # volvemos al Post actualizado
    
    else:
        # 3. si es un GET mostramos formulario pre-llenado con datos actuales
        form = PostForm(instance=post)
    
    return render(request, 'blog/editar_post.html', {'form': form, 'post': post})

# DELETE
@login_required
def eliminar_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # 1. para eliminar, la mejor practica de seguridad es a traves de metodo POST
    if request.method == 'POST':
        post.delete() # comando directo del ORM para borrar de la DB
        return redirect('lista_posts')
    
    # 2. si es GET, mostramos una pagina de confirmacion
    return render(request, 'blog/eliminar_post.html', {'post': post})