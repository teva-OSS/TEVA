resource "aws_vpc" "TestVPC" {
    cidr_block = "10.1.0.0/16"
    instance_tenancy = "default"
    enable_dns_support = "true"
    enable_dns_hostnames = "false"
    tags {
      "Name" = ""
    }
}
 
resource "aws_internet_gateway" "TestGW" {
    vpc_id = "${aws_vpc.TestVPC.id}"
    depends_on = "${aws_vpc.TestVPC}"
}
