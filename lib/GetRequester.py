import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        """Query the endpoint and return the raw response body as bytes"""
        response = requests.get(self.url)
        return response.content


    def load_json(self):
        """Convert the endpoint data to JSON and return parsed data"""
        response_body = self.get_response_body()
        return json.loads(response_body)
    