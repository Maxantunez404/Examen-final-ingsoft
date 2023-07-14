import unittest
from flask import Flask
from flask.testing import FlaskClient
from app import *
from models import *

class ContactosTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    #Test de exito
    def test_obtener_contactos(self):
        respuesta = self.app.get('/billetera/contactos?minumero=123')
        self.assertEqual(respuesta.status_code, 200)
        datos_respuesta = respuesta.get_json()
        self.assertIn('contactos', datos_respuesta)
        self.assertEqual(datos_respuesta['contactos'], ['456'])

    #Test de error
    def test_obtener_contactos_error(self):
        respuesta = self.app.get('/billetera/contactos?minumero=123456789')
        self.assertEqual(respuesta.status_code, 200)
        datos_respuesta = respuesta.get_json()
        self.assertIn('error', datos_respuesta)
        self.assertEqual(datos_respuesta['error'], 'Cuenta no encontrada')

    def test_realizar_pago_error_cuenta(self):
        respuesta = self.app.get('/billetera/pagar?minumero=213122145&numerodestino=123&valor=100')
        self.assertEqual(respuesta.status_code, 200)
        datos_respuesta = respuesta.get_json()
        self.assertIn('error', datos_respuesta)
        self.assertEqual(datos_respuesta['error'], 'Cuenta origen o destino no encontrada')

    def test_realizar_pago_error_valor(self):
        respuesta = self.app.get('/billetera/pagar?minumero=21345&numerodestino=123&valor=1122100')
        self.assertEqual(respuesta.status_code, 200)
        datos_respuesta = respuesta.get_json()
        self.assertIn('error', datos_respuesta)
        self.assertEqual(datos_respuesta['error'], 'Saldo insuficiente para realizar la transferencia')

if __name__ == '__main__':
    unittest.main()
