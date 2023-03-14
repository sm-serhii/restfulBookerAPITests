import requests

from utils.logger import Logger

""" HTTP Methods List """


class Http_method:
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    cookie = ""

    """ GET """

    @staticmethod
    def get(url):
        Logger.add_request(url, method="GET")
        result = requests.get(url, headers=Http_method.headers, cookies=Http_method.cookie)
        Logger.add_response(result)
        return result

    """ POST """

    @staticmethod
    def post(url, body):
        Logger.add_request(url, method="POST")
        result = requests.post(url, json=body, headers=Http_method.headers, cookies=Http_method.cookie)
        Logger.add_response(result)
        return result

    """ PUT """

    @staticmethod
    def put(url, body, headers):
        Logger.add_request(url, method="PUT")
        result = requests.put(url, json=body, headers=headers, cookies=Http_method.cookie)
        Logger.add_response(result)
        return result

    """ PATCH """

    @staticmethod
    def patch(url, body, headers):
        Logger.add_request(url, method="PATCH")
        result = requests.patch(url, json=body, headers=headers, cookies=Http_method.cookie)
        Logger.add_response(result)
        return result

    """ DELETE """

    @staticmethod
    def delete(url, headers):
        Logger.add_request(url, method="DELETE")
        result = requests.delete(url, headers=headers, cookies=Http_method.cookie)
        Logger.add_response(result)
        return result
