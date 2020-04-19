import os
import requests

from covid19 import helpers


# api.covid19india.org
DATA_API = "https://api.covid19india.org/data.json"
DISTRICT_WISE_API = "https://api.covid19india.org/state_district_wise.json"

# NovelCovid/API for all world
WORLD_API = "https://corona.lmao.ninja/v2/all"
COUNTRIES_API = "https://corona.lmao.ninja/v2/countries"

STATE_CODES = []
COUNTRY_CODES = []

DATA = helpers.send_request(DATA_API)
if DATA:
    for details in DATA['statewise']:
        STATE = [
            details['state'],
            details['statecode']
        ]
        STATE_CODES.append(STATE)

# print(STATE_CODES)

COUNTRIES_DATA = helpers.send_request(COUNTRIES_API)
if COUNTRIES_DATA:
    for COUNTRY_DATA in COUNTRIES_DATA:
        COUNTRY = []
        COUNTRY.append(COUNTRY_DATA['country'])

        if 'countryInfo' in COUNTRY_DATA:
            if 'iso2' in COUNTRY_DATA['countryInfo'] and \
               COUNTRY_DATA['countryInfo']['iso2'] is not None:
                COUNTRY.append(COUNTRY_DATA['countryInfo']['iso2'])

            if 'iso3' in COUNTRY_DATA['countryInfo'] and \
               COUNTRY_DATA['countryInfo']['iso3'] is not None:
                COUNTRY.append(COUNTRY_DATA['countryInfo']['iso3'])
        COUNTRY_CODES.append(COUNTRY)

# print(COUNTRY_CODES)


f = open("CODES.md", "w+")

f.write("## Codes for refrence\n")

f.write("\n\n")

f.write("### STATES Codes\n")
f.write("<p>Usage `covid19 India -s $state_name` or `covid19 India -s $state_code`</p>\n\n")
f.write("|\tSr. No.\t|\tState Name\t|\tState Code\t|\n")
f.write("|-----------|:-----------:|:------------:|\n")
count = 1
for state_code in STATE_CODES[1:]:
    f.write("|\t"+str(count)+"\t|\t"+state_code[0]+"\t|\t"+state_code[1]+"\t|\n")
    count += 1

f.write("\n\n")

f.write("### Country Codes\n")
f.write("<p>Usage `covid19 $country_name` or `covid19 $iso`</p>\n\n")
f.write("|\tSr. No.\t|\tCountry Name\t|\tISO\t|\n")
f.write("|-----------|:-----------:|:------------:|\n")
count = 1
for country_code in COUNTRY_CODES:
    try:
        f.write("|\t"+str(count)+"\t|\t"+country_code[0]+"\t|\t"+country_code[1]+"\t|\n")
    except Exception:
        f.write("|\t"+str(count)+"\t|\t"+country_code[0]+"\t|\t\t|\n")
    count += 1

f.close()
