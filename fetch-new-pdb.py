#!/usr/bin/python3
'''
Search for new PDB structures corresponding to a search term and deposited after a certain date.
Default search term: autophagy
Default max release date: 7 days ago
'''

from pypdb import make_query, do_search, get_entity_info
from dateutil import parser
from datetime import datetime, timedelta

def searchPDB(searchTerm):
    searchStructures = make_query(searchTerm, querytype='AdvancedKeywordQuery')
    foundStructures = do_search(searchStructures)

    return(foundStructures)

def parseData(maxReleaseDate, foundStructures):
    results = {}
    for entry in foundStructures:
        entityInfo = get_entity_info(entry)
        releaseDate = datetime.date(parser.parse(entityInfo['release_date']))
        if releaseDate >= maxReleaseDate:
            results[entry] = str(releaseDate)

    return(results)

def printOutput(foundStructures, searchTerm, results, maxReleaseDate):
    message = 'I found {} structures from the PDB corresponding to the search term \'{}\'. Of the {} structures, {} were deposited after {}.'.format(len(foundStructures), searchTerm, len(foundStructures), len(results), maxReleaseDate)

    return(message)

def main():
    searchTerm = 'autophagy'
    daysToSubtract = 7
    maxReleaseDate = datetime.date(datetime.today() - timedelta(days = daysToSubtract))

    foundStructures = searchPDB(searchTerm)
    results = parseData(maxReleaseDate, foundStructures)
    message = printOutput(foundStructures, searchTerm, results, maxReleaseDate)

    print(message)

if __name__ == '__main__':
    main()
