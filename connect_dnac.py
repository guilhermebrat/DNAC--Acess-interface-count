from dnacentersdk import api
import requests
import json


def connect_dnac():
    dna = api.DNACenterAPI(base_url='https://sandboxdnac.cisco.com',
                           username='devnetuser', password='Cisco123!', verify=False)

    return(dna)
