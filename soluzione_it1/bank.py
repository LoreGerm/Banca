class banca:

    def __init__(self, nome_banca):
        self.__nome_banca = nome_banca
        self.__clienti = []
        self.__conti_correnti = []

    def __repr__(self):
        return f"Nome banca: {self.__nome_banca} \n Numero clienti: {len(self.__clienti)} \n Numero conti corrente: {len(self.__conti_correnti)}"

    
        