import os
import json
from json import JSONEncoder





class EmployeeEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__





class PersistenceHandler:
    
    def over_write(self,file,x):
        f = open(file, "w")
        f.write(json.dumps(x)) 
        f.close()


    def get_size(self,file):
        try:
            size = os.path.getsize(file)
        except:
            self.over_write(file,[])
            size = os.path.getsize(file)
        return size
    

    def stampa_file(self,file):
        f = open(file, "r")
        x = f.read()
        f.close()
        return x


    def salva_banca(self,banca):
        file = 'classi/file/banca.json'
        size = self.get_size(file)
        if size == 0:
            b = [banca]
            self.over_write(file,b)
        else:
            all = json.loads(self.stampa_file(file))
            all.append(banca)
            self.over_write(file,all)
            
    

    def salva_clienti(self,clienti):
        file = 'classi/file/clienti.json'
        size = self.get_size(file)
        if size == 0:
            c = [clienti]
            self.over_write(file,c)
        else:
            all = json.loads(self.stampa_file(file))
            all.append(clienti)
            self.over_write(file,all)
        
    
    def salva_conto(self,conto):
        conto_encode = EmployeeEncoder().encode(conto)
        file = 'classi/file/conto.json'
        size = self.get_size(file)
        if size == 0:
            c = [conto_encode]
            self.over_write(file,c)
        else:
            all = json.loads(self.stampa_file(file))
            all.append(conto_encode)
            self.over_write(file,all)
        
    
    def salva_tutto(self,banca,clienti,conto):
        self.salva_banca(banca)
        self.salva_clienti(clienti)
        self.salva_conto(conto)
              
        
