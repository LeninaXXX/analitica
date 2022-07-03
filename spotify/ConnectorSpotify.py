import logging
import pandas as pd
from connectors.Connector import Connector
from databases.MongoDB.MongoDB import MongoDB       # Por ahora limito a MongoDB ... levantar _con la pala ancha_

from spotify.Account import Account

class ConnectorSpotify(Connector):

    def __init__(self) -> None:                 # Al construirse, el conector se hace de ...
        self.accounts = self.loadAccounts()     # ... una lista de cuentas levantadas de un file
        self.mongo = MongoDB()                  # ... un 'enchufe' a la database

    def execute(self):                          # 'Dispara' al conector a hacer _lo suyo_...
        for a in self.accounts:                 # ... itera sobre la lista de cuentas y _hace lo suyo_
            logging.info('Procesando')
        pass

    def loadAccounts(self) -> list[Account]:
        fp = 'spotify/accounts.csv'             # CAMPOS :: username, client_id, client_secret, redirect_uri
        csv = pd.read_csv(fp)
        accounts = list[Account]()
        
        # Esto es DEPENDIENTE DEL METODO DE AUTENTICACION y que se requiera. Provisionalmente asumo que 
        # ... voy a estar lidiando con pares client_id/client_secret, a los fines de esbozar el modulo.
        for idx, row in csv.iterrows():
            accounts.append(Account(row['username'], row['client_id'], row['client_secret'], row['redirect_uri']))      

        return accounts


