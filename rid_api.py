import requests

def test_creds(s, url, username, password):
    id = s.get(url).json()['id']
    resp = s.post(url, json={
        'id'       : id,
        'type'     : 'username+password',
        'username' : username,
        'password' : password
    }).json()
    valid = resp['type'] == 'complete'
    return valid

def test_list(s, url, username, password_list):
    for password in password_list:
        parsed_password = password.strip("\n")
        valid_pass = test_creds(s, url, username, parsed_password)
        if valid_pass:
            with open('password', 'w') as f:
                f.write(parsed_password)
        print(username, ":","Testing", parsed_password[0:30].ljust(30), valid_pass)