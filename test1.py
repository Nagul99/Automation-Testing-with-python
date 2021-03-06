import sys,socket
import requests

import unittest

url="https://qa-api.imahila.in:443/api/v1/users/register"


access_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7Il9pZCI6IjVjZTY5MDJlZjJhNGYyMWZmYjM1M2JiMiIsInBob25lIjo5NzkxMzMxMjgwLCJsYW5ndWFnZSI6IjVjMzlhMTVmYjRmZWQxM2ZlNzNiM2E4NCIsInByZWZlcmVuY2VzIjpbIjVjMzljMDYxOTI1NDc4NDkzZTI5Y2Q4NyIsIjVjNTgyZmI1NzZmZWY2M2ZlYmFlZGEyYSIsIjVjNWQ3NzQyMGM0NjQzMDE0OWMxOGIxNSIsIjVjNzM4YmQ3ZjczZWE5NTI5NzA2MzhkNCIsIjVjNWQzMWJiMGM0NjQzMDE0OWMxOGIwMiIsIjVjNzhkOGM5YjczZmJlMTNhNmMwMDI3ZCIsIjVjNzkyZTY2YjczZmJlMTNhNmMwMDI5NyIsIjVjY2VjNmMwZjk5ZTA0NDA3YmU3NGRlOCJdLCJyb2xlcyI6WyJ1c2VyIl19LCJkZXZpY2UiOiI1Y2U2OGY2M2YyYTRmMjFmZmIzNTNiYjEiLCJpYXQiOjE1NTkxMDYyMzcsImV4cCI6MTU1OTE5MjYzNywiYXVkIjoiYW5kcm9pZC1nYXRld2F5IiwiaXNzIjoidXNlci1zZXJ2aWNlLmp3dC1tYW5hZ2VyLmF1dGgiLCJzdWIiOiJnZW5lcmFsLXJlc291cmNlLWF1dGhvcml6YXRpb24ifQ.LdugNqEwtAj7MKcGVVVgCyhGhO8dIYbl9GMU9oe3W5k'

response=requests.post(url, json = { "language" : "5c39a78eb4fed13fe73b3a85",
    "phone" : "9791331290",
    "preferences" : []},
           headers={'Authorization': 'Bearer {}'.format(access_token),
                'Content-Type':'application/json',
                'X-Device-Identifier':'5ce68f63f2a4f21ffb353bb1'})

print(response)
assert response.status_code==200

url1="https://qa-api.imahila.in:443/api/v1/app-versions/1"



response1=requests.post(url1, 
           headers={'Authorization': 'Bearer {}'.format(access_token),
                'Content-Type':'application/json',
                'X-Device-Identifier':'5ce68f63f2a4f21ffb353bb1'})

print(response1)


url2="https://qa-api.imahila.in:443/api/v1/preferences"

response2 = requests.get(url2,
      params={'limit' : 3, 'offset' : 0, 'languageId' : '5c39a78eb4fed13fe73b3a85', 'fields': 'name,description,coverImage'},
      headers={'Authorization': 'Bearer {}'.format(access_token),
                'Content-Type':'application/json',
                'X-Device-Identifier':'5ce68f63f2a4f21ffb353bb1'})

print(response2)

class TestStringMethods(unittest.TestCase):

    def test_register_new_user(self):
        self.assertEqual(response.status_code, 200)

    def test_add_versions(self):
        self.assertEqual(response1.status_code, 200)

    def test_preferences(self):
        self.assertEqual(response2.status_code, 200)


if __name__ == '__main__':
    unittest.main()
