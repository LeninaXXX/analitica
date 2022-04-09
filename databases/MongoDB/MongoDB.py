from databases.Database import Database
import pandas as pd
from pymongo import MongoClient

class MongoDB(Database):
	def __init__(self):
		self.client = MongoClient('mongodb://administrador:p4s$w0Rd@172.16.7.19:27017')

	def upsertDF(self,df: pd.DataFrame, base, collection):

		db = self.client[base]
		# collection
		collection = db[collection]

		# Recorrer las filas del dataframe y guardar en la base de datos
		lista = {}
		for i,r in df.iterrows():
			for key in df.keys():
				lista[key] = r[key]
			id = lista.pop('id')
			collection.update_one({"_id": id},{"$set": lista},upsert=True)

	def upsertDict(self,aDict: dict, base, collection):
		# database
		db = self.client[base]
		# collection
		collection = db[collection]

		id = aDict.pop('_id')
		# Upsert
		collection.update_one(
			{"_id": id},
			{"$set": aDict},
			upsert=True
		)