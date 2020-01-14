import requests
from ..userAgent import agents
import random
class Movie:
	
	def __init__(self,url,time):
		self.url = url
		self.time = time

	def GetHtml(self):
		head = {}
		head['User-Agent'] = random.choice(agents)
		res = requests.get(self.url,headers=head)
		status = res.status_code
		print(status)
		return res.text
		