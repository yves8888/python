import urllib.request,json
url = r"http://www.tps138.brady2/test/t_amp"
data = {
        'id': 'true',
        'anme': 'Python'
    }
data = urllib.parse.urlencode(data).encode('utf-8');

req = urllib.request.Request(url,data)
response = urllib.request.urlopen(req)

page = response.read().decode('utf-8')
page = json.loads(page)
print(page)

for  key in page:
    print(key)

