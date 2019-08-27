from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.compute.models import DiskCreateOption

SUBSCRIPTION_ID = '2f50f202-0a84-4c8c-a929-fcc5a3174590'
GROUP_NAME = 'myResourceGroup'
LOCATION = 'West India'
VM_NAME = 'VM61'

def get_credentials():
    credentials = ServicePrincipalCredentials(
        client_id = 'eed2ecc7-e56e-4be3-98e9-d5f8199b33e2',
        secret = 'MTL9_v+/=R0R1AO0*S-35[vaAf?sfnc8',
        tenant = 'd5656af4-b7b3-45b9-9346-fb0547921fb7'
    )

    return credentials

def stop_vm(compute_client):
    compute_client.virtual_machines.power_off(GROUP_NAME, VM_NAME)


if __name__ == "__main__":
     credentials = get_credentials()
     resource_group_client = ResourceManagementClient(
     credentials,
     SUBSCRIPTION_ID
     )
     network_client = NetworkManagementClient(
     credentials,
     SUBSCRIPTION_ID
     )
     compute_client = ComputeManagementClient(
     credentials,
     SUBSCRIPTION_ID
     )

stop_vm(compute_client)
input('Press enter to continue...')