import os
import sys
import urllib.request
import json

class Translator_Papago:
    client_id='QTdhFVd5ysueemMh5hQa'
    client_secret='8MaeRBtbdt'

    def __init__(self):
        self.client_id = "QTdhFVd5ysueemMh5hQa"
        self.client_secret = "8MaeRBtbdt"

    def setClient_Id(self, client_id_input):
        self.client_id = client_id_input

    def setClient_Secret(self, client_secret_input):
        self.client_secret = client_secret_input

    def GetTranslate(self, inputtext, native_language, target_language):
        print("Call translate - GetTranslate")
        encText = urllib.parse.quote(inputtext)
        data = "source="+native_language+"&target="+target_language+"&text="+encText
        url = "https://openapi.naver.com/v1/papago/n2mt"
        try:
            request = urllib.request.Request(url)
            request.add_header("X-Naver-Client-Id",self.client_id)
            request.add_header("X-Naver-Client-Secret",self.client_secret)
        except :
            print("no license")
        response = urllib.request.urlopen(request, data=data.encode("utf-8"))
        rescode = response.getcode()
        if(rescode==200):
            response_body = response.read()
            decode = json.loads(response_body.decode('utf-8'))    
            result = decode['message']['result']['translatedText']    
            return result
        else:
            print("Error Code:" + rescode)
"""
    def readReferenceInfo(directory):
        try:
            if not os.path.exists(directory):
                    if not os.path.isfile("./CSV/"+file_name+".csv"):
                    self.saveDictionary("------","------",file_name)
                with open("./CSV/"+file_name+".csv", newline='',encoding='UTF8') as f:
                    reader = csv.reader(f)
                    data = list(reader)
                if(len(data) == 0):
                    return False
                for i in range(0, len(data)):
                    if(data[i][0] == input_text):
                        return data[i][1]
        except:


    def writeReferenceInfo(directory):
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
        except OSError:
            print('')"""