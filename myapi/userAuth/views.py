from django.http.response import HttpResponse
from django.shortcuts import render, resolve_url
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from userAuth.models import User, FraudCheck
import json
import sys
import datetime

# Create your views here.
def index(request):
    response = json.dumps({'Hello':'world'})
    return HttpResponse( response, content_type='application/json')

def get_Users(request):
    if request.method == 'GET':
        try:
            users = User.objects.all()
            response = serializers.serialize("json", users)
        except:
            response = json.dumps({'Error': str(sys.exc_info()[0])})
    else:
        response = json.dumps({'Error': 'bad reqeust type'})
    return HttpResponse(response, content_type='application/json')

@csrf_exempt
def add_User(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        username = payload["username"]
        password = payload["password"]
        fingerprint = payload["fingerprint"]
        newUser = User(username=username, password=password, fingerprint=fingerprint)
        try:
            newUser.save()
            response = json.dumps({'Sucess':'User Added'})
        except:
            response = json.dumps({'Error': str(sys.exc_info()[0])})
    else:
        response = json.dumps({'Error': 'bad request type'})
    return HttpResponse(response, content_type='application/json')

@csrf_exempt
def handleFraudCheck(request):
    if request.method == "POST":
        payload = json.loads(request.body)
        ipAndFp = FraudCheck.objects.filter(**payload)
        onlyFp = FraudCheck.objects.filter(fingerprint=payload["fingerprint"])
        onlyIp = FraudCheck.objects.filter(ipaddr=payload["ipaddr"])
        if ipAndFp:
            response = makeResponse("Already Credited", ipAndFp)
        elif onlyFp:
            response = makeResponse("Probably already credited to FP", onlyFp)
        elif onlyIp:
            response = makeResponse("Probably already credited to IP", onlyIp)
        else:
            newFraudCheck = FraudCheck(time=datetime.datetime.now().strftime("%d/%m/%y %H:%M"),  **payload)
            try:
                newFraudCheck.save()
                response = json.dumps({'Sucess':'Check'})
            except:
                response = json.dumps({'Error': str(sys.exc_info()[0])})
    else:
        response = json.dumps({'Error': 'bad request type'})
    return HttpResponse(response, content_type='application/json')

def makeResponse(info, q):
    return json.dumps({"creditStatus": info, "user": [[x.fingerprint, x.ipaddr, x.time] for x in q]})
