import colorama as col

C = col.Fore

class Printify:
	def __init__(self, Message, Tab:int = 0, Log:bool = False, SLog:bool = False):
		self.Message = Message
		self.Tab = str(" "*Tab)
		self.Log = Log
		self.SLog = SLog

	def Error(self):
		v = f"{self.Tab}{C.BLUE}[    {C.RED}Error    {C.BLUE}]  {C.LIGHTYELLOW_EX}{self.Message}{col.Style.RESET_ALL}"
		print(v)

	def SError(self):
		v = f"{self.Tab}{C.BLUE}[ {C.RED}X {C.BLUE}]  {C.LIGHTYELLOW_EX}{self.Message}{col.Style.RESET_ALL}"
		print(v)

	def Inform(self):
		v = f"{self.Tab}[ Information ]  {self.Message}"
		print(v)

	def SInform(self):
		v = f"{self.Tab}[ * ]  {self.Message}"
		print(v)

	def Note(self):
		v = f"{self.Tab}[    Note     ]  {self.Message}"
		print(v)

	def SNote(self):
		v = f"{self.Tab}[ ! ]  {self.Message}"
		print(v)

	def Suggest(self):
		v = f"{self.Tab}[ Suggestion  ]  {self.Message}"
		print(v)

	def SSuggest(self):
		v = f"{self.Tab}[ ? ]  {self.Message}"
		print(v)

	def List(self, count:int = None):
		if count is None:
			v = f"{self.Tab}[    List     ]  {self.Message}"
		else:
			v = f"{self.Tab}[   List #{count}   ]  {self.Message}"
		print(v)

	def SList(self, count:int = None):
		if count is None:
			v = f"{self.Tab}[ # ]  {self.Message}"
		else:
			v = f"{self.Tab}[ #{count} ]  {self.Message}"
		print(v)

Printify("MESSAGE").SError()
