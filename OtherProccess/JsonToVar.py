import os
import json
from Printify import Printify


class JsonToVar:
	def __init__(self):
		self.Configs = {}

	@staticmethod
	def VerifyExistence():
		if os.path.isfile(r"./Configs.json"):
			return True
		else:
			return False

	@staticmethod
	def CreateConfig():
		Printify("Creating new config file...").Inform()
		with open(r"./Configs.json", "w") as ConfigsWriter:
			ConfigsWriter.write("""""")

	def Transform(self):
		with open(r"./Configs.json") as ConfigsRaw:
			JsonConfigs = json.load(ConfigsRaw)
			for Key, Value in JsonConfigs.items():
				self.Configs[Key] = Value
				print(f"{Key} :: {Value}")


