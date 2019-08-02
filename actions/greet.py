import sys

from st2common.runners.base_action import Action

class MyEchoAction(Action):
    def run(self, message):
        print(message)

		
		
import requests
from st2common.runners.base_action import Action
class MyEchoAction(Action):
	def run(self, message):
		resp = requests.get('https://jsonplaceholder.typicode.com/todos/1)
		if resp.status_code != 200:
			# This means something went wrong.
			raise ApiError('GET /tasks/ {}'.format(resp.status_code))
		for todo_item in resp.json():
			print('{} {}'.format(todo_item['id'], todo_item['userId']))