import aws
import gcp
import ibm_cloud


template_map = {
    'aws': aws.template_map,
    'gcp': gcp.template_map,
    'ibm_cloud': ibm_cloud.template_map,
}
