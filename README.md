# Introduction

This repo contains code and data from a historical index (1888-1988) of Dublin City Council meeting notes.

Goals of this project are:

* Clean up the data into a more structured format
* Use NLP and geocoding to attach geographical locations to each element
* Enrich the text with linked data tags from DBPedia where possible
* Allow semantic querying over the data.


Inspired by a hackathon on Dublin City Council Data from Dublin Inquirer (counciltracker.ie)


# Process

* Generated a gazetteer for Dublin streets and areas (`data/dublin_gazetteer.csv`)
* This combined a streetname list from logainm.ie with placenames gazetteer from geonames.
* Wrote some code to loop through the Dublin City Council minutes (`minutes/dublin_city_council.tsv`)
* Output a json file containing placename frequencies in the corpus.
* TODO : Geocode these using Google Maps API
* TODO : Further enrich this data using dbpedia_spotlight allowing semantic search and explanations (https://github.com/dbpedia-spotlight/dbpedia-spotlight)
* TODO : Create frontend using OpenStreetMap and allow users to view the history of a location through Dublin City Council data.
* TODO : Visualise the change in focus of the council over 100 years (building of new suburbs in 1960s and 1970s, etc)

# Challenges

* Renamed or removed streets or locations (Sackville St to O'Connell Street, Kingsbridge to Heuston Station)
* Compile list of non-street-landmarks in Dublin (parks, rivers, etc)
* Evaluate coverage of gazetteer for areas (Dolphins's Barn, Pimlico, etc)
