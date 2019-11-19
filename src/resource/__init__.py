import aws
import gcp
import ibm_cloud


resource_map = {
    'aws': aws.resource_map,
    'gcp': gcp.resource_map,
    'ibm_cloud': ibm_cloud.resource_map,
}
