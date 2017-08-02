# New PDB Depositons Inspector

Searches the PDB for new depositions.

## Usage

## Requirements

Python 3

and the following packages (all found in `requirement.txt`):

* beautifulsoup4==4.6.0
* cycler==0.10.0
* matplotlib==2.0.2
* numpy==1.13.1
* pyparsing==2.2.0
* pypdb==1.103
* python-dateutil==2.6.1
* pytz==2017.2
* six==1.10.0
* xmltodict==0.11.0


## Notes to self

### Step 1 - Get the data

- fetch the new structures information
- download the pdb file
- parse the data to json format

### Step 2 - Output the data

- get the data in json format
- print as table in webpage

### Step 3 - Notify user

- weekly, send an email to user to notify of new depositions
