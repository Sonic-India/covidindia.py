import http.client
import json
import objectpath
import mimetypes
conn = http.client.HTTPSConnection("api.covid19india.org")
payload = ''
headers = {}
conn.request("GET", "/state_district_wise.json", payload, headers)
res = conn.getresponse()
data = res.read()
#print(data.decode("utf-8"))
data = json.loads(data.decode())
jsonnn_tree = objectpath.Tree(data['Maharashtra'])
result_tuple = tuple(jsonnn_tree.execute('$..Solapur'))
print(result_tuple)
