# KinglyAssessment

The url http://localhost:5000/KinglyAssessment_CSV will respond in a csv file KinglyAssessment.csv after running the python code KinglyAssessment.py.
    
Prerequisites :

Python 2.7 (preferred) or above  and Flask (1.0.2 preferred) should be installed in the machine.

Approach :

● Json object from url http://mysafeinfo.com/api/data?list=englishmonarchs&format=json is extracted using urllib2 module of python
● The above transformation rules are applied to the elements in the json data
● The new transformed data is then stored as a csv file
● Flask is used as the web application interface to provide the csv file as a response
