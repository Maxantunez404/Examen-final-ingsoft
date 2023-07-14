from flask import Flask, request
from models import *

app = Flask(__name__)

BD = [
    Cuenta("21345", "Arnaldo", 200, ["123", "456"]),
    Cuenta("123", "Luisa", 400, ["456"]),
    Cuenta("456", "Andrea", 300, ["21345"])
]

@app.route('/billetera/contactos', methods=['GET'])
def obtener_contactos():
    minumero = request.args.get('minumero')
    cuenta = buscar_cuenta_por_numero(minumero)
    if cuenta:
        return {'contactos': cuenta.contactos}
    else:
        return {'error': 'Cuenta no encontrada'}

@app.route('/billetera/pagar', methods=['GET'])
def realizar_pago():
    minumero = request.args.get('minumero')
    numerodestino = request.args.get('numerodestino')
    valor = float(request.args.get('valor'))

    cuenta_origen = buscar_cuenta_por_numero(minumero)
    cuenta_destino = buscar_cuenta_por_numero(numerodestino)

    if cuenta_origen and cuenta_destino:
        if cuenta_origen.saldo >= valor:
            cuenta_origen.saldo -= valor
            cuenta_destino.saldo += valor
            operacion = Operacion(numerodestino, datetime.now(), valor)
            cuenta_origen.operaciones.append(operacion)
            return "Realizado en {}".format(operacion.fecha)
        else:
            return {'error': 'Saldo insuficiente para realizar la transferencia'}
    else:
        return {'error': 'Cuenta origen o destino no encontrada'}

@app.route('/billetera/historial', methods=['GET'])
def obtener_historial():
    minumero = request.args.get('minumero')
    cuenta = buscar_cuenta_por_numero(minumero)
    if cuenta:
        return cuenta.historial()
    else:
        return {'error': 'Cuenta no encontrada'},404

def buscar_cuenta_por_numero(numero):
    for cuenta in BD:
        if cuenta.numero == numero:
            return cuenta
    return None

if __name__ == '__main__':
    app.run()
