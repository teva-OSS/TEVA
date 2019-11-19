vpc_template = '''
resource "{type}" "{name}" {
    cidr_block = "{cidr_block}"
    instance_tenancy = "{instance_tenancy}"
    enable_dns_support = "{enable_dns_support}"
    enable_dns_hostnames = "{enable_dns_hostnames}"
    enable_classiclink = "{enable_classic_link}"
    enable_classic_link_dns_support = "{enable_classic_link_dns_support}"
    enable_generated_ipv6_cidr_block = "{enable_generated_ipv6_cidr_block}"
    tags = {tags}
}
'''
