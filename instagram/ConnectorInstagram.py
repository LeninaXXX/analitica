import pandas as pd
from connectors.Connector import Connector
from databases.MongoDB.MongoDB import MongoDB
from databases.SQLServer.SQLServer import SQLServer
from instagram.Account import Account

class ConnectorInstagram(Connector):

	def __init__(self) -> None:
		self.accounts = self.loadAccounts()
		self.mongo = MongoDB()
		self.sql = SQLServer()

	def execute(self):
		## TODO: Add Business discovery para ver numeros de otras cuentas
		# Para cada cuenta
		for a in self.accounts:
			posts = a.getPosts(10)
			posts_df = []
			for p in posts:
				self.mongo.upsertDict(p.asRawDict(),'TESTE','InstagramPosts')
				posts_df.append(p.asSQLDict())
			self.sql.upsert(pd.DataFrame(posts_df),'PY_IG_MEDIA')
			
			stories = a.getStories(10)
			stories_df = []
			for s in stories:
				self.mongo.upsertDict(s.asRawDict(),'TESTE','InstagramStories')
				stories_df.append(s.asSQLDict())
			self.sql.upsert(pd.DataFrame(stories_df),'PY_IG_STORIES')

			# insights = a.getDailyInsights(10)
			# for i in insights:
			# 	self.mongo.upsertDict(i.asRawDF(),'TESTE','InstagramInsights')
			# 	self.sql.upsert(i.asSQLDF(),'PY_IG_AccountInsights')

			# insights = a.getLifetimeInsights(10)
			# for i in insights:
			# 	self.mongo.upsertDict(i.asRawDF(),'TESTE','InstagramInsights')
			# 	self.sql.upsert(i.asSQLDF(),'PY_IG_AudienceInsights')

	def loadAccounts(self) -> list[Account]:
		filepath = 'instagram/accounts.csv'
		csv = pd.read_csv(filepath)
		accounts = list[Account]()
		for index, row in csv.iterrows():
			accounts.append(Account(row['id'], row['name'],row['token']))

		return accounts