from oauth2client.service_account import ServiceAccountCredentials
import httplib2
import googleapiclient
import time
global urls

with open("pages.txt") as f:
    urls = f.readlines()
    pass
    i = 0
    urls = ([s.strip('\n') for s in urls])

for urlindexing in urls:
    #action = "URL_DELETED"
    action = "URL_UPDATED"
    SCOPES = ["https://www.googleapis.com/auth/indexing"]
    ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"

    # service_account_file.json is the private key that you created for your service account.
    JSON_KEY_FILE = "service_account_file.json"

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
    JSON_KEY_FILE, scopes=SCOPES)

    http = credentials.authorize(httplib2.Http())

    content = "{{\"url\": \"{0}\",\"type\": \"{1}\"}}".format(urlindexing,action)
    response, content = http.request(ENDPOINT, method="POST", body=content)

    #print(response)
    print("\n")
    print("URL address: {}".format(urlindexing))
    print("Request status code: {}".format(response.status))
    print("Request status: {}".format(response.reason))
    print("Request type: {}".format(action))
    print("\n")
    #print(content)