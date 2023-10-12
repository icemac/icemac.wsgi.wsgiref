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
import wsgiref.handlers
from wsgiref.simple_server import WSGIRequestHandler
from wsgiref.simple_server import WSGIServer


def serve_paste(app, global_conf, **kw):
    """ A handler for PasteDeploy-compatible runners.

    Sample .ini configuration:

     [server:main]
     use = egg:icemac.wsgi.wsgiref#main
     host = 127.0.0.1
     port = 8080

    If no host is specified wsgiref will bind to all IPv4 IPs (0.0.0.0)
    If no port is specified, wsgiref will use a random port
    """
    # Convert the values from the .ini file to something wsgiref can work with
    host = kw.get('host', '')
    port = int(kw.get('port', '0'))

    server = WSGIServer((host, port), WSGIRequestHandler)
    server.set_app(app)

    orig_flush = wsgiref.handlers.SimpleHandler._flush

    def silent_flush(self):  # pragma: no cover
        """Silence "error 32: Broken pipe" errors in wsgi.Layer

        They just mean the client closed the connection prematurely, which is
        as harmless as it is normal.
        """
        try:
            orig_flush(self)
        except OSError as e:
            if e.args[0] != 32:
                raise

    wsgiref.handlers.SimpleHandler._flush = silent_flush
    server.serve_forever()

    return 0
