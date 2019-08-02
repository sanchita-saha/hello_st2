import requests
from st2common.runners.base_action import Action
class MyEchoAction(Action):
	def run(self, message):
		resp = requests.get('https://jsonplaceholder.typicode.com/todos/1')
		if resp.status_code == 200:
		for todo_item in resp.json():
			print('{} {}'.format(todo_item['id'], todo_item['userId']))