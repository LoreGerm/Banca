class conto:

    def __init__(self, bilancio_conto, numero_conto, saldo=0):
        self.__bilancio_conto = bilancio_conto
        self.__numero_conto = numero_conto
        self.__saldo = saldo
        __operazioni_effettuate = []

