from operator import truediv
from classi.cliente import cliente


class banca:

    def __init__(self, nome_banca,cliente = [],conto_corrente = [],nazione = 'IT'):
        self.__nazione = nazione
        self.__nome_banca = nome_banca
        self.__clienti = cliente
        self.__conti_correnti = conto_corrente

    def __repr__(self):
        return f"Nome banca: {self.__nome_banca} \n Nazione banca: {self.__nazione} \n Numero clienti: {len(self.__clienti)} \n Numero conti corrente: {len(self.__conti_correnti)}"


    def apri_conto_corrente(self, conto):
        self.__conti_correnti.append(conto)

    def aggiungi_cliente(self, cliente):
        self.__clienti.append(cliente)


    def chiudi_conto_corrente(self, numero_conto):
        canc = []
        for i in range(len(self.__conti_correnti)):
            if numero_conto == self.__conti_correnti[i].numero_conto:
                canc = self.__conti_correnti[i].pop()
                return True
        return False

    def rimuovi_cliente(self,id):
        canc = []
        for i in range(len(self.__clienti)):
            if int(id) == self.__clienti[i].id:
                canc.append(self.__clienti[i].pop())
                return True
        return False


    @property
    def nazione(self):
        return self.__nazione

    @nazione.setter
    def nazione(self,nazione):
        self.__nazione = nazione

    @property
    def nome_banca(self):
        return self.__nome_banca

    @nome_banca.setter
    def nome_banca(self,nome):
        self.__nome_banca = nome


    @property
    def clienti(self):
        return self.__clienti
    
    @clienti.setter
    def clienti(self,cliente):
        self.__clienti = cliente
    

    @property
    def conti_correnti(self):
        return self.__conti_correnti
    
    @conti_correnti.setter
    def conti_correnti(self,conto):
        self.__conti_correnti.append(conto)
        