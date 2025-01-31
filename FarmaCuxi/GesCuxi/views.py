from django.shortcuts import render
from .models import Cliente, Sucursal, Usuario, Medicamento, Inventario, Pedido, DetallePedido, Transferencia, Venta, DetalleVenta

def inicio(request):
    return render(request, 'inicio.html')

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes.html', {'clientes': clientes})

def lista_sucursales(request):
    sucursales = Sucursal.objects.all()
    return render(request, 'sucursales.html', {'sucursales': sucursales})

def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios.html', {'usuarios': usuarios})

def lista_medicamentos(request):
    medicamentos = Medicamento.objects.all()
    return render(request, 'medicamentos.html', {'medicamentos': medicamentos})

def lista_inventario(request):
    inventario = Inventario.objects.all()
    return render(request, 'inventario.html', {'inventario': inventario})

def lista_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedidos.html', {'pedidos': pedidos})

def lista_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'ventas.html', {'ventas': ventas})

def lista_transferencias(request):
    transferencias = Transferencia.objects.all()
    return render(request, 'transferencias.html', {'transferencias': transferencias})