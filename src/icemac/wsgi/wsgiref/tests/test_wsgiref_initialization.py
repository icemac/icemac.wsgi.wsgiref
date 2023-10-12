##############################################################################
#
# Copyright (c) 2019-2023 Jens Vagelpohl and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
import unittest
from wsgiref.simple_server import WSGIRequestHandler

from icemac.wsgi.wsgiref import WSGIServer
from icemac.wsgi.wsgiref import serve_paste


SERVER = {}


def fake_init(self, server_address, request_handler):
    global SERVER
    SERVER.clear()

    SERVER['host'], SERVER['port'] = server_address
    SERVER['request_handler'] = request_handler


def noop(self):
    pass


class WsgirefInitializationTests(unittest.TestCase):

    def setUp(self):
        self.orig_init = WSGIServer.__init__
        WSGIServer.__init__ = fake_init
        self.orig_serve_forever = WSGIServer.serve_forever
        WSGIServer.serve_forever = noop

    def tearDown(self) -> None:
        WSGIServer.__init__ = self.orig_init
        WSGIServer.serve_forever = self.orig_serve_forever

    def test_initialization(self):
        global SERVER

        # The defaults
        serve_paste(None, None)
        self.assertEqual(SERVER['host'], '')
        self.assertEqual(SERVER['port'], False)
        self.assertEqual(SERVER['request_handler'], WSGIRequestHandler)

        # Host and port set
        serve_paste(None, None, host='localhost', port='8888')
        self.assertEqual(SERVER['host'], 'localhost')
        self.assertEqual(SERVER['port'], 8888)
