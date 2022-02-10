import json
from classi.cliente import cliente
from classi.bank import banca
from classi.conto import conto,contoSpecial
from classi.persistence import PersistenceHandler

# CODICE DI TEST. Rispondi alle domande scritte nei commenti #
cliente1 = cliente('Davide', '3924663077')
cliente2 = cliente('Simona', '3335688985')
cliente3 = cliente('Marco', '3335688285')

banca_san_paolo = banca('Banca San Paolo')
banca_fineco = banca('Banca San Paolo', 'GE')

conto1 = contoSpecial(1588,cliente1,74845418744)
conto2 = contoSpecial(1685,cliente2,54897412)
conto3 = contoSpecial(1987,cliente3,82121454)

p = PersistenceHandler()

p.salva_clienti(cliente1.__dict__)
p.salva_clienti(cliente2.__dict__)
p.salva_clienti(cliente3.__dict__)

p.salva_banca(banca_san_paolo.__dict__)
p.salva_banca(banca_fineco.__dict__)

p.salva_conto(conto1)
p.salva_conto(conto2)
p.salva_conto(conto3)


conto1.stampa_numero_conto_nome()
conto1.stampa_saldo_nome()

conto2.stampa_numero_conto_nome()
conto2.stampa_saldo_nome()

conto3.stampa_numero_conto_nome()
conto3.stampa_saldo_nome()




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