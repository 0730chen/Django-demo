import requests
from ..userAgent import agents
class Movie:
	
	def __init__(self,url,time):
		self.url = url
		self.time = time

	def GetHtml(self):
		head = {}
		head['User-Agent'] = 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
		res = requests.get(self.url,headers=head)
		status = res.status_code
		print(status)
		return res.text
		