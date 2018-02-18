# from django.shortcuts import render
import requests
from django.http import JsonResponse

def processMessage(request):
    assert("message" in request.POST)

    r = requests.get("http://www.cleverbot.com/getreply", params={
        "key": "CC7ahK5j61mGnivkAzEmsoI6aEA",
        "input": request.POST["message"],
    })
    json_data = r.json()

    return JsonResponse({"response": json_data['output']})

    # return render(request, "webapp/index.html")
