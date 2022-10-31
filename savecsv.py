from datetime import datetime
import csv
import os

class SaveCsv:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    def __init__(self):
        x=0
    
    def saveDictionary(self, number, input_text, translated_text):
        now = datetime.now()
        f = open('dictionary.csv', 'a', encoding='utf-8', newline='')
        csvwriter = csv.writer(f)
        csvwriter.writerow([now, number, input_text, translated_text])
        f.close()
        
sd = SaveCsv()
sd.saveDictionary(1, 'normal', 'notnormal')