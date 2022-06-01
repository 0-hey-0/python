import json
import re

import requests

def request(method,url,data,header,**kwargs):
    method=str(method).lower()
    if method=='get':
        res=requests.request(method=method,url=url,parmas=data,headers=header,**kwargs)
    else:
        str_header=".*application/json.*"
        match_header=re.match(str_header,str(header))
        if match_header:
            data=json.dumps(data).encode(encoding='utf-8')
        res=requests.request(method=method,url=url,data=data,headers=header,**kwargs)
    return res.json()

