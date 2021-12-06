from django.http.response import HttpResponse
from django.shortcuts import render, resolve_url
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json
from userAuth.models import User


# Create your views here.
def index(request):
    response = json.dumps({'Hello':'world'})
    return HttpResponse( response, content_type='application/json')

def get_Users(request):
    if request.method == 'GET':
        try:
            users = User.objects.all()
            response = serializers.serialize("json", users)
        except Exception as e:
            response = json.dumps({'Error': e})
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
        except Exception as e:
            response = json.dumps({'Error': e})
    else:
        response = json.dumps({'Error': 'bad request type'})
    return HttpResponse(response, content_type='application/json')