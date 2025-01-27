from django.contrib import admin
from .models import Sucursal, Cliente, Usuario, Medicamento, Inventario, Pedido, DetallePedido, Transferencia, Venta, DetalleVenta

admin.site.register(Sucursal)
admin.site.register(Cliente)
admin.site.register(Usuario)
admin.site.register(Medicamento)
admin.site.register(Inventario)
admin.site.register(Pedido)
admin.site.register(DetallePedido)
admin.site.register(Transferencia)
admin.site.register(Venta)
admin.site.register(DetalleVenta)