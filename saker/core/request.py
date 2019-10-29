#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import requests


class Request(object):

    def __init__(self, options={}, sess=None):
        """Summary

        Args:
            sess (requests.sessions.Session): request Session
            options (saker.core.Request): request object
        """
        super(Request, self).__init__()
        if sess is None:
            self.sess = requests.Session()
        else:
            self.sess = sess
        self.method = options.get('method', 'get').lower()
        if not self.method:
            self.method = 'get'
        self.url = options.get('url', '')
        self.params = options.get('params', {})
        self.data = options.get('data', {})
        self.files = options.get('files', {})
        self.headers = options.get('headers', {})
        self.cookies = options.get('cookies', {})
        self.interval = 0

    def submit(self):
        start = time.time()
        self.lastr = getattr(self.sess, self.method)(
            self.url, params=self.params, data=self.data, files=self.files,
            headers=self.headers, cookies=self.cookies
        )
        self.interval = time.time() - start
        return self.lastr

    def brief(self):
        return "%s\t%s\t%s" % (self.lastr.status_code, len(self.lastr.content), self.interval)