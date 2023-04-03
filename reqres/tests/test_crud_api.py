from reqres.utils import rest
from reqres.utils.helper import *

# Define the base URL of the API
base_url = "https://reqres.in"

post_req_body = {
        'id': '2',
        'first_name': 'Janet',
        'last_name': 'Caren'
    }

update_req_body = {
        'id': '2',
        'first_name': 'Janet',
        'last_name': 'Weaver'
    }


def test_status_codes():
    # Verify the status codes for various API Calls
    get_resp = rest.get(base_url)
    verify_status_code(200, get_resp.status_code)

    post_resp = rest.post(base_url + "/api/users", post_req_body)
    verify_status_code(201, post_resp.status_code)

    put_resp = rest.put(base_url + "/api/users/2", update_req_body)
    verify_status_code(200, put_resp.status_code)

    delete_resp = rest.delete(base_url + "/api/users/2")
    verify_status_code(204, delete_resp.status_code)

    get_resp = rest.get(base_url + "/api/users/23")
    verify_status_code(404, get_resp.status_code)


def test_validate_response_time():
    # Validating the Response time for the API response.
    resp = rest.get(base_url)
    # Validating that the response time is less than 1 second
    assert resp.elapsed.total_seconds() < 1, "Time taken to get the response is more than a second"


def test_validate_response_data():
    # Validating the response data for API response.
    req_body = {
        "name": "morpheus",
        "job": "leader"
    }
    resp = rest.post(base_url + "/api/users", req_body)
    resp_json = get_response_json(resp)

    verify_status_code(201, resp.status_code)
    assert req_body['name'] == resp_json['name'], "Expected name is {}, but found {}".format(req_body['name'], resp_json['name'])
    assert req_body['job'] == resp_json['job'], "Expected job is {}, but found {}".format(req_body['job'], resp_json['job'])

    # Validation the response is returned in json() format
    assert 'application/json' in resp.headers['Content-Type'], "Response is expected in json, but it is not".format(req_body['job'], resp_json['job'])


def test_endpoints():
    # Verifying the API Responses for the POST call.
    resp = rest.post(base_url + "/api/users", post_req_body)
    verify_status_code(201, resp.status_code)
    resp_json = get_response_json(resp)
    assert post_req_body['id'] == resp_json['id'], "Expected ID is {}, but found {}".format(post_req_body['id'], resp_json['id'])
    assert post_req_body['first_name'] == resp_json['first_name'], "Expected name is {}, but found {}".format(post_req_body['name'], resp_json['name'])
    assert post_req_body['last_name'] == resp_json['last_name'], "Expected job is {}, but found {}".format(post_req_body['job'], resp_json['job'])

    # Verifying the API Responses for the PUT call.
    put_resp = rest.put(base_url + "/api/users/2", update_req_body)
    verify_status_code(200, put_resp.status_code)
    put_resp_json = get_response_json(put_resp)
    assert update_req_body['id'] == put_resp_json['id'], "Expected ID is {}, but found {}".format(update_req_body['id'], put_resp_json['id'])
    assert update_req_body['first_name'] == put_resp_json['first_name'], "Expected first_name is {}, but found {}".format(update_req_body['first_name'], put_resp_json['first_name'])
    assert update_req_body['last_name'] == put_resp_json['last_name'], "Expected last_name is {}, but found {}".format(update_req_body['last_name'], put_resp_json['last_name'])

    # Verifying the API Responses for the GET call.
    get_resp = rest.get(base_url + "/api/users/2")
    verify_status_code(200, get_resp.status_code)
    get_resp_json = get_response_json(get_resp)
    assert update_req_body['id'] == str(get_resp_json['data']['id']), "Expected ID is {}, but found {}".format(update_req_body['id'], get_resp_json['id'])
    assert update_req_body['first_name'] == get_resp_json['data']['first_name'], "Expected first_name is {}, but found {}".format(update_req_body['first_name'], get_resp_json['data']['first_name'])
    assert update_req_body['last_name'] == get_resp_json['data']['last_name'], "Expected last_name is {}, but found {}".format(update_req_body['last_name'], get_resp_json['data']['last_name'])

    # Verifying the API Responses for the DELETE call.
    delete_resp = rest.delete(base_url + "/api/users/2")
    verify_status_code(204, delete_resp.status_code)

