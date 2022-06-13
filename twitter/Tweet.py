import pandas as pd

class Tweet:
	def __init__(self, data : dict) -> None:
		self.data = data

	def asSQLDF(self):
		return pd.json_normalize(self.data)