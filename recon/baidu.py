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


class Baidu(Request):
    def __init__(self, target):
        super(Baidu, self).__init__()
        self.target = target

    def search(self):
        test('Searching "%s" in Baidu...' % self.target)
        url = "http://www.baidu.com/s?wd=%40{target}&pn=0".format(
            target=self.target)
        try:
            resp = self.send(method='GET', url=url, headers={'Host': 'www.baidu.com'})
        except requests.exceptions.RequestException:
            raise
        else:
            getemail(resp.content, self.target)
