import os
import sys
import urllib.request
import json

client_id = "vJTrCnvRmexX3WFt1YqR"
client_secret = "nKpbRHRW0r"

def GetTranslate(inputtext, native_language, target_language):
    encText = urllib.parse.quote(inputtext)
    data = "source="+native_language+"&target="+target_language+"&text="+encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        decode = json.loads(response_body.decode('utf-8'))    
        result = decode['message']['result']['translatedText']    
        return result
    else:
        print("Error Code:" + rescode)