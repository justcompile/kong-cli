import requests

class API(object):
    def __init__(self, base_url):
        self.base_url = base_url

    def get_api_endpoints(self):
        return self.__get('apis')

    def get_consumer_endpoints(self):
        return self.__get('consumers')

    def __get(self, endpoint):
        req = requests.get(self.base_url+'/{0}/'.format(endpoint))
        if req.status_code == 200:
            return req.json()

        raise Exception(req.json()['message'])
