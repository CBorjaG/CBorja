from django.shortcuts import render, redirect
from .models import Cliente, Destino, Transporte, Nacionalidad
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    
    clientes = Cliente.objects.all()
    
    return render(request, "core/home.html", {'clientes': clientes})

def galeria(request):
    return render(request, 'core/galeria.html')

def formulario(request):
    destino = Destino.objects.all()
    transporte = Transporte.objects.all()
    nacionalidad = Nacionalidad.objects.all()

    variables = {
        'destino':destino,
        'transporte':transporte,
        'nacionalidad':nacionalidad
    }

    if request.POST:
        cliente = Cliente()
        cliente.nombre = request.POST.get('nombre')
        cliente.apellido = request.POST.get('apellido')
        cliente.email = request.POST.get('correo')
        cliente.inicio = request.POST.get('inicio')
        cliente.fin = request.POST.get('fin')
        destino = Destino()
        destino.id = request.POST.get('donde')
        cliente.destino = destino
        nacionalidad = Nacionalidad()
        nacionalidad.id = request.POST.get('pais')
        cliente.nacionalidad = nacionalidad
        transporte = Transporte()
        transporte.id = request.POST.get('transporte')
        cliente.transporte = transporte

        try:
            cliente.save()
            variables['mensaje'] = 'Cliente Guardado'
        except:
            variables['mensaje'] = 'No se ha guardado el cliente'
    
    return render(request, 'core/formulario.html', variables)

#CRUD de Cliente
@login_required
def listar_clientes(request):
    clientes = Cliente.objects.all()
    apellido = ""  # Filtro por defecto
    nombre = ""
    if request.POST.get('apellido'):
        apellido = request.POST.get('apellido')
        clientes = clientes.filter(apellido=apellido)
    
    return render(request, 'core/listar_clientes.html', {
        'clientes':clientes, 'apellido':apellido
    })
   
    if request.POST.get('nombre'):
        nombre = request.POST.get('nombre')
        clientes = clientes.filter(nombre=nombre)
        
    return render(request, 'core/listar_clientes.html', {
        'clientes':clientes, 'nombre':nombre
    })
@login_required
def eliminar_cliente(request, id):
    #Buscar el cliente a eliminar
    cliente = Cliente.objects.get(id=id)

    try:
        cliente.delete()
        mensaje = "Cliente eliminado correctamente"
        messages.success(request, mensaje)
    except:
        mensaje = "Cliente no ha podido ser eliminado"
        messages.error(request, mensaje)
    return redirect('listado_clientes')
@login_required
def modificar_cliente(request, id):
    #modifica el cliente
    cliente = Cliente.objects.get(id=id)
    destino = Destino.objects.all()
    nacionalidad = Nacionalidad.objects.all()
    transporte = Transporte.objects.all()

    variables = {
        'cliente':cliente,
        'destino':destino,
        'nacionalidad':nacionalidad,
        'transporte':transporte
    }
    
    if request.POST:
        cliente = Cliente()
        cliente.id = request.POST.get('txtid')
        cliente.nombre = request.POST.get('nombre')
        cliente.apellido = request.POST.get('apellido')
        cliente.email = request.POST.get('correo')
        cliente.inicio = request.POST.get('inicio')
        cliente.fin = request.POST.get('fin')
        destino = Destino()
        destino.id = request.POST.get('donde')
        cliente.destino = destino
        nacionalidad = Nacionalidad()
        nacionalidad.id = request.POST.get('pais')
        cliente.nacionalidad = nacionalidad
        transporte = Transporte()
        transporte.id = request.POST.get('transporte')
        cliente.transporte = transporte

        try:
            cliente.save()
            messages.success(request, 'Cliente modificado') 
        except:
            messages.error(request, 'Cliente no se ha modificado') 
        return redirect('listado_clientes')
    return render(request, 'core/modificar_cliente.html', variables)
