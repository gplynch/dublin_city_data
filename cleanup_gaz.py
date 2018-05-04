import pandas as pd
import json
import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()

splitters = ["close","street","road","villas","mansions","lane", "upper",\
 "middle", "lower", "the", "gardens","crescent","walk","drive","park","square",\
"avenue", "green","terrace","parade","place","quay","court","drive","grove","cottages",\
"mews","way","buildings","estate","wood","rise","lawn",\
"village","heath","row","downs","alley","view","lawn",\
"gort","island","hill","villa","hall","market","glen","bridge","wall","dock","wharf"]

both_names = []

for line in lines:
    line =line.rstrip()
    words = line.split(" ")
    found = False
    if len(words) > 1:
        line = line.lower()
        indexes= []
        for s in splitters:
            #print(s)
            spaced = " " + s + " "
            if spaced in line:
                #print("(" + line + ")")
                found = True
                #print(line.rfind(s))
                indexes.append(line.rfind(s) + len(s))
        sorted_indexes = sorted(indexes, key = lambda x: x, reverse = True)
        if found:
            last_index = sorted_indexes[0]
            #print(last_index)
            english = line[0:last_index]
            irish = line[last_index:len(line)]
            both_names.append({"english" : english, "irish" : irish})
        else:
            print(line)

df = pd.DataFrame(both_names)
df.to_csv("data_structured.csv")
