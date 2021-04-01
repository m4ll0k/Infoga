#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#
# @name   : Infoga - Email Information Gathering
# @url    : http://github.com/m4ll0k
# @author : Momo Outaadi (m4ll0k)

from lib.output import *
from lib.request import *
from lib.parser import *

class Shodan(Request):
	def __init__(self, ip):
		super(Shodan, self).__init__()
		self.ip = ip

	def search(self):
		url = "https://api.shodan.io/shodan/host/{target}?key=UNmOjxeFS2mPA3kmzm1sZwC0XjaTTksy".format(
			target=self.ip)
		try:
			resp = self.send(method = 'GET',url = url)
			resp.raise_for_status()
		except requests.HTTPError:
			raise
		else:
			return resp.content

