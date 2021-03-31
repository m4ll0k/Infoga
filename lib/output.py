#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#
# @name   : Infoga - Email OSINT
# @url    : http://github.com/m4ll0k
# @author : Momo Outaadi (m4ll0k)

import sys
import json
from lib.colors import *
from recon.pwned import *
from recon.shodan import *


def plus(string): print("%s[+]%s %s" % (G % 0, E, string))


def warn(string): print("%s[!]%s %s" % (R % 0, E, string))


def test(string): print("%s[*]%s %s" % (B % 0, E, string))


def info(string): print("%s[i]%s %s" % (Y % 0, E, string))


def more(string): print(" %s|%s  %s" % (W % 0, E, string))


class PPrint(object):
    """
    PPrint class
    """

    def __init__(self, ips, email, ver, pwned=False, report=None):
        self.ips = ips
        self.s_data = None
        self.email = email
        self.verbose = ver
        self.spaces = lambda x: ' ' * x
        self.separator = lambda x: '-' * x
        self.pwned = pwned
        self.file = None
        if report:
            self.file = report

    def output(self):
        data = None
        # if verbose 1
        if self.verbose == 1:
            email = 'Email: %s (%s)' % (self.email, ', '.join([x for x in self.ips]))
            plus(email)
            if self.file:
                self.file.write('[+] ' + email + '\n')
            if self.pwned:
                data = Pwned(self.email).search()
                if data is None:
                    print('%s>> This email wasn\'t leaked' % self.spaces(1))
                    if self.file:
                        self.file.write('%s>> This email wasn\'t leaked\n' % self.spaces(1))
                elif data.has_key('Breaches'):
                    if data.get('Breaches') is None and data.has_key('Breaches'):
                        data.pop('Breaches')
                        data['Breaches'] = data.pop('Pastes')
                    headers = '%s>> This email was leaked... found %s results' % (self.spaces(1), len(data['Breaches']))
                    if self.file:
                        self.file.write(headers + '\n')
                    print(headers)
            if self.file:
                self.file.writelines(self.separator(30) + '\n')
        # if verbose 2
        elif self.verbose == 2:
            email = 'Email: %s (%s)' % (self.email, ', '.join([x for x in self.ips]))
            plus(email)
            if self.file:
                self.file.write('[+] ' + email + '\n')
            if self.ips:
                data = json.loads(Shodan(self.ips[0]).search())
                if isinstance(data, dict):
                    data = None
            if data:
                headers = ''
                if data.has_key('hostnames'):
                    headers += '%s- Hostname: %s\n' % (self.spaces(1), data.get('hostnames')[0])
                if data.has_key('country_code') and data.has_key('country_name'):
                    headers += '%s- Country: %s (%s)\n' % (
                        self.spaces(1), data.get('country_code'), data.get('country_name'))
                if data.has_key('city') and data.has_key('region_code'):
                    headers += '%s- City: %s (%s)' % (self.spaces(1), data.get('city'), data.get('region_code'))
                if self.file:
                    self.file.write(headers + '\n')
                print(headers)
            else:
                info('Not found information (on shodan) for this email, search this ip/ips on internet..')
                if self.file:
                    self.file.write(
                        '%s- Not found information (on shodan) for this email, search this ip/ips on internet..')
            if self.pwned:
                headers = ''
                data = Pwned(self.email).search()
                if data is None:
                    print('%s>> This email wasn\'t leaked' % self.spaces(1))
                    if self.file:
                        self.file.write('%s>> This email wasn\'t leaked\n' % (self.spaces(1)))
                    headers += '%s\n' % self.separator(30)
                elif data.has_key('Breaches'):
                    if data.get('Breaches') is None and data.has_key('Breaches'):
                        data.pop('Breaches')
                        data['Breaches'] = data.pop('Pastes')
                    headers = '%s>> This email was leaked... found %s results...\n' % (
                        self.spaces(1), len(data['Breaches']))
                    for i in range(0, len(data['Breaches'])):
                        if data['Breaches'][i].has_key('Title'):
                            headers += '%s> Leaked in: %s\n' % (self.spaces(2), data['Breaches'][i].get('Title'))
                        if data['Breaches'][i].has_key('BreachDate'):
                            headers += '%s> Data Leaked: %s\n' % (self.spaces(2), data['Breaches'][i].get('BreachDate'))
                        if data['Breaches'][i].has_key('IsVerified'):
                            headers += '%s> Verified: %s\n' % (self.spaces(2), data['Breaches'][i].get('IsVerified'))
                        headers += '%s%s\n' % (self.spaces(2), self.separator(30))
                    if self.file:
                        self.file.write(headers.encode('utf-8'))
                    print(headers.encode('utf-8'))
        # if verbose 3
        elif self.verbose == 3:
            email = 'Email: %s (%s)' % (self.email, ', '.join([x for x in self.ips]))
            plus(email)
            if self.file:
                self.file.write('[+] ' + email + '\n')
            if self.ips:
                data = json.loads(Shodan(self.ips[0]).search())
                if data == {}:
                    data = None
            if data:
                headers = ''
                print(data.has_key('hostnames'))
                exit()
                if data.has_key('hostnames'):
                    headers += '%s- Hostname: %s\n' % (self.spaces(1), data.get('hostnames')[0])
                if data.has_key('country_code') and data.has_key('country_name'):
                    headers += '%s- Country: %s (%s)\n' % (
                        self.spaces(1), data.get('country_code'), data.get('country_name'))
                if data.has_key('city') and data.has_key('region_code'):
                    headers += '%s- City: %s (%s)\n' % (self.spaces(1), data.get('city'), data.get('region_code'))
                if data.has_key('asn'):
                    headers += '%s- ASN: %s\n' % (self.spaces(1), data.get('asn'))
                if data.has_key('isp'):
                    headers += '%s- ISP: %s\n' % (self.spaces(1), data.get('isp'))
                if data.has_key('latitude') and data.has_key('longitude'):
                    headers += '%s- Map: https://www.google.com/maps/@%s,%s,10z (%s,%s)\n' % (
                        self.spaces(1), data.get('latitude'), data.get('longitude'),
                        data.get('latitude'), data.get('longitude')
                    )
                if data.has_key('org'):
                    headers += '%s- Organization: %s\n' % (self.spaces(1), data.get('org'))
                if data.has_key('ports'):
                    headers += '%s- Ports: %s' % (self.spaces(1), ', '.join([str(x) for x in data.get('ports')]))

                if headers != '':
                    if self.file:
                        self.file.write(headers)
                    print(headers)
            else:
                info('Not found information (on shodan) for this email, search this ip/ips on internet..')
                if self.file:
                    self.file.write(
                        '%s- Not found information (on shodan) for this email, search this ip/ips on internet..')
            if self.pwned:
                headers = ''
                data = Pwned(self.email).search()
                if data is None:
                    print('%s>> This email wasn\'t leaked' % self.spaces(1))
                    if self.file:
                        self.file.write('%s>> This email wasn\'t leaked\n' % (self.spaces(1)))
                elif data.has_key('Breaches'):
                    if data.get('Breaches') is None and data.has_key('Breaches'):
                        data.pop('Breaches')
                        data['Breaches'] = data.pop('Pastes')
                    headers = '%s>> This email was leaked... found %s results...\n' % (
                        self.spaces(1), len(data['Breaches']))
                    for i in range(0, len(data['Breaches'])):
                        if data['Breaches'][i].has_key('Title'):
                            headers += '%s> Leaked in: %s\n' % (self.spaces(2), data['Breaches'][i].get('Title'))
                        if data['Breaches'][i].has_key('BreachDate'):
                            headers += '%s> Data Leaked: %s\n' % (self.spaces(2), data['Breaches'][i].get('BreachDate'))
                        if data['Breaches'][i].has_key('IsVerified'):
                            headers += '%s> Verified: %s\n' % (self.spaces(2), data['Breaches'][i].get('IsVerified'))
                        if data['Breaches'][i].has_key('Description'):
                            headers += '%s> Description: %s\n' % (
                                self.spaces(2), data['Breaches'][i].get('Description'))
                        headers += '%s%s\n' % (self.spaces(2), self.separator(30))

                    if self.file:
                        self.file.write('\n' + headers.encode('utf-8'))
                    print(headers.encode('utf-8'))
