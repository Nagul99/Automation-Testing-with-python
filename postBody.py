import sys,socket
import requests

url="https://qa-api.imahila.in:443/api/v1/app-versions/1"


access_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7Il9pZCI6IjVjZTY5MDJlZjJhNGYyMWZmYjM1M2JiMiIsInBob25lIjo5NzkxMzMxMjgwLCJsYW5ndWFnZSI6IjVjMzlhMTVmYjRmZWQxM2ZlNzNiM2E4NCIsInByZWZlcmVuY2VzIjpbIjVjMzljMDYxOTI1NDc4NDkzZTI5Y2Q4NyIsIjVjNTgyZmI1NzZmZWY2M2ZlYmFlZGEyYSIsIjVjNWQ3NzQyMGM0NjQzMDE0OWMxOGIxNSIsIjVjNzM4YmQ3ZjczZWE5NTI5NzA2MzhkNCIsIjVjNWQzMWJiMGM0NjQzMDE0OWMxOGIwMiIsIjVjNzhkOGM5YjczZmJlMTNhNmMwMDI3ZCIsIjVjNzkyZTY2YjczZmJlMTNhNmMwMDI5NyIsIjVjY2VjNmMwZjk5ZTA0NDA3YmU3NGRlOCJdLCJyb2xlcyI6WyJ1c2VyIl19LCJkZXZpY2UiOiI1Y2U2OGY2M2YyYTRmMjFmZmIzNTNiYjEiLCJpYXQiOjE1NTkxMDYyMzcsImV4cCI6MTU1OTE5MjYzNywiYXVkIjoiYW5kcm9pZC1nYXRld2F5IiwiaXNzIjoidXNlci1zZXJ2aWNlLmp3dC1tYW5hZ2VyLmF1dGgiLCJzdWIiOiJnZW5lcmFsLXJlc291cmNlLWF1dGhvcml6YXRpb24ifQ.LdugNqEwtAj7MKcGVVVgCyhGhO8dIYbl9GMU9oe3W5k'

response=requests.post(url, 
           headers={'Authorization': 'Bearer {}'.format(access_token),
                'Content-Type':'application/json',
                'X-Device-Identifier':'5ce68f63f2a4f21ffb353bb1'})

print(response)
#assert response.status_code==200
