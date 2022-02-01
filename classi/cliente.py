class cliente:

    def __init__(self, nome_cliente, numero_telefono):
        self.__nome_cliente = nome_cliente
        self.__numero_telefono = numero_telefono
        self.__id = id(self)

    def __repr__(self):
        return f"Nome cliente: {self.__nome_cliente} \n Numero telefono: {self.__numero_telefono}"


    @property
    def id(self):
        return self.__id

    @property
    def nome_cliente(self):
        return self.__nome_cliente

    @nome_cliente.setter
    def nome_cliente(self,nome):
        self.__nome_cliente = nome

    @property
    def numero_telefono(self):
        return self.__numero_telefono

    @numero_telefono.setter
    def numero_telefono(self,telefono):
        self.numero_telefono = telefono

