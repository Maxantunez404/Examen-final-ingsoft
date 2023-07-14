from datetime import datetime

class Cuenta:
    def __init__(self, numero, nombre, saldo, contactos):
        self.numero = numero
        self.nombre = nombre
        self.saldo = saldo
        self.contactos = contactos
        self.operaciones = []

    def historial(self):
        saldo_str = "Saldo de {}: {}".format(self.nombre, self.saldo)
        operaciones_str = "Operaciones de {}:".format(self.nombre)
        operaciones = []
        for op in self.operaciones:
            operaciones.append(str(op))
        return [saldo_str, operaciones_str] + operaciones

    def pagar(self, destino, valor):
        if self.saldo >= valor:
            if self.es_contacto(destino):
                self.saldo -= valor
                operacion = Operacion(destino, datetime.now(), valor)
                self.operaciones.append(operacion)
                print("Transferencia realizada con éxito.")
            else:
                print("El destino no es un contacto válido.")
        else:
            print("Saldo insuficiente para realizar la transferencia.")

    def es_contacto(self, numero):
        return numero in self.contactos

class Operacion:
    def __init__(self, numero_destino, fecha, valor):
        self.numero_destino = numero_destino
        self.fecha = fecha
        self.valor = valor

    def mostrar_operacion(self):
        return "Destino: {}, Fecha: {}, Valor: {}".format(self.numero_destino, self.fecha, self.valor)
