from django.db import models

class Sucursal(models.Model):
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return self.direccion

class Cliente(models.Model):
    usuario = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    cedula = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return self.usuario

class Usuario(models.Model):
    ADMINISTRADOR = 'AD'
    EMPLEADO = 'EM'
    EMPLEADO_SUCUR = 'ES'
    CLIENTE = 'CL'

    ROL_CHOICES = [
        (ADMINISTRADOR, 'Administrador'),
        (EMPLEADO, 'Empleado'),
        (EMPLEADO_SUCUR, 'Empleado Sucursal'),
        (CLIENTE, 'Cliente'),
    ]

    nombreUsuario = models.CharField(max_length=255)
    email = models.EmailField()
    rol = models.CharField(max_length=2, choices=ROL_CHOICES, default=CLIENTE)
    primerNombre = models.CharField(max_length=255)
    primerApellido = models.CharField(max_length=255)

    def __str__(self):
        return self.nombreUsuario

class Medicamento(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.FloatField()
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Inventario(models.Model):
    farmaciald = models.IntegerField()
    medicamentold = models.IntegerField()
    cantidad = models.IntegerField()
    actualizarStock = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Inventario de {self.medicamentold}"

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    sucursalCompra = models.ForeignKey(Sucursal, related_name='sucursal_compra', on_delete=models.CASCADE)
    sucursalEntrega = models.ForeignKey(Sucursal, related_name='sucursal_entrega', on_delete=models.CASCADE)
    fecha = models.DateField()
    estado = models.CharField(max_length=50)

    def __str__(self):
        return f"Pedido de {self.cliente} en {self.sucursalCompra}"

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"Detalle de Pedido {self.pedido} - Medicamento {self.medicamento}"

class Transferencia(models.Model):
    sucursalOrigen = models.ForeignKey(Sucursal, related_name='sucursal_origen', on_delete=models.CASCADE)
    sucursalDestino = models.ForeignKey(Sucursal, related_name='sucursal_destino', on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha = models.DateField()

    def __str__(self):
        return f"Transferencia de {self.medicamento} de {self.sucursalOrigen} a {self.sucursalDestino}"

class Venta(models.Model):
    clienteId = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    farmaciald = models.IntegerField()
    medicamentold = models.IntegerField()
    total = models.FloatField()

    def realizarVenta(self):
        # Lógica para realizar la venta
        pass

    def calcularTotal(self):
        # Lógica para calcular el total
        pass

    def __str__(self):
        return f"Venta de {self.medicamentold} a {self.clienteId}"

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precioUnitario = models.FloatField()

    def __str__(self):
        return f"Detalle de Venta {self.venta} - Cantidad {self.cantidad}"
