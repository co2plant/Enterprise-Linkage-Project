import os
import sys
import urllib.request,json

# Author : zsz153
# Naver papago translator API

client_id = "vJTrCnvRmexX3WFt1YqR"
client_secret = "nKpbRHRW0r"

def Trans(text,s,t): #텍스트,원어,번역언어
    encText = urllib.parse.quote(text)
    data = "source="+s+"&target="+t+"&text=" + encText
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