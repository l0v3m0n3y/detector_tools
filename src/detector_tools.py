import requests
class Client():
	def __init__(self):
		self.headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36","x-requested-with": "XMLHttpRequest"}
		self.api="https://detector.tools/api/v1"
	def ip_info(self,ip):
		data={"ip":ip}
		return requests.post(f"{self.api}/api_info",headers=self.headers,json=data).json()
	def check_email(self,email):
		data={"email":email}
		return requests.post(f"{self.api}/check_email",headers=self.headers,json=data).json()
	def geo_ip(self,ip):
		data={"ip":ip}
		return requests.post(f"{self.api}/geo_ip",headers=self.headers,json=data).json()
	def check_cms(self,site):
		data={"site":site}
		return requests.post(f"{self.api}/check_cms",headers=self.headers,json=data).json()
	def check_port(self,port):
		data={"port":port}
		return requests.post(f"{self.api}/check_port",headers=self.headers,json=data).json()
	def whois(self,address):
		data={"address":address}
		return requests.post(f"{self.api}/whois",headers=self.headers,json=data).json()
	def additional_whois(self,address):
		data={"address":address}
		return requests.post(f"{self.api}/additional_whois",headers=self.headers,json=data).json()
	def dig(self,domain):
		data={"domain":domain}
		return requests.post(f"{self.api}/dig",headers=self.headers,json=data).json()
	def ping(self,ip):
		data={"ip":ip}
		return requests.post(f"{self.api}/ping",headers=self.headers,json=data).json()
	def ipv6_leaks(self):
		return requests.get(f"{self.api}/ipv6_leaks",headers=self.headers).json()
	def rkn_check(self,object):
		data={"object":object}
		return requests.post(f"{self.api}/rkn/check",headers=self.headers,json=data).json()
	def rkn_ad(self,object,contact):
		data={"object":object,"contact":contact}
		return requests.post(f"{self.api}/rkn/add",headers=self.headers,json=data).json()
	def short_url(self,link):
		data={"link":link}
		return requests.post(f"{self.api}/shorten",headers=self.headers,json=data).json()
	def ip_calc(self,ip):
		return  requests.get(f"{self.api}/ip-calc?ip={ip}",headers=self.headers).json()
	def spam_chek(self,ip):
		return  requests.get(f"{self.api}/spam-check/?ip={ip}",headers=self.headers).json()
	def pass_leak(self,email):
		return  requests.get(f"{self.api}/pass-leak/?query={email}",headers=self.headers).json()
	def dns_leak(self):
		return  requests.get(f"{self.api}/dns_leak/request",headers=self.headers).json()