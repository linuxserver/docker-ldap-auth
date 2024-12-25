#!/bin/sh
''''which python  >/dev/null && exec python  "$0" "$@" # '''

# Copyright (C) 2014-2015 Nginx, Inc.
# Copyright (C) 2018-2020 LinuxServer.io

# Example of an application working on port 9000
# To interact with nginx-ldap-auth-daemon this application
# 1) accepts GET  requests on /login and /ldaplogin and responds with a login form
# 2) accepts POST requests on /login and /ldaplogin, sets a cookie, and responds with redirect

import sys, os, signal, base64, cgi
if sys.version_info.major == 2:
    from urlparse import urlparse
    from Cookie import BaseCookie
    from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
elif sys.version_info.major == 3:
    from urllib.parse import urlparse
    from http.cookies import BaseCookie
    from http.server import HTTPServer, BaseHTTPRequestHandler

from cryptography.fernet import Fernet

Listen = ('0.0.0.0', 9000)

import threading
if sys.version_info.major == 2:
    from SocketServer import ThreadingMixIn
elif sys.version_info.major == 3:
    from socketserver import ThreadingMixIn


def ensure_bytes(data):
    return data if sys.version_info.major == 2 else data.encode("utf-8")


class AuthHTTPServer(ThreadingMixIn, HTTPServer):
    pass

class AppHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        url = urlparse(self.path)

        # set the proper login page subfolder and serve form
        if url.path.startswith("/login"):
            return self.auth_form(loginsubfolder="/login")
        if url.path.startswith("/ldaplogin"):
            return self.auth_form(loginsubfolder="/ldaplogin")

        self.send_response(200)
        self.end_headers()
        self.wfile.write(ensure_bytes('Hello, world! Requested URL: ' + self.path + '\n'))


    # send login form html
    def auth_form(self, target = None, loginsubfolder = ""):

        # try to get target location from header
        if target == None:
            target = self.headers.get('X-Target')

        # form cannot be generated if target is unknown
        if target == None:
            self.log_error('target url is not passed')
            self.send_response(500)
            return

        html="""
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
    <head>
        <meta http-equiv=Content-Type content="text/html;charset=UTF-8">
        <title>Log In</title>
        <style type="text/css" rel="stylesheet">
            body { background-color: #f1f1f1; font-family: sans-serif,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif; }
            .log-in { width: 400px; height: 500px; position: absolute; top: 0; bottom: 0; left: 0; right: 0; margin: auto; background-color: #fff; border-radius: 3px; overflow: hidden; -webkit-box-shadow: 0px 0px 2px 0px rgba(222,222,222,1); -moz-box-shadow: 0px 0px 2px 0px rgba(222,222,222,1); box-shadow: 0px 0px 2px 0px rgba(222,222,222,1); }
            .log-in > div { position: relative; }
            .log-in .content { margin-top: 50px; padding: 20px; text-align: center; }
            h1, h2 { text-align: center; }
            h1 {  margin-top: 20px; margin-bottom: 20px; letter-spacing: -0.05rem; color: #565656; font-size: 1.6rem; }
            form { margin-top: 50px; }
            input[type="text"], input[type="password"] { width: 80%; padding: 10px; border-top: 0; border-left: 0; border-right: 0; outline: none; }
            input[type="text"]:focus, input[type="password"]:focus { border-bottom: 2px solid #666; }
            button { width: 80%; padding: 10px; background-color: #3468e2; border: none; color: #fff; cursor: pointer; margin-top: 50px; }
            button:hover { background-color: #5581e8; }
        </style>
    </head>
    <body>
        <div class="log-in">
            <div class="content">
                <h1>Log in to your account</h1>
                <form action="LOGINSUBFOLDER" method="post">
                    <p>
                        <input type="text" name="username" placeholder="Username" aria-label="Username" />
                    </p>
                    <p>
                        <input type="password" name="password" placeholder="Password" aria-label="Password" />
                    </p>
                    <!-- <p>
                        <input type="text" name="token" placeholder="2FA Token" aria-label="2FA Token" />
                    </p> -->
                    <input type="hidden" name="target" value="TARGET">
                    <button type="submit" class="submit btn btn-primary">Log In</button>
                </form>
            </div>
        </div>
    </body>
</html>"""

        self.send_response(200)
        self.end_headers()
        self.wfile.write(ensure_bytes(html.replace('TARGET', target).replace('LOGINSUBFOLDER', loginsubfolder)))


    # processes posted form and sets the cookie with login/password
    def do_POST(self):

        # prepare arguments for cgi module to read posted form
        env = {'REQUEST_METHOD':'POST',
               'CONTENT_TYPE': self.headers['Content-Type'],}

        # read the form contents
        form = cgi.FieldStorage(fp = self.rfile, headers = self.headers,
                                environ = env)

        # extract required fields
        user = form.getvalue('username')
        passwd = form.getvalue('password')
        target = form.getvalue('target')

        if user != None and passwd != None and target != None:

            # form is filled, set the cookie and redirect to target
            # so that auth daemon will be able to use information from cookie

            self.send_response(302)

            fernetkey = os.getenv("FERNET_KEY").encode()
            cipher_suite = Fernet(fernetkey)
            enc = cipher_suite.encrypt(ensure_bytes(user + ':' + passwd))
            enc = enc.decode()
            self.send_header('Set-Cookie', 'nginxauth=' + enc + '; httponly')

            self.send_header('Location', target)
            self.end_headers()

            return

        self.log_error('some form fields are not provided')
        self.auth_form(target)


    def log_message(self, format, *args):
        if len(self.client_address) > 0:
            addr = BaseHTTPRequestHandler.address_string(self)
        else:
            addr = "-"

        sys.stdout.write("%s - - [%s] %s\n" % (addr,
                         self.log_date_time_string(), format % args))

    def log_error(self, format, *args):
        self.log_message(format, *args)


def exit_handler(signal, frame):
    sys.exit(0)

if __name__ == '__main__':
    server = AuthHTTPServer(Listen, AppHandler)
    signal.signal(signal.SIGINT, exit_handler)
    server.serve_forever()
