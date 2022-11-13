import requests

def test_creds(s, url, username, password):
    id = s.get(url).json()['id']
    valid = s.post(url, json={
        'id'       : id,
        'type'     : 'username+password',
        'username' : username,
        'password' : password
    }).json()['type'] == 'complete'
    print(valid)