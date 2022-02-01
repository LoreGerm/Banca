from classi.cliente import cliente
from classi.bank import banca
from classi.conto import conto

# CODICE DI TEST. Rispondi alle domande scritte nei commenti #
cliente1 = cliente('Davide', '3924663077')
cliente2 = cliente('Simona', '3335688985')
cliente3 = cliente('Marco', '3335688285')
banca_san_paolo = banca('Banca San Paolo')
account = conto('00001',cliente1)


# Per questi print mi aspetto la stampa nel metodo __repr__
print("Account", "\n", account, "\n")
print("Banca", "\n", banca_san_paolo, "\n")
print("Cliente", "\n", cliente1, "\n")



'''
# RISPONDI ALLE DOMANDE SCRITTE NEI COMMENTI * 

#1. OUTPUT PREVISTO:  
print( cliente1.nome_cliente )


#2. OUTPUT PREVISTO:  
print(account.cliente.nome_cliente) 


#3. OUTPUT PREVISTO: 
cliente1.nome_cliente = 'Giovanni'
print(account.cliente.nome_cliente) 
'''