# from django.shortcuts import render
import requests, json, random
from cgi import parse_header
from django.http import JsonResponse

def processMessage(request):
    data = json.loads(request.body.decode('utf-8'))
    assert("message" in data)

    r = requests.get("http://www.cleverbot.com/getreply", params={
        "key": "CC7ahK5j61mGnivkAzEmsoI6aEA",
        "input": data["message"],
    })
    json_data = r.json()

    message = ""

    if "cookietruths" in data:
        options = [x["name"] for x in data.get("cookietruths")["accounts"] if x["logged_in"]]
        message = "\nI see that you are a fan of " + random.choice(options) + "."

    return JsonResponse({"response": json_data['output'] + message, "conversation_id": json_data['conversation_id']})

    # return render(request, "webapp/index.html")
