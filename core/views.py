from django.shortcuts import render,redirect,get_object_or_404
from .models import Trabalhador
from .forms import TrabalhadorForm

# Create your views here.

def home(request):
    return render(request, 'home.html')


def cadastrar(request):
    form = TrabalhadorForm()
    contexto ={'form':form}
    if request.method == 'POST':
        form = TrabalhadorForm(request.POST or None)
        if form.is_valid():
            form.save()
            print(form)
            form = TrabalhadorForm
    return render(request, 'cadastrar.html',contexto)


def update(request, id):
    obj = get_object_or_404(Trabalhador, id=id)
    form = TrabalhadorForm(instance=obj)
    contexto ={'form':form}
    if request.method == 'POST':
        form = TrabalhadorForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('listar')
    return render(request, 'update.html',contexto)

def listar(request):
    obj = Trabalhador.objects.all()
    contexto={'trabalhador':obj}
    return render(request, 'listar.html',contexto)

def apagar(request, id):
    obj = get_object_or_404(Trabalhador, id=id)
    obj.delete()

