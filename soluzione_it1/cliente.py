class cliente:

    def __init__(self, nome_cliente, numero_telefono):
        self.__nome_cliente = nome_cliente
        self.__numero_telefono = numero_telefono

    def __repr__(self):
        return f"Nome cliente: {self.__nome_cliente} \n Numero telefono: {self.__numero_telefono}"
