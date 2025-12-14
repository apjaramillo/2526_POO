class Cuenta:  # (defino la clase Cuenta)
    def __init__(self):  # (inicializo la cuenta)
        self.__saldo = 0  # (protejo el saldo y lo inicio en 0)

    def depositar(self, monto):  # (defino metodo para depositar)
        self.__saldo += monto  # (sumo el monto al saldo)

    def ver_saldo(self):  # (defino metodo para ver saldo)
        print(self.__saldo)  # (muestro el saldo actual)

c = Cuenta()  # (creo un objeto c de la clase Cuenta)
c.depositar(100)  # (deposito 100 en la cuenta)
c.ver_saldo()  # (muestro el saldo, imprime 100)
#FIN