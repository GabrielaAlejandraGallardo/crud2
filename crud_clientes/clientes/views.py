from django.shortcuts import render,redirect
from  django.http import HttpResponse
from .models import Clientes
from .forms  import ClientesForm

# Create your views here.
def inicio(request):
    return render(request,'paginas_base/inicio.html')
def nosotros(request):
    return render(request,'paginas_base/nosotros.html')

def lista(request):
    clientes=Clientes.objects.all()
    #print(clientes)
    return render(request,'Crud/listado.html',{'clientes':clientes})

def crear(request):
    formulario=ClientesForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('lista')
    return render(request,'Crud/crear.html',{'formulario':formulario})

def eliminar(request, id):
    bc=Clientes.objects.get(id=id)
    bc.delete()
    return redirect('lista')

def editar(request, id):
    bc=Clientes.objects.get(id=id)
    formulario=ClientesForm(request.POST or None, request.FILES or None, instance=bc)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('lista')
    return render(request,'Crud/editar.html',{'formulario':formulario})

    
        
    
