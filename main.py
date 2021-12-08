import http.client
import json
import objectpath
import mimetypes
conn = http.client.HTTPSConnection("data.covid19india.org")
payload = ''
headers = {}
conn.request("GET", "/v4/min/data.min.json", payload, headers)
res = conn.getresponse()
data = res.read()
#print(data.decode("utf-8"))
data = json.loads(data.decode())
jsonnn_tree = objectpath.Tree(data['MH'])
result_tuple = tuple(jsonnn_tree.execute('$..Solapur'))
print(result_tuple)
