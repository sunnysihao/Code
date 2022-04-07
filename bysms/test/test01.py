# -*- coding = utf-8 -*-
import requests,pprint

payload = {
    'username': 'sunny',
    'password': '88888888'
}

response = requests.post('http://127.0.0.1:8000/api/mgr/signin',
                         data=payload)
#请求在消息体中用data  在url中用params
pprint.pprint(response.json())
