from OtherProccess.JsonToVar import JsonToVar
from OtherProcess.Printify import Printify
from OtherProcess.DBHandler import DBHandler
from guilded.ext import commands
import guilded

JTV = JsonToVar()
DBH = DBHandler()

Bot = commands.Bot(command_prefix=DefaultPrefix, owner_id=BotOwnerUserID, owner_ids=BotCoOwnerUserIDs, description=BotDescription, help_command=None, case_insensitive=True)
