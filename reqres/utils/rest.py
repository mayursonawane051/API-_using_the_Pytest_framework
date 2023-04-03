import requests


def post(url, data):
    """
    This method is used to send the POST Request to the server.
    :param string url: endpoint url to send the request
    :param json data: json body to send as payload
    :return: object response: response object returned from the server
    """
    response = requests.post(url, data)
    return response


def get(url):
    """
    This method is used to send the GET Request to the server.
    :param string url: endpoint url to send the request
    :return: object response: response object returned from the server
    """
    response = requests.get(url)
    return response


def put(url, data):
    """
    This method is used to send the PUT Request to the server.
    :param string url: endpoint url to send the request
    :param json data: json body to send as payload
    :return: object response: response object returned from the server
    """
    response = requests.put(url, data)
    return response


def delete(url):
    """
    This method is used to send the DELETE Request to the server.
    :param string url: endpoint url to send the request
    :return: object response: response object returned from the server
    """
    response = requests.delete(url)
    return response
