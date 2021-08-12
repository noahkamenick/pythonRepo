import requests
from requests.auth import HTTPBasicAuth
from dnac_config import DNAC_IP, USERNAME, PASSWORD

requests.packages.urllib3.disable_warnings()