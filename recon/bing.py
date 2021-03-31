#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#
# @name   : Infoga - Email Information Gathering
# @url    : http://github.com/m4ll0k
# @author : Momo Outaadi (m4ll0k)

from lib.output import *
from lib.request import *
from lib.parser import *


def getemail(content, target):
	return parser(content, target).email()


class Bing(Request):
    def __init__(self, target):
        super(Bing, self).__init__()
        self.target = target

    def search(self):
        test('Searching "%s" in Bing...' % self.target)
        url = "http://bing.com/search?q=%40{target}".format(target=self.target)
        try:
            resp = self.send(method='GET', url=url,
                             headers={'Cookie': 'SRCHHPGUSR=ADLT=DEMOTE&NRSLT=100'})
        except requests.exceptions.RequestException:
            raise
        else:
            getemail(resp.content, self.target)
