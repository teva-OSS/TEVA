import json

from tornado import web


class MainHandler(web.RequestHandler):
    def post(self):
        print(json.loads(self.request.body.decode()))
