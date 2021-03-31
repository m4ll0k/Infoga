#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#
# @name   : Infoga - Email OSINT
# @url    : http://github.com/m4ll0k
# @author : Momo Outaadi (m4ll0k)

import sys
import json
import getopt
# infoga.lib
from lib.check import *
from lib.output import *
from lib.banner import Banner
# infoga.recon
from recon.ask import *
from recon.baidu import *
from recon.bing import *
from recon.pgp import *
from recon.yahoo import *
from recon.dogpile import *
from recon.exalead import *
from recon.google import *
from recon.mailtester import *
from lib.output import PPrint


def tester(email):
    return MailTester(email).search()


class infoga(object):
    """ infoga """

    def __init__(self):
        self.verbose = 1
        self.domain = None
        self.breach = False
        self.source = "all"
        self.listEmail = []
        self.report = None

    def search(self, module):
        emails = module.search()
        # precise check that emails exist that is is not none
        if not emails:
            raise ValueError("No e-mails were found")
        for email in emails:
            self.listEmail.append(email) if email not in self.listEmail else print("{} already in emails".format(email))

        if self.verbose in (1, 2, 3):
            info('Found %s emails in %s' % (len(emails),
                                            module.__class__.__name__))

    def engine(self, target, engine):
        engine_list = [Ask(target), Baidu(target), Bing(target), Dogpile(target),
                       Exalead(target), Google(target), PGP(target), Yahoo(target)
                       ]

        for eng in engine_list:
            print(
                "Engine not found") if engine != "all" and eng.__class__.__name__.lower() not in engine \
                else self.search(eng)

    def main(self):
        if len(sys.argv) <= 2: Banner().usage(True)
        try:
            opts, args = getopt.getopt(sys.argv[1:], 'd:s:i:v:r:hb',
                                       ['domain=', 'source=', 'info=', 'breach', 'verbose=', 'help', 'report='])
        except getopt.GetoptError:
            Banner().usage(True)
        else:
            Banner().banner()
            for option, arg in opts:
                if option in ('-d', '--domain'): self.domain = checkTarget(arg)
                if option in ('-v', '--verbose'): self.verbose = checkVerbose(arg)
                if option in ('-s', '--source'): self.source = checkSource(arg)
                if option in ('-b', '--breach'): self.breach = True
                if option in ('-r', '--report'): self.report = open(arg, 'w') if arg else None
                if option in ('-i', '--info'):
                    self.listEmail.append(checkEmail(arg))
                    plus('Searching for: %s' % arg)
                if option in ('-h', '--help'): Banner().usage(True)
        ### start ####
        if self.domain != ('' or None):
            if self.source == 'ask': self.engine(self.domain, 'ask')
            if self.source == 'all': self.engine(self.domain, 'all')
            if self.source == 'google': self.engine(self.domain, 'google')
            if self.source == 'baidu': self.engine(self.domain, 'baidu')
            if self.source == 'bing': self.engine(self.domain, 'bing')
            if self.source == 'dogpile': self.engine(self.domain, 'dogpile')
            if self.source == 'exalead': self.engine(self.domain, 'exalead')
            if self.source == 'pgp': self.engine(self.domain, 'pgp')
            if self.source == 'yahoo': self.engine(self.domain, 'yahoo')

        if not self.listEmail:
            sys.exit(warn('No emails found... :('))

        for email in self.listEmail:
            ip = tester(email)
            if ip:
                ips = []
                for i in ip:
                    if i not in ips: ips.append(i)
                if len(ips) >= 2:
                    info("Found multiple ip for this email...")
                PPrint(ips, email, self.verbose, self.breach, self.report).output()
            else:
                more('Not found any informations for %s' % (email))
        if self.report:
            info('File saved in: ' + self.report.name)
            self.report.close()
    # end


if __name__ == "__main__":
    try:
        infoga().main()
    except KeyboardInterrupt as e:
        sys.exit(warn('Exiting...'))
