class conto:

    def __init__(self, numero_conto, bilancio_conto, saldo=0):
        self.__bilancio_conto = bilancio_conto
        self.__numero_conto = numero_conto
        self.__saldo = saldo
        self.__operazioni_effettuate = []

    def __repr__(self):
        return f"Numero conto: {self.__numero_conto} \n {self.__bilancio_conto} \n Saldo: {self.__saldo} \n Operazioni effettuate: {len(self.__operazioni_effettuate)}"

