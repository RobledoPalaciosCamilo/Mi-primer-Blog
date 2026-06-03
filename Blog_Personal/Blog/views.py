from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post
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
            # Crea el bojeto en la memoria pero PAUSA el guardado en la base de datos
            nuevo_post = form.save(commit=False)
            # Inyectamos el usuario que tiene la sesion iniciada actualmente
            nuevo_post.autor = request.user
            # Ahora que tiene autor, damos luz verde para guardar
            nuevo_post.save()
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

    # 2. Bloqueo de seguridad
    if post.autor != request.user:
        messages.error(request, '⚠️ Acceso denegado: No puedes editar un posteo que le pertenece a otro usuario.')
        # si es un intruso lo mandamos al inicio
        return redirect('lista_posts')

    if request.method == 'POST':
        # 3. llenamos el formulario con los nuevos datos, pero actualizamos la instancia
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('detalle_post',post_id=post.id) # volvemos al Post actualizado
    
    else:
        # 4. si es un GET mostramos formulario pre-llenado con datos actuales
        form = PostForm(instance=post)
    
    return render(request, 'blog/editar_post.html', {'form': form, 'post': post})

# DELETE
@login_required
def eliminar_post(request, post_id):
    # 1. Buscamos en la DB por id
    post = get_object_or_404(Post, id=post_id)

    # 2. Bloqueo de seguridad
    if post.autor != request.user:
        messages.error(request, '⚠️ Acceso denegado: No puedes eliminar un posteo que no te pertenece.')
        return redirect('lista_posts')

    # 3. para eliminar, la mejor practica de seguridad es a traves de metodo POST
    if request.method == 'POST':
        post.delete() # comando directo del ORM para borrar de la DB
        return redirect('lista_posts')
    
    # 4. si es GET, mostramos una pagina de confirmacion
    return render(request, 'blog/eliminar_post.html', {'post': post})

#VISTA DE REGISTRO DE USUARIO NORMAL
def registro(request):
    if request.method == 'POST':
        # instanciamos el formulario nativo con los datos que ingresó el usuario
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
    else:
        # Si entra por primera vez, le  mostramos el formulario vacio
        form = UserCreationForm()
    
    return render(request, 'registration/registro.html', {'form': form})
