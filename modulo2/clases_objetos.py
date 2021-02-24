import uuid

class Cliente:
    nombre: str
    id: int
    saldo: float

    def __init__(self, nombre, saldo):
        self.nombre = nombre
        self.id = uuid.uuid1()
        self.saldo = saldo


    def girar(self, monto_giro):
        self.saldo = self.saldo - monto_giro
        return self.saldo


    def abonar(self, recibir_monto):
        self.saldo = self.saldo + recibir_monto
        return self.saldo

    def mostrar_saldo(self):
        return self.saldo

    def r_id(self):
        return self.id


class Financiera:
    nombre: str
    id: int
    saldo_institucional: float
    clientes: []

    def __init__(self, nombre, id, saldo_institucional):
        self.nombre = nombre
        self.id = uuid.uuid1()
    
    #def agregar_cliente():

    #def eliminar_cliente():

    #def transferir():

    #def giros_totales():

    #def abonos_totales():

    #def mostrar_saldo_institucional():

    
Luis = Cliente('luis', 1000)

print(Luis.r_id())

Luis.girar(500)

Luis.abonar(4000)

print('el saldo total es:', Luis.mostrar_saldo())