from django.shortcuts import render
import requests

def processMessage(request):
    r = requests.get("http://www.cleverbot.com/getreply?key=CC7ahK5j61mGnivkAzEmsoI6aEA&input=YouSuck!&cs=76nxdxIJ02AAA")
    json_data = r.json()
    print("Reply: "+json_data['output'])

    return render(request, "webapp/index.html")
