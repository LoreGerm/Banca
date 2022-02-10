from classi.cliente import cliente
from classi.bank import banca
from classi.conto import conto
from classi.persistence import PersistenceHandler

# CODICE DI TEST. Rispondi alle domande scritte nei commenti #
cliente1 = cliente('Davide', '3924663077')
cliente2 = cliente('Simona', '3335688985')
cliente3 = cliente('Marco', '3335688285')
banca_san_paolo = banca('Banca San Paolo')
cont = conto('00001',cliente1)
p = PersistenceHandler()

#p.salva_clienti(cliente1.__dict__)
#p.salva_banca(banca_san_paolo.__dict__)
p.salva_conto(cont)



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