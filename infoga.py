#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
#
# @name   : Infoga - Email Information Gathering
# @url    : http://github.com/m4ll0k
# @author : Momo Outaadi (m4ll0k)

import sys
import json
import getopt
# import lib modules
from lib.check import *
from lib.banner import Banner 
from lib.output import *
# import recon modules
from recon.ask import *
from recon.baidu import *
from recon.bing import *
from recon.pgp import *
from recon.yahoo import *
from recon.dogpile import *
from recon.exalead import *
from recon.google import *
from recon.pwned import *
from recon.shodan import *
from recon.mailtester import *

class infoga(object):
	""" infoga """
	def __init__(self):
		self.verbose = 1
		self.domain = None
		self.breach = False
		self.source = "all"
		self.listEmail = []

	def search(self,module):
		emails = module.search()
		if emails != ([] or None):
			for email in emails:
				if email not in self.listEmail:
					self.listEmail.append(email)
			if self.verbose == 2 or self.verbose == 3:
				info('Found %s emails in %s'%(len(emails),
					module.__class__.__name__))

	def engine(self,target,engine):
		engine_list = [ Ask(target),Baidu(target),Bing(target),Dogpile(target),
						Exalead(target),Google(target),PGP(target),Yahoo(target)
						]
		if engine == 'all':
			for e in engine_list: self.search(e)
		else:
			for e in engine_list:
				if e.__class__.__name__.lower() in engine:self.search(e)

	def shodan(self,ip):
		return Shodan(ip).search()

	def tester(self,email):
		return MailTester(email).search()

	def pwned(self,email):
		return Pwned(email).search()

	def main(self):
		if len(sys.argv) <= 2:Banner().usage(True)
		try:
			opts,args = getopt.getopt(sys.argv[1:],'d:s:i:v:hb',
				['domain=','source=','info=','breach','verbose=','help'])
		except Exception as e:
			Banner().usage(True)
		Banner().banner()
		for o,a in opts:
			if o in ('-d','--domain'):self.domain=checkTarget(a)
			if o in ('-v','--verbose'):self.verbose=checkVerbose(a)
			if o in ('-s','--source'):self.source=checkSource(a)
			if o in ('-b','--breach'):self.breach=True
			if o in ('-i','--info'):self.listEmail.append(checkEmail(a))
			if o in ('-h','--help'):usage(True)
		### start ####
		print 
		if self.domain != ('' or None):
			if self.source == 'ask':self.engine(self.domain,'ask')
			if self.source == 'all':self.engine(self.domain,'all')
			if self.source == 'google':self.engine(self.domain,'google')
			if self.source == 'baidu':self.engine(self.domain,'baidu')
			if self.source == 'bing':self.engine(self.domain,'bing')
			if self.source == 'dogpile':self.engine(self.domain,'dogpile')
			if self.source == 'exalead':self.engine(self.domain,'exalead')
			if self.source == 'pgp':self.engine(self.domain,'pgp')
			if self.source == 'yahoo':self.engine(self.domain,'yahoo')
		if self.listEmail == ([] or None):exit(warn('Not found emails... :('))
		for email in self.listEmail:
			ip = self.tester(email)
			if ip != ([] or None):
				for i in ip: # search info and print info :)
					data(i,json.loads(self.shodan(i)),email,self.verbose)
					if self.breach:ppwned(self.pwned(email),self.verbose)
			else:more('Not found any informations for %s'%(email))
		# end
if __name__ == "__main__":
	try:
		infoga().main()
	except KeyboardInterrupt as e:
		exit(warn('CTRL+C: %s'%e))