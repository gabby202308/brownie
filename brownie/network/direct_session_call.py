import requests

def make_direct_request(method, url, headers=None, params=None, data=None, json=None):
    # Step 1: Create a session object
    session = requests.Session()

    # Step 2: Create a Request object (without sending it yet)
    req = requests.Request(method=method, url=url, headers=headers, params=params, data=data, json=json)

    # Step 3: Prepare the request (this converts it to a PreparedRequest object)
    prepared_request = session.prepare_request(req)

    # Step 4: Send the prepared request using session.send()
    response = session.send(prepared_request)

    # Step 5: Return or process the response (for example, return the status code and text)
    return response.status_code, response.text


# Example usage of the function
status_code, content = make_direct_request(
    method='GET', 
    url='https://httpbin.org/get', 
    headers={'User-Agent': 'my-app'},
    params={'key': 'value'}
)

print(f'Status Code: {status_code}')
print(f'Content: {content}')
