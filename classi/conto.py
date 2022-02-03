from sqlite3 import Timestamp


class conto:

    __tassa_prelievo = 1.0


    def __init__(self, numero_conto, bilancio_conto, saldo=0, operazioni = []):
        self.__bilancio_conto = bilancio_conto
        self.__numero_conto = numero_conto
        self.__saldo = saldo
        self.__operazioni_effettuate = operazioni

    def __repr__(self):
        return f"Numero conto: {self.__numero_conto} \n {self.__bilancio_conto} \n Saldo: {self.__saldo} \n Operazioni effettuate: {len(self.__operazioni_effettuate)}"

    def versa_soldi(self,value):
        self.__saldo += value

    def preleva_soldi(self,value):
        if self.__saldo >= value:
            self.__saldo -= value - self.__tassa_prelievo
        else:
            return False

    @property
    def bliancio_conto(self):
        return self.__bliancio_conto

    @bliancio_conto.setter
    def bliancio_conto(self,bliancio):
        self.__bliancio_conto = bliancio


    @property
    def numero_conto(self):
        return self.__numero_conto
    
    @numero_conto.setter
    def numero_conto(self,numero_conto):
        self.__numero_conto = numero_conto

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self,saldo):
        self.__saldo = saldo


    @property
    def operazioni_effettuate(self):
        return self.__operazioni_effettuate
    
    @operazioni_effettuate.setter
    def operazioni_effettuate(self,operazione):
        if self.__operazioni_effettuate == []:
            self.__operazioni_effettuate = operazione
        else:
            self.__operazioni_effettuate.append(operazione)





class contoSpecial(conto):
    __tassa_prelievo = 2.0
    __data_inizio_debito = None


    def __init__(self, numero_conto, bilancio_conto, saldo=0, operazioni=[]):
        super().__init__(numero_conto, bilancio_conto, saldo, operazioni)

    def preleva_soldi(self, value):
        self.__saldo -= value - self.__tassa_prelievo
        if self.__saldo < 0 and self.__data_inizio_debito != None:
            self.__data_inizio_debito = Timestamp()
        
    def versa_soldi(self, value):
        super().versa_soldi(value)
        if self.__saldo > 0:
            self.__data_inizio_debito = None
            return "Saldo positivo"
        
            