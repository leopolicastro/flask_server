from flask import Blueprint, jsonify, redirect, url_for, request
import requests
import json
import os

github = Blueprint('github', __name__)

GITHUB_API="https://api.github.com"
API_TOKEN=os.getenv('GIT_TOKEN')

#form a request URL
url=GITHUB_API+"/gists"
print("Request URL: %s"%url)

#print headers,parameters,payload
headers = {'Authorization': 'token %s' % API_TOKEN}
params = {'scope': 'gist'}


@github.route("/github/", methods = ['POST'])
def git():
  result = json.loads(request.data.decode('utf-8'))
  print(result)
  payload = {
    "description": "GIST created by python code",
    "public": True,
  }
  payload.update(result)
  # print(payload)
  res = requests.post(url,
                    headers=headers,
                    params=params,
                    data=json.dumps(payload))


  j = json.loads(res.text)
  # payload["files"] = file
  return j