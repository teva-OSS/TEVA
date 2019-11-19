import json

from tornado import web

from resource import resource_map


class MainHandler(web.RequestHandler):
    def post(self):
        json_template = json.loads(self.request.body.decode())
        print(json_template)

        cloud = json_template['cloud']
        resources_json = json_template['resources']

        for resource_json in resources_json:
            resource_type = resource_json['type']
            resource = resource_map[cloud][resource_type](resource_json)
            print(resource.resource_type)
