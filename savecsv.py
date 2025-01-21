#from datetime import datetime
import csv
import os

class SaveCsv:
    file_name=None
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    def __init__(self, selected_window_name):
        self.file_name = selected_window_name
    
    def save_dictionary(self, input_text, translated_text):
        #now = datetime.now()
        f = open("./CSV/"+self.file_name+".csv", 'a', encoding='utf-8', newline='')
        csvwriter = csv.writer(f)
        csvwriter.writerow([input_text, translated_text])
        f.close()
        
    def search(self,input_text):
        if not os.path.isfile("./CSV/"+self.file_name+".csv"):
            self.save_dictionary("------","------")
        with open("./CSV/"+self.file_name+".csv", newline='',encoding='UTF8') as f:
            reader = csv.reader(f)
            data = list(reader)
        if(len(data) == 0):
            return False
        for i in range(0, len(data)):
            if(data[i][0] == input_text):
                return data[i][1]

        return False
