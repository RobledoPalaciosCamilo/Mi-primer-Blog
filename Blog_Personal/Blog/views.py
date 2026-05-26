from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Perfil
from .forms import PostForm

# Create your views here.

def lista_posts(request):
    posteos = Post.objects.all().order_by('-fecha_creacion')
    return render(request, 'blog/lista_posts.html', {'lista_de_posteos': posteos})

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

def detalle_post(request, post_id):
    # Buscamos el post por su ID
    post = get_object_or_404(Post, id=post_id)

    return render(request, 'blog/detalle_post.html', {'post': post})