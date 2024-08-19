from flask import Flask, request
import docker
import sys
import json
import os

app = Flask(__name__)
client = docker.from_env()


@app.route('/')
async def hello():
    return "Service Up!"


@app.route('/webhook', methods=['POST'])
async def receive_payload():
    payload = request.json
    
    ##Some security for the webhook##
    api = {
        "name": "studenthub-api",
        "image": "ghcr.io/studenthubproject/studenthub-api",
        "ports": {"8080" : "8080"},
        "detach": True,
        "restart_policy": {"Name": "always"}
    }

    web = {
        "name": "studenthub-web",
        "image": "ghcr.io/studenthubproject/studenthub-web",
        "ports": {"3000" : "3000"},
        "detach": True,
        "restart_policy": {"Name": "always"}
    }

    if payload["repository"] == api["name"]:
        payload = api
    elif payload["repository"] == web["name"]:
        payload = web
    else:
        return "Unauthorized"
    #################################

    registry='ghcr.io'
    pat = os.environ.get("pat")
    username = os.environ.get("username")
    
    print("Request recieved for: " + str(payload["name"]),file=sys.stderr)    
    client.login(username=username, password=pat, registry=registry)

    try:
        existing_container = client.containers.get(payload["name"])
        existing_container.stop()
        existing_container.remove(force=True)
    except:
        print("No existing container",file=sys.stderr)
    
    payload["image"] = client.images.pull(repository = payload["image"], tag = 'main')

    container_run_parameters = payload
    
    client.containers.run(**container_run_parameters)
    client.images.prune()
    
    return "Success"




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)