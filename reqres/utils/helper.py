import json


def verify_status_code(expected_status_code, actual_status_code):
    """
    This method is used to verify the status code returned in the response against the expected.
    :param int expected_status_code: Exepcted status code for the response
    :param int actual_status_code: Actual status code returned in the response
    :return None
    """
    assert actual_status_code == expected_status_code, "{} status code was expected, but found {}".format(
        expected_status_code, actual_status_code)


def get_response_json(resp):
    """
    This method is used to return the json response from the response object.
    :param object resp: response object of the response
    :return: None
    """
    return json.loads(resp.text)
