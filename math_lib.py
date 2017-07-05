def summ(data):
    return "{0}+{1}={2}".format(data[1],data[2],data[1]+data[2])

def sum_all(data):
    ret_list=list()
    for i in data:
        ret_list.append(summ(i))
    return ret_list

math_dict = {
    "sum": summ,
    "summ_all":sum_all,
}

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from SocketServer import ThreadingMixIn
import threading
import argparse
import re
import cgi
import json

class HTTPRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if None != re.search('/api/v1/addrecord/*', self.path):
            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
            if ctype == 'application/json':
                length = int(self.headers.getheader('content-length'))
                content_len = int(self.headers.getheader('content-length', 0))
                post_body = self.rfile.read(content_len)
                print post_body
                j_data = json.loads(post_body)
                print j_data
                recordID = self.path.split('/')[-1]
                LocalData.records[recordID] = j_data
                print "record %s is added successfully" % recordID
            else:
                data = {}
            self.send_response(200)
            self.end_headers()
        else:
            self.send_response(403)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
return