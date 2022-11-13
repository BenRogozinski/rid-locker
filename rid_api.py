import requests

def test_creds(s, url, username, password):
    id = s.get(url).json()['id']
    valid = s.post(url, json={
        'id'       : id,
        'type'     : 'username+password',
        'username' : username,
        'password' : password
    }).json()['type'] == 'complete'
    return valid

def test_list(s, url, username, password_list):
    for password in password_list:
        print("Testing", password.strip('\n')[0:30].ljust(30), test_creds(s, url, username, password.strip('\n')))