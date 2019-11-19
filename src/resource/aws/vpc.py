import ..common
import ..exception
import ..template


class VPC(common.Resource):
    def __init__(self, json_template):
        super(json_template)
        self.cidr_block = json_template.get('cidr_block', None)
        self.instance_tenancy = json_template['instance_tenancy']
        self.enable_dns_support = json_template['true']
        self.enable_dns_hostnames = json_template['false']
        self.template = template_map['aws']['vpc']

    def generate_tf_template(self):
        if not self.__valid_required_field():
            raise exception.RequiredFieldMissingError()
        return super().generate_tf_template()

    def __valid_required_field(self):
        if self.cidr_block is None:
            return False
        return True
