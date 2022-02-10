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
        if self.__saldo >= value + self.__tassa_prelievo:
            self.__saldo -= value - self.__tassa_prelievo
        else:
            return False

    def stampa_saldo_nome(self):
            print(self.__bilancio_conto.nome_cliente, ' -> Saldo: ', self.__saldo)

    def stampa_numero_conto_nome(self):
            print(self.__bilancio_conto.nome_cliente, ' -> Codice conto: ', self.__numero_conto)
    

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
        self.__operazioni_effettuate.append(operazione)





class contoSpecial(conto):
    __tassa_prelievo = 2.0
    __interessi = 1.2

    def __init__(self, numero_conto, bilancio_conto, saldo=0, operazioni=[]):
        super().__init__(numero_conto, bilancio_conto, saldo, operazioni)
        self.__tot_giorni_debito = 0
        self.__data_inizio_debito = None

    def preleva_soldi(self, value):
        self.__saldo -= value - self.__tassa_prelievo
        if self.__saldo < 0 and self.__data_inizio_debito == None:
            self.__tot_giorni_debito += 1
            self.__data_inizio_debito = Timestamp()
        
    def versa_soldi(self, value):
        super().versa_soldi(value)
        if self.__saldo > 0 and self.__data_inizio_debito != None:
            print('Debiti: ', self.__tot_giorni_debito*self.__interessi)
            self.__tot_giorni_debito = 0
            self.__data_inizio_debito = None
            print("Saldo positivo")
        
            