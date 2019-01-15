#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#
# @name   : Infoga - Email OSINT
# @url    : http://github.com/m4ll0k
# @author : Momo Outaadi (m4ll0k)

import urllib3
import requests
from lib.output import *


class Request(object):
	"""Create an object for the requests."""
	agent = ''

	def send(self, method, url, params=None, data=None, headers=None):
		"""Create the request."""
		if headers is None:
			headers = {}

		headers['User-Agent'] = Request.agent

		try:
			session = requests.Session()
			req = urllib3.disable_warnings(
				urllib3.exceptions.InsecureRequestWarning)
			req = requests.request(
				method=method.upper(),
				url=url,
				params=params,
				data=data,
				allow_redirects=True,
				verify=False,
				timeout=10)
			return req
		except Exception as e:
			exit(warn('Failed to establish a new connection'))
