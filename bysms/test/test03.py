# -*- coding = utf-8 -*-
import requests,pprint

payload = {
    "action":"add_customer",
    "data":{
        "name":"gaofangfang",
        "phonenumber":"13345679934",
        "address":"zhongguo"
    }
}

response = requests.post('http://127.0.0.1:8000/api/mgr/customers',
                         params=payload)
#请求在消息体中用data  在url中用params
pprint.pprint(response.json())

