import requests
from requests.adapters import HTTPAdapter

class NoVerifyAdapter(HTTPAdapter):
    def init_poolmanager(self, *args, **kwargs):
        kwargs['ssl_context'].check_hostname = False
        kwargs['ssl_context'].verify_mode = False
        super().init_poolmanager(*args, **kwargs)

# Mount the adapter with the session
session = requests.Session()
session.mount('https://', NoVerifyAdapter())

# Test a request
response = session.get('https://facebook.com')
print(response.content)
