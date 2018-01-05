from urllib.parse import urlparse
import requests
import json


class LaundryService:

    def __init__(self,  host, machineId, token):
        self.token = token
        self.id = int(machineId)

        # Add http scheme if no scheme was provided.
        if '//' not in host:
            host = '%s%s' % ('http://', host)

        parsedHost= urlparse(host)
        self.host = parsedHost.scheme +'://'+ parsedHost.netloc

    def push(self, seconds):
        # Construct the Laundry Service URL.
        url = "%s/api/machines/%d/machine_states" % (self.host, self.id)

        # Make the request.
        response = requests.post(
            url=url,
            headers={
                "MachineToken": self.token,
                "Content-Type": "application/json; charset=utf-8",
            },
            data=json.dumps({
                "seconds_remaining": seconds
            })
        )

        # Return True if response status code is 200, False otherwise.
        return True if response.status_code == 200 else False
