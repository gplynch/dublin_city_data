import pandas as pd
import json
import sys
from collections import defaultdict

'''
Usage python gazetteer.csv data/dublin_city_records.csv
Read in city council headings
'''

council_notes = pd.read_csv(sys.argv[2],sep="\t",delimiter=None,encoding="utf8",header=0)
council_obj = council_notes.to_dict('records')
'''
Read in gazetteer
'''

gaz = pd.read_csv(sys.argv[1],sep=",",delimiter=None,encoding="utf8",header=0)
gaz_obj = gaz.to_dict('records')

places = ["close","street","road","villas","mansions","lane", "upper",\
 "middle", "lower", "the", "gardens","crescent","walk","drive","park","square",\
"avenue", "green","terrace","parade","place","quay","court","drive","grove","cottages",\
"mews","way","buildings","estate","wood","rise","lawn",\
"village","heath","row","downs","alley","view","lawn",\
"gort","island","hill","villa","hall","market","glen","bridge","wall","dock","wharf"]

non_located = 0
found = False
locations_map = defaultdict(int)
overlooked = []
for line in council_obj:
    #print(line)
    found = False
    subject = line['Subject']
    low_sub = subject.lower()
    low_sub = low_sub.replace("-"," ")
    locations = []
    for g in gaz_obj:
        english = g['english']
        eng = str(english).lower()
        if low_sub.find(eng) > -1:
            found = True
            locations.append(eng)
            locations_map[eng] +=1
    #print(low_sub + "( )" + str(list(set(locations))))
    if not found:
        for x in places:
            found = low_sub.find(x)
            if found > -1:
                overlooked.append(low_sub[0:found + len(x)])
        non_located = non_located + 1
print(str(non_located) + " records out of " + str(len(council_obj)) + " do not contain location information")
with open("locations_map.json","w") as o:
    o.write(json.dumps(list(locations_map.items())))
with open("overlooked.json","w") as b:
    b.write(json.dumps(overlooked))
