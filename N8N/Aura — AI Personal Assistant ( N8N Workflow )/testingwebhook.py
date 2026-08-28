import requests

url="http://localhost:5678/webhook-test/765f700b-7da7-42f9-aa13-887c8f64a338"

data="hi my name is ahmad nawaz."
a={"name":data,
   "sessionId":"ello"}


response=requests.post(url,json=a)

print(response.status_code)
print(response)