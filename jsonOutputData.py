#!/usr/bin/python3
'''
Parse the results to json format
'''

import json
import fetchNewPdb

results = fetchNewPdb.main()
jsonResults = json.dumps(results)
print(jsonResults)
