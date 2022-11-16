#from datetime import datetime
import csv
import os

class SaveCsv:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    def saveDictionary(self, input_text, translated_text,file_name):
        #now = datetime.now()
        f = open("./CSV/"+file_name+".csv", 'a', encoding='utf-8', newline='')
        csvwriter = csv.writer(f)
        csvwriter.writerow([input_text, translated_text])
        f.close()
        
    def serach(self,input_text,file_name):
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

        return False
