class Resource(object):
    def __init__(self, json_template):
        self.resource_type = json_template['type']
        self.name = json_template['name']
        self.template = ''
        self.tags = self.__parse_tags(json_template['tags'])

    def generate_tf_template(self):
        mapped_template = self.template.format(self.__dict__)
        return mapped_template

    def __parse_tags(self, tags_dict):
        tags = 'tags = {\n'
        for key, value in tags_dict:
            tags += f'{key} = "{value}"\n'
        tags += '}\n'

        return tags
