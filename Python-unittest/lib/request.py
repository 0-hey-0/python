import os
import re
import sys
import json
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from config.MyEncoder import MyEncoder

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


# def request(url, method, data="", header=""):
#     # print(url,method,data,header)
#     if method == "get":
#         res = requests.get(url=url, params=data, headers=header, verify=False)
#         return res.json()
#     if method == "post":
#         # data = json.dumps(data).encode(encoding='utf-8')
#         res = requests.post(url=url, json=data, headers=header, verify=False)
#         return res.json()
#     if method == "put":
#         res = requests.put(url=url, data=data, headers=header, verify=False)
#         return res.json()
#     if method == "delete":
#         res = requests.delete(url=url, data=data, headers=header, verify=False)
#         return res.json()

# def request_get(url, data="", header=""):
#     print(url)
#     res = requests.get(url=url, params=data, headers=header, verify=False)
#     return res.json()
# def request_post_json(url, data="", header=""):
#     res = requests.post(url=url, json=data, headers=header, verify=False)
#     return res.json()
# def request_post(url, data="", header=""):
#     res = requests.post(url=url, data=data, headers=header, verify=False)
#     return res.json()
# def request_put(url, data="", header=""):
#     res = requests.put(url=url, data=data, headers=header, verify=False)
#     return res.json()
# def request_delete(url, data="", header=""):
#     res = requests.delete(url=url, data=data, headers=header, verify=False)
#     return res.json()
#
# def request(url, method, data="", header=""):
#     if method=="get":
#         res=request_get(url=url,data=data,header=header)
#     if method=="post":
#         str_json=".*(application/json).*"
#         header_match=re.match(str_json,str(header))
#         # print(header_match)
#         if header_match:
#             # print(header_match.group(1))
#             res=request_post_json(url=url,data=data,header=header)
#         else:
#             res=request_post(url=url,data=data,header=header)
#     if method=="put":
#         str_json = ".*(application/json).*"
#         header_match = re.match(str_json, str(header))
#         if header_match:
#             data=json.dumps(data).encode(encoding='utf-8')
#         res=request_put(url=url,data=data,header=header)
#     if method=="delete":
#         str_json = ".*(application/json).*"
#         header_match = re.match(str_json, str(header))
#         if header_match:
#             data = json.dumps(data).encode(encoding='utf-8')
#         res=request_delete(url=url,data=data,header=header)
#     return res

def request(url, method, data="", header="",**kwargs):
    method=str(method).lower()
    print(header, data)
    if method == "get":
        res = requests.request(method="get", url=url, headers=header, params=data,**kwargs)
    else:
        str_json = ".*(application/json).*"
        header_match = re.match(str_json, str(header))
        # print(header_match)
        if header_match:
            data = json.dumps(data,cls=MyEncoder,indent=4).encode(encoding='utf-8')
        res = requests.request(method=method, url=url, headers=header, data=data,**kwargs)
        # print(res)
    return res.json()
