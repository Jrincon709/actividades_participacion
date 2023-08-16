#Para la clase CuentaBancaria, cree un método depositar que maneje las acciones de depósito en la cuenta.
#Para la clase CuentaBancaria, cree un método retirar que maneje las acci=ones de retiro de la cuenta.
#Para la clase CuentaBancaria, cree un método aplicar_cuota_manejo que aplique un porcentaje del 2% sobre el balance de la cuenta
#Para la clase CuentaBancaria, cree un método mostrar_detalles que imprima por consola los detalles de la cuenta bancaria.

class CUENTABANCARIA:
    def __init__( self ):
        self.my_dinero = 0


    def depositar( self, monto ):
        self.my_dinero += monto
        return self.my_dinero
    

    def retirar( self, retiro):
        if self.my_dinero >= retiro:
            self.my_dinero -= retiro
            return self.my_dinero
        else:
            print ("Fondos Insuficientes")
            return self.my_dinero
    

    def aplicar_cuota_manejo(self):
        cuota = self.my_dinero * 0.02
        self.my_dinero -= cuota
        return self.my_dinero




    