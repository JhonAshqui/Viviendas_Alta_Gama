from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Proyecto
from .models import ClienteVIP
from .models import Vivienda
from .models import Costo
# Create your views here.
def index(request):
    return render(request, 'index.html')
def agregarProyecto(request):
    return render(request,'agregarProyecto.html')
# Listado de Proyectos
def listadoProyectos(request):
    proyectosBdd = Proyecto.objects.all()
    return render(request, 'listadoProyectos.html', {'proyectos': proyectosBdd})

# Guardar Proyecto
def guardarProyecto(request):
    Proyecto.objects.create(
        nombre=request.POST['txt_nombre'],
        descripcion=request.POST.get('txt_descripcion', ''),
        fecha_inicio=request.POST['txt_fecha_inicio'],
        fecha_fin=request.POST.get('txt_fecha_fin', None),
        foto=request.FILES.get("archivo_proyecto")  # Documento del proyecto
    )
    messages.success(request, "Proyecto registrado correctamente")
    return redirect('/listadoProyectos')

# Eliminar Proyecto
def eliminarProyecto(request, id):
    proyectoEliminar = Proyecto.objects.get(id=id)
    proyectoEliminar.delete()
    messages.success(request, "Proyecto eliminado correctamente")
    return redirect('/listadoProyectos')

# Editar Proyecto (mostrar formulario con datos cargados)
def editarProyecto(request, id):
    proyectoEditar = Proyecto.objects.get(id=id)
    return render(request, "editarProyecto.html", {'proyecto': proyectoEditar})

# Procesar la edición de Proyecto
def procesarEdicionProyecto(request):
    proyecto = Proyecto.objects.get(id=request.POST['id_proyecto'])

    # Verifica si hay un nuevo archivo en los archivos
    nuevo_documento = request.FILES.get("archivo_proyecto")
    if nuevo_documento:
        proyecto.foto = nuevo_documento  # Actualiza solo si se sube un nuevo archivo

    proyecto.nombre = request.POST['txt_nombre']
    proyecto.descripcion = request.POST.get('txt_descripcion', '')
    proyecto.fecha_inicio = request.POST['txt_fecha_inicio']
    proyecto.fecha_fin = request.POST.get('txt_fecha_fin', None)

    proyecto.save()
    messages.success(request, "Proyecto editado correctamente")
    return redirect('/listadoProyectos')





# Agregar ClienteVIP
def agregarClienteVIP(request):
    return render(request, 'agregarClienteVIP.html')

# Listado de ClientesVIP
def listadoClientesVIP(request):
    clientesVIPBdd = ClienteVIP.objects.all()
    return render(request, 'listadoClientesVIP.html', {'clientesVIP': clientesVIPBdd})

# Guardar ClienteVIP
def guardarClienteVIP(request):
    ClienteVIP.objects.create(
        nombre=request.POST['txt_nombre'],
        email=request.POST['txt_email'],
        telefono=request.POST.get('txt_telefono', ''),
        direccion=request.POST.get('txt_direccion', '')
    )
    messages.success(request, "Cliente VIP registrado correctamente")
    return redirect('/listadoClientesVIP')

# Eliminar ClienteVIP
def eliminarClienteVIP(request, id):
    clienteEliminar = ClienteVIP.objects.get(id=id)
    clienteEliminar.delete()
    messages.success(request, "Cliente VIP eliminado correctamente")
    return redirect('/listadoClientesVIP')

# Editar ClienteVIP (mostrar formulario con datos cargados)
def editarClienteVIP(request, id):
    clienteEditar = ClienteVIP.objects.get(id=id)
    return render(request, "editarClienteVIP.html", {'cliente': clienteEditar})

# Procesar la edición de ClienteVIP
def procesarEdicionClienteVIP(request):
    cliente = ClienteVIP.objects.get(id=request.POST['id_clienteVIP'])

    cliente.nombre = request.POST['txt_nombre']
    cliente.email = request.POST['txt_email']
    cliente.telefono = request.POST.get('txt_telefono', '')
    cliente.direccion = request.POST.get('txt_direccion', '')

    cliente.save()
    messages.success(request, "Cliente VIP editado correctamente")
    return redirect('/listadoClientesVIP')

# Agregar Vivienda
def agregarVivienda(request):
    proyectos = Proyecto.objects.all()
    clientesVIP = ClienteVIP.objects.all()
    return render(request, 'agregarVivienda.html', {'proyectos': proyectos, 'clientes': clientesVIP})

# Listado de Viviendas
def listadoViviendas(request):
    viviendasBdd = Vivienda.objects.all()
    return render(request, 'listadoViviendas.html', {'viviendas': viviendasBdd})

