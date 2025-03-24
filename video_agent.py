import requests
import json
from clip_extraction import clip
import time

url = "https://api.d-id.com/clips"

payload = json.dumps({
  "script": {
    "type": "text",
    "input": "Hypothesis method compares two opposite statements about a population and uses sample data to decide which one is more likely to be correct.To test this assumption we first take a sample from the population and analyze it and use the results of the analysis to decide if the claim is valid or not."
  },
  "presenter_id": "amy-Aq6OmGZnMt",
  "driver_id": "Vcq0R4a8F0"
})
headers = {
  'accept': 'application/json',
  'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik53ek53TmV1R3ptcFZTQjNVZ0J4ZyJ9.eyJodHRwczovL2QtaWQuY29tL2ZlYXR1cmVzIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9zdHJpcGVfcHJvZHVjdF9pZCI6IiIsImh0dHBzOi8vZC1pZC5jb20vc3RyaXBlX2N1c3RvbWVyX2lkIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9zdHJpcGVfcHJvZHVjdF9uYW1lIjoidHJpYWwiLCJodHRwczovL2QtaWQuY29tL3N0cmlwZV9zdWJzY3JpcHRpb25faWQiOiIiLCJodHRwczovL2QtaWQuY29tL3N0cmlwZV9iaWxsaW5nX2ludGVydmFsIjoibW9udGgiLCJodHRwczovL2QtaWQuY29tL3N0cmlwZV9wbGFuX2dyb3VwIjoiZGVpZC10cmlhbCIsImh0dHBzOi8vZC1pZC5jb20vc3RyaXBlX3ByaWNlX2lkIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9zdHJpcGVfcHJpY2VfY3JlZGl0cyI6IiIsImh0dHBzOi8vZC1pZC5jb20vY2hhdF9zdHJpcGVfc3Vic2NyaXB0aW9uX2lkIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9jaGF0X3N0cmlwZV9wcmljZV9jcmVkaXRzIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9jaGF0X3N0cmlwZV9wcmljZV9pZCI6IiIsImh0dHBzOi8vZC1pZC5jb20vcHJvdmlkZXIiOiJnb29nbGUtb2F1dGgyIiwiaHR0cHM6Ly9kLWlkLmNvbS9pc19uZXciOmZhbHNlLCJodHRwczovL2QtaWQuY29tL2FwaV9rZXlfbW9kaWZpZWRfYXQiOiIiLCJodHRwczovL2QtaWQuY29tL29yZ19pZCI6IiIsImh0dHBzOi8vZC1pZC5jb20vYXBwc192aXNpdGVkIjpbIlN0dWRpbyJdLCJodHRwczovL2QtaWQuY29tL2N4X2xvZ2ljX2lkIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9jcmVhdGlvbl90aW1lc3RhbXAiOiIyMDI1LTAzLTIzVDEwOjEzOjU0LjEzOFoiLCJodHRwczovL2QtaWQuY29tL2FwaV9nYXRld2F5X2tleV9pZCI6IiIsImh0dHBzOi8vZC1pZC5jb20vaGFzaF9rZXkiOiJDZFQydTlTdk1RVmVrUlB5dkhUWTkiLCJodHRwczovL2QtaWQuY29tL3ByaW1hcnkiOnRydWUsImh0dHBzOi8vZC1pZC5jb20vZW1haWwiOiJsaWtpdGhrdW1hcmQwNEBnbWFpbC5jb20iLCJodHRwczovL2QtaWQuY29tL2NvdW50cnlfY29kZSI6IlVTIiwiaHR0cHM6Ly9kLWlkLmNvbS9wYXltZW50X3Byb3ZpZGVyIjoic3RyaXBlIiwiaXNzIjoiaHR0cHM6Ly9hdXRoLmQtaWQuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTEyMTMzNDM2MjQwNzE0OTY3MDUyIiwiYXVkIjpbImh0dHBzOi8vZC1pZC51cy5hdXRoMC5jb20vYXBpL3YyLyIsImh0dHBzOi8vZC1pZC51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNzQyNzI0ODY5LCJleHAiOjE3NDI4MTEyNjksInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwgcmVhZDpjdXJyZW50X3VzZXIgdXBkYXRlOmN1cnJlbnRfdXNlcl9tZXRhZGF0YSBvZmZsaW5lX2FjY2VzcyIsImF6cCI6Ikd6ck5JMU9yZTlGTTNFZURSZjNtM3ozVFN3MEpsUllxIn0.IxAZUkRSqvTvC99ZgaHvrRl5WILY_laRJJtl60U-KR7db4ku-jsyqs-DIWecyQZXC6eJ_ht7k0DwmG4LMlx7ANugiXaSqTwn-ZbWy9UF9jxBPxW-pEYCjEpKFeR7o_alHc4wDdUvTvOVpZNKULyzpF9AJx3stc_wHIwvFnqLL__wONfCN5k3uCX3JiyGUbEnGbO7tYv8_w2CGEz9A4w2naCuLXyScedmHzXLQn5XI_S7wQASYE2ctgKkGoow_c8mP7s3W5oT1BZS_CoEx62LsWG6obnJ_daFdreSjeNWsYTGTOXz9lcva7XOkyMzfzLJi3KD_8cUcXC4pWWr0CHnkQ',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
time.sleep(10)
clip_id = response.json()["id"]
video = clip(clip_id)

