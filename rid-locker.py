import requests
import rid_api
from threading import Thread

api_url = "https://portal.id.cps.edu/api/rest/authn"
session = requests.session()

thread = Thread(target=rid_api.test_creds, args=(session, api_url, "brogozinski", "Creeper10227"))
thread.start()

#rid_api.test_creds(session, api_url, "bogozinski", "Creeper10227")