# Guardar Vivienda
def guardarVivienda(request):
    proyecto = Proyecto.objects.get(id=request.POST['txt_proyecto'])
    cliente = ClienteVIP.objects.get(id=request.POST['txt_cliente']) if request.POST['txt_cliente'] else None

    Vivienda.objects.create(
        proyecto=proyecto,
        cliente=cliente,
        direccion=request.POST['txt_direccion'],
        metros_cuadrados=request.POST['txt_metros_cuadrados'],
        precio=request.POST['txt_precio'],
        estado=request.POST['txt_estado'],
        foto=request.FILES.get('foto_vivienda')
    )
    messages.success(request, "Vivienda registrada correctamente")
    return redirect('/listadoViviendas')

# Eliminar Vivienda
def eliminarVivienda(request, id):
    viviendaEliminar = Vivienda.objects.get(id=id)
    viviendaEliminar.delete()
    messages.success(request, "Vivienda eliminada correctamente")
    return redirect('/listadoViviendas')

# Editar Vivienda (mostrar formulario con datos cargados)
def editarVivienda(request, id):
    viviendaEditar = Vivienda.objects.get(id=id)
    proyectos = Proyecto.objects.all()
    clientesVIP = ClienteVIP.objects.all()
    return render(request, "editarVivienda.html", {'vivienda': viviendaEditar, 'proyectos': proyectos, 'clientes': clientesVIP})

# Procesar la edición de Vivienda
def procesarEdicionVivienda(request):
    vivienda = Vivienda.objects.get(id=request.POST['id_vivienda'])

    vivienda.proyecto = Proyecto.objects.get(id=request.POST['txt_proyecto'])
    vivienda.cliente = ClienteVIP.objects.get(id=request.POST['txt_cliente']) if request.POST['txt_cliente'] else None
    vivienda.direccion = request.POST['txt_direccion']
    vivienda.metros_cuadrados = request.POST['txt_metros_cuadrados']
    vivienda.precio = request.POST['txt_precio']
    vivienda.estado = request.POST['txt_estado']

    if 'foto_vivienda' in request.FILES:
        vivienda.foto = request.FILES['foto_vivienda']

    vivienda.save()
    messages.success(request, "Vivienda editada correctamente")
    return redirect('/listadoViviendas')



# Agregar Costo
def agregarCosto(request):
    proyectos = Proyecto.objects.all()
    viviendas = Vivienda.objects.all()
    return render(request, 'agregarCosto.html', {'proyectos': proyectos, 'viviendas': viviendas})

# Listado de Costos
def listadoCostos(request):
    costosBdd = Costo.objects.all()
    return render(request, 'listadoCostos.html', {'costos': costosBdd})

# Guardar Costo
def guardarCosto(request):
    proyecto = Proyecto.objects.get(id=request.POST['txt_proyecto'])
    vivienda = Vivienda.objects.get(id=request.POST['txt_vivienda']) if request.POST['txt_vivienda'] else None

    Costo.objects.create(
        proyecto=proyecto,
        vivienda=vivienda,
        descripcion=request.POST['txt_descripcion'],
        monto=request.POST['txt_monto'],
        fecha=request.POST['txt_fecha']
    )
    messages.success(request, "Costo registrado correctamente")
    return redirect('/listadoCostos')

# Eliminar Costo
def eliminarCosto(request, id):
    costoEliminar = Costo.objects.get(id=id)
    costoEliminar.delete()
    messages.success(request, "Costo eliminado correctamente")
    return redirect('/listadoCostos')

# Editar Costo (mostrar formulario con datos cargados)
def editarCosto(request, id):
    costoEditar = Costo.objects.get(id=id)
    proyectos = Proyecto.objects.all()
    viviendas = Vivienda.objects.all()
    return render(request, "editarCosto.html", {'costo': costoEditar, 'proyectos': proyectos, 'viviendas': viviendas})

# Procesar la edición de Costo
def procesarEdicionCosto(request):
    costo = Costo.objects.get(id=request.POST['id_costo'])

    costo.proyecto = Proyecto.objects.get(id=request.POST['txt_proyecto'])
    costo.vivienda = Vivienda.objects.get(id=request.POST['txt_vivienda']) if request.POST['txt_vivienda'] else None
    costo.descripcion = request.POST['txt_descripcion']
    costo.monto = request.POST['txt_monto']
    costo.fecha = request.POST['txt_fecha']

    costo.save()
    messages.success(request, "Costo editado correctamente")
    return redirect('/listadoCostos')
