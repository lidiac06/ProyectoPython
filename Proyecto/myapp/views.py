from django.shortcuts import redirect, render
from .forms import ReviewForm
from .models import Usuario, Libro, Review, Post

# Create your views here.


def listar_libros(request):
    libros = Libro.objects.all()
    return render(request, 'blog/post_list.html', context={"libros":libros})

def post_create(request):
    if request.method == "POST":
        form = ReviewForm(request.Post)
        if form.is_valid():
            form.save()
            return redirect("blog/post_list")


