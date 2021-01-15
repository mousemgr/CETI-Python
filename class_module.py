class Pedido:
    def __init__(self, numero_pedido=0, cliente="", importe_total=0.0, repartidor=""):
        self.numero_pedido = numero_pedido
        self.cliente = cliente
        self.importe_total = importe_total
        self.repartidor = repartidor

    def registrar_informacion(self):
        self.numero_pedido = int(input("Captura el número de pedido:"))
        self.cliente = input("Captura el cliente:")
        self.importe_total = float(input("Captura el importe total:"))
        self.repartidor = input("Captura el repartidor:")




p = Pedido(1500, "Los Arcos", 2000.50, "Juan Ortega")
print("Número pedido:" + str(p.numero_pedido))
print("Número cliente:" + p.cliente)
print("Número importe_total:" + str(p.importe_total))
print("Número repartidor:" + p.repartidor)
print("----------------------------------")


p2 = Pedido()
p2.registrar_informacion()

print("Número pedido:" + str(p2.numero_pedido))
print("Número cliente:" + p2.cliente)
print("Número importe_total:" + str(p2.importe_total))
print("Número repartidor:" + p2.repartidor)

