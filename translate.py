import urllib.request
import json

class TranslatorPapago:
    client_id=''
    client_secret=''

    def __init__(self):
        self.client_id = ""
        self.client_secret = ""

    def set_client_id(self, client_id_input):
        self.client_id = client_id_input

    def set_client_secret(self, client_secret_input):
        self.client_secret = client_secret_input

    def get_translate(self, input_text, native_language, target_language):
        print("Call translate - GetTranslate")
        encText = urllib.parse.quote(input_text)
        data = "source="+native_language+"&target="+target_language+"&text="+encText
        url = "https://openapi.naver.com/v1/papago/n2mt"
        try:
            request = urllib.request.Request(url)
            request.add_header("X-Naver-Client-Id",self.client_id)
            request.add_header("X-Naver-Client-Secret",self.client_secret)
        except :
            print("no license")
        response = urllib.request.urlopen(request, data=data.encode("utf-8"))
        response_code = response.getcode()
        if(response_code==200):
            response_body = response.read()
            decode = json.loads(response_body.decode('utf-8'))    
            result = decode['message']['result']['translatedText']    
            return result
        else:
            print("Error Code:" + response_code)
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