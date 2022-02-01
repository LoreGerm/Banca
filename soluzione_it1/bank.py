from soluzione_it1.cliente import cliente


class banca:

    def __init__(self, nome_banca,cliente = [],conto_corrente = []):
        self.__nome_banca = nome_banca
        self.__clienti = cliente
        self.__conti_correnti = conto_corrente

    def __repr__(self):
        return f"Nome banca: {self.__nome_banca} \n Numero clienti: {len(self.__clienti)} \n Numero conti corrente: {len(self.__conti_correnti)}"


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
        if self.__clienti == []:
            self.__clienti = cliente
        else:
            self.__clienti.append(cliente)
    

    @property
    def conti_correnti(self):
        return self.__conti_correnti
    
    @conti_correnti.setter
    def conti_correnti(self,conto):
        if self.__conti_correnti == []:
            self.__conti_correnti = conto
        else:
            self.__conti_correnti.append(conto)
        