# KinglyAssessment

The url http://localhost:5000/KinglyAssessment_CSV will respond in a csv file KinglyAssessment.csv after running the python code KinglyAssessment.py.
    
Prerequisites :

Python 2.7 (preferred) or above  and Flask (1.0.2 preferred) should be installed in the machine.

Requirement :

Output CSV file  to be developed after performing the following rules in the returned json object from URL http://mysafeinfo.com/api/data?list=englishmonarchs&format=json.

Rules :

● Kings should be divided up by century the year they were coronated.
● Any king from the House of Wessex should not be included.
● Kings should include their first names and they should be backwards e.g “Edward I” should be
“drawdE”
● Kings should be ordered alphabetically.
● Country should be stored as an acronym e.g ‘United States’ should be (US)
● Only include the year the king was coronated
● Write the manipulated data to a csv file using the given headers:
    Name
    Country
    House
    Year of Coronatiom
    Ingestion Time - A timestamp of when the data was wrote to the file

Approach :

● Json object from url is extracted using urllib2 module of python
● The above transformation rules are applied to the elements in the json data
● The new transformed data is then stored as a csv file
● Flask is used as the web application interface to provide the csv file as a response
