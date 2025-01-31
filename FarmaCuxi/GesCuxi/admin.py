from django.contrib import admin
from .models import Cliente, Sucursal, Usuario, Medicamento, Inventario, Pedido, DetallePedido, Transferencia, Venta, DetalleVenta

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'telefono', 'email')
    search_fields = ('nombre', 'email')

@admin.register(Sucursal)
class SucursalAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'telefono')
    search_fields = ('nombre',)

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'sucursal')
    search_fields = ('nombre', 'email')
    list_filter = ('sucursal',)

@admin.register(Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio')
    search_fields = ('nombre',)

@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ('medicamento', 'sucursal', 'cantidad')
    list_filter = ('sucursal', 'medicamento')

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'fecha', 'total')
    search_fields = ('cliente__nombre',)
    list_filter = ('fecha',)

@admin.register(DetallePedido)
class DetallePedidoAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'medicamento', 'cantidad', 'precio')
    list_filter = ('pedido', 'medicamento')

@admin.register(Transferencia)
class TransferenciaAdmin(admin.ModelAdmin):
    list_display = ('medicamento', 'sucursal_origen', 'sucursal_destino', 'cantidad', 'fecha')
    list_filter = ('sucursal_origen', 'sucursal_destino', 'fecha')

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'fecha', 'total')
    search_fields = ('cliente__nombre',)
    list_filter = ('fecha',)

@admin.register(DetalleVenta)
class DetalleVentaAdmin(admin.ModelAdmin):
    list_display = ('venta', 'medicamento', 'cantidad', 'precio')
    list_filter = ('venta', 'medicamento')