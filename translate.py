import os
import sys
import urllib.request
import json
from sandbox_renderer import App

client_id = ""
client_secret = ""

def setClient_Id(client_id_input):
    client_id = client_id_input

def setClient_Secret(client_secret_input):
    client_secret = client_secret_input

def GetTranslate(inputtext, native_language, target_language):
    encText = urllib.parse.quote(inputtext)
    data = "source="+native_language+"&target="+target_language+"&text="+encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    try:
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id",client_id)
        request.add_header("X-Naver-Client-Secret",client_secret)
    except :
        App.makeAlert("NULL", "NULL")
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        decode = json.loads(response_body.decode('utf-8'))    
        result = decode['message']['result']['translatedText']    
        return result
    else:
        print("Error Code:" + rescode)