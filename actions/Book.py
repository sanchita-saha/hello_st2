import requests
from st2common.runners.base_action import Action
class MyEchoAction(Action):
	task = {"summary": "Take out trash", "description": "" }
resp = requests.post('http://fakerestapi.azurewebsites.net/api/Books, json=task)
if resp.status_code != 201:
    raise ApiError('POST /tasks/ {}'.format(resp.status_code))
print('Created task. ID: {}'.format(resp.json()["id"]))