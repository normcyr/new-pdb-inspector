#!/usr/bin/python3
'''
Search for new PDB structures corresponding to a search term and deposited after a certain date.
Default search term: autophagy
Default max deposition date: 30 days ago
'''

from pypdb import make_query, do_search, describe_pdb, get_pdb_file, get_all_info
from dateutil import parser
from datetime import datetime, timedelta

def searchPDB(searchTerm):

    # use these entries for test purposes
    pdbtest = '3vtv' #BUG: this structure uses entityNr instead of nr_entities
    #pdbtest = '4xkl'
    #pdbtest = '5v4k'
    searchStructures = make_query(pdbtest, querytype='AdvancedKeywordQuery')

    #searchStructures = make_query(searchTerm, querytype='AdvancedKeywordQuery')
    foundStructures = do_search(searchStructures)
    print(foundStructures)
    return(foundStructures)

def extractData(maxDepositionDate, foundStructures):
    results = {}

    for entry in foundStructures:
        entityInfo = describe_pdb(entry)
        depositionDate = datetime.date(parser.parse(entityInfo['deposition_date']))

        if depositionDate >= maxDepositionDate:
            entityStructureID = entityInfo['structureId']
            entityTitle = entityInfo['title']
            entityExtraInfo = get_all_info(entry)

            #this needs to be fixed so I can get all molecule names if nr_entities > 1
            if int(describe_pdb(entry)['nr_entities']) > 1:
                for mol in entityExtraInfo['polymer']:
                    moleculeName = mol.get('macroMolecule').get('@name')

            elif int(describe_pdb(entry)['nr_entities']) == 1:
                moleculeName = entityExtraInfo.get('polymer').get('macroMolecule').get('@name')

            else:
                moleculeName = 'No molecule name give'

            results[entry] = (moleculeName, entityTitle, str(depositionDate))

    return(results)

def printOutput(foundStructures, searchTerm, results, maxDepositionDate):
    message = 'I found {} structures from the PDB corresponding to the search term \'{}\'. Of the {} structures, {} were deposited after {}.'.format(len(foundStructures), searchTerm, len(foundStructures), len(results), maxDepositionDate)

    return(message)

def main():
    searchTerm = 'autophagy'
    daysToSubtract = 20000
    maxDepositionDate = datetime.date(datetime.today() - timedelta(days = daysToSubtract))

    foundStructures = searchPDB(searchTerm)
    results = extractData(maxDepositionDate, foundStructures)
    #message = printOutput(foundStructures, searchTerm, results, maxDepositionDate)
    #print(message)

    return(results)

if __name__ == '__main__':
    main()
