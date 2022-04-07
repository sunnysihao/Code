# -*- coding = utf-8 -*-
import requests,pprint

payload = {
    "action":"list_medicine"
}
response = requests.get('http://127.0.0.1:8000/api/mgr/medicines',
                         params=payload)
#请求在消息体中用data  在url中用params
pprint.pprint(response.json())

