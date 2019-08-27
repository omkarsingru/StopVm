import sys
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.compute.models import DiskCreateOption

from st2common.runners.base_action import Action
class MyEchoAction(Action):
    def run(self, SUBSCRIPTION_ID,GROUP_NAME,LOCATION,VM_NAME,client_id, secret,tenant):
		get_credentials()
		resource_group_client = ResourceManagementClient(credentials,SUBSCRIPTION_ID)
                network_client = NetworkManagementClient(credentials,SUBSCRIPTION_ID)
                compute_client = ComputeManagementClient(credentials,SUBSCRIPTION_ID)
	        stop_vm(compute_client)
	

def get_credentials():
    credentials = ServicePrincipalCredentials(client_id,secret,tenant)
     return credentials

def stop_vm(compute_client):
input('Press enter to continue...')
    compute_client.virtual_machines.power_off(GROUP_NAME, VM_NAME)


  

