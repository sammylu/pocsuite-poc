from pocsuite3.api import Output, POCBase, register_poc, requests, logger
from pocsuite3.api import get_listener_ip, get_listener_port
from pocsuite3.api import REVERSE_PAYLOAD
from pocsuite3.lib.utils import random_str
from urllib.parse import urlparse,parse_qs
import re
import requests

class HoutaiBoom(POCBase):
	vulID = '0'
	name = '诈骗网站后台特征爆破'
	appName = 'dede'
	appVersion = '1.0'
	desc = 'test'

	def dede(self,scheme,netloc,path,param):
		rule1 = re.compile(r'^\..*?\?.*?')
		result1 = re.search(rule1,param)
		if result1:
		   	print(param)
		   	url = 'dede'
			print(url)
		return 

	def _verify(self):
		result = {}
		url = self.url
		parseResult = urlparse(url)
		scheme = parseResult.scheme
		netloc = parseResult.netloc
		path = parseResult.path
		url = scheme+'://'+netloc+path
		a = open('ssss.txt','r+')
		for i in a:
		param = i.strip()
		self.dede(scheme,netloc,path,param)
		return self.parse_output(result)

	def parse_output(self, result):
		output=''
		return output

	def _attack(self):
		return self._verify()

register_poc(HoutaiBoom)
