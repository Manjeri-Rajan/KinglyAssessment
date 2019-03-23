#!/usr/bin/python

from flask import Flask, Response
app = Flask(__name__)

import urllib2
import json
import datetime
import time

response = urllib2.urlopen('http://mysafeinfo.com/api/data?list=englishmonarchs&format=json') #Loading source data
jsonFile = response.read()
input_data = json.loads(jsonFile)

new_data = [d for d in input_data if d["hse"] != "House of Wessex"] #Remove House of Wessex

for ele in new_data:
   ele["nm"] = ele["nm"].split(" ")[0][::-1]  #Reversing the name
   ele["cty"] = ele["cty"].split(" ")[0][0] + ele["cty"].split(" ")[1][0] #Country as acronym
   ele["yrs"] = ele["yrs"].split("-")[0]  #Splitting years to get year of coronation
   ele["century"] = int(ele["yrs"])//100 + 1 #Finding the century of coronation
   
   
newlist = sorted(new_data, key = lambda k : (k["century"],k["nm"])) #Sorting alphabetically within century

csv =  open("output_assessment.csv","w") #Creating a csv file for writing

i = 0

for ele in newlist:
   
   if (ele["century"] != i):
       csv.write("\n" + str(ele["century"]) + "th century\n\n" + "Name,Country,House,Year_Of_Coronation,Ingestion_Time\n")
   
   ts = time.time() 
   ele["ingestion"] = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S') #Finding time of ingestion
   
   csv.write(ele["nm"] + "," + ele["cty"] + "," + ele["hse"] + "," + ele["yrs"] + "," + ele["ingestion"] + "\n")
   
   i = ele["century"]
   
csv.close()

@app.route("/")
def hello():
    return '''
        <html><body>
        Hello. <a href="/KinglyAssessment_CSV">Click me.</a>
        </body></html>
        '''

@app.route("/KinglyAssessment_CSV")
def getPlotCSV():	
    with open("output_assessment.csv") as file:
        csv = file.read()
    return Response(
        csv,
        mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename=KinglyAssessment.csv"}) #Response as CSV file


app.run()
