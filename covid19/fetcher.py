import pprint
import time
from datetime import datetime

from covid19.helpers import send_request

# api.covid19india.org
DATA_API = "https://api.covid19india.org/data.json"
DISTRICT_WISE_API = "https://api.covid19india.org/state_district_wise.json"

# NovelCovid/API for all world
WORLD_API = "https://corona.lmao.ninja/v2/all"
COUNTRIES_API = "https://corona.lmao.ninja/v2/countries"


def fetch_india_status(state=False):
    try:
        DATA = send_request(DATA_API)

        if not state:
            # for India stateName is Total
            state = "Total"
        elif state.lower() == "all":
            # if data for every state requested
            return DATA['statewise'][1:]

        for details in DATA['statewise']:
            if details['state'].lower() == state.lower() or \
               details['statecode'].upper() == state.upper():
                return details

    except Exception as e:
        return None


def fetch_world_details():
    try:
        DATA = send_request(WORLD_API)
        # match data according global parser object
        WORLD_DETAILS = {}
        WORLD_DETAILS['state'] = "World"
        WORLD_DETAILS['lastupdatedtime'] = time.strftime(
            '%d/%H/%Y %H:%M',
            time.gmtime(DATA['updated']/1000)
        )
        WORLD_DETAILS['confirmed'] = DATA['cases']
        WORLD_DETAILS['active'] = DATA['active']
        WORLD_DETAILS['recovered'] = DATA['recovered']
        WORLD_DETAILS['deaths'] = DATA['deaths']

        WORLD_DETAILS['deltaconfirmed'] = DATA['todayCases']
        WORLD_DETAILS['detlaactive'] = 0
        WORLD_DETAILS['deltarecovered'] = 0
        WORLD_DETAILS['deltadeaths'] = DATA['todayDeaths']

        WORLD_DETAILS['affectedCountries'] = DATA['affectedCountries']

        return WORLD_DETAILS

    except Exception as e:
        return None


def fetch_country_details(country):
    try:
        COUNTRIES_DATA = send_request(COUNTRIES_API)
        DATA = {}

        if country != "all":
            for COUNTRY_DATA in COUNTRIES_DATA:
                if COUNTRY_DATA['country'].lower() == country.lower():
                    DATA = COUNTRY_DATA
                    break

                if 'countryInfo' in COUNTRY_DATA:
                    if 'iso2' in COUNTRY_DATA['countryInfo'] and \
                       COUNTRY_DATA['countryInfo']['iso2'] is not None:
                        if COUNTRY_DATA['countryInfo']['iso2'].lower() == country.lower():
                            DATA = COUNTRY_DATA
                            break

                    if 'iso3' in COUNTRY_DATA['countryInfo'] and \
                       COUNTRY_DATA['countryInfo']['iso3'] is not None:
                        if COUNTRY_DATA['countryInfo']['iso3'].lower() == country.lower():
                            DATA = COUNTRY_DATA
                            break
            COUNTRY_DETAILS = {}
            COUNTRY_DETAILS['state'] = DATA['country']
            COUNTRY_DETAILS['lastupdatedtime'] = time.strftime(
                '%d/%H/%Y %H:%M',
                time.gmtime(DATA['updated']/1000)
            )
            COUNTRY_DETAILS['confirmed'] = DATA['cases']
            COUNTRY_DETAILS['active'] = DATA['active']
            COUNTRY_DETAILS['recovered'] = DATA['recovered']
            COUNTRY_DETAILS['deaths'] = DATA['deaths']

            COUNTRY_DETAILS['deltaconfirmed'] = DATA['todayCases']
            COUNTRY_DETAILS['detlaactive'] = 0
            COUNTRY_DETAILS['deltarecovered'] = 0
            COUNTRY_DETAILS['deltadeaths'] = DATA['todayDeaths']

            COUNTRY_DETAILS['critical'] = DATA['critical']

            return COUNTRY_DETAILS
        else:
            COUNTRIES_DETAILS = []
            for DATA in COUNTRIES_DATA:
                COUNTRY_DETAILS = {}
                COUNTRY_DETAILS['state'] = DATA['country']
                COUNTRY_DETAILS['lastupdatedtime'] = time.strftime(
                    '%d/%H/%Y %H:%M',
                    time.gmtime(DATA['updated']/1000)
                )
                COUNTRY_DETAILS['confirmed'] = DATA['cases']
                COUNTRY_DETAILS['active'] = DATA['active']
                COUNTRY_DETAILS['recovered'] = DATA['recovered']
                COUNTRY_DETAILS['deaths'] = DATA['deaths']

                COUNTRY_DETAILS['deltaconfirmed'] = DATA['todayCases']
                COUNTRY_DETAILS['detlaactive'] = 0
                COUNTRY_DETAILS['deltarecovered'] = 0
                COUNTRY_DETAILS['deltadeaths'] = DATA['todayDeaths']

                COUNTRY_DETAILS['critical'] = DATA['critical']
                COUNTRIES_DETAILS.append(COUNTRY_DETAILS)
            return COUNTRIES_DETAILS

    except Exception as e:
        return None


def fetch_sos_details():
    print("_______Helpline Numbers___________\n")
    print("1. Andra Pradesh : 0866-2410978")
    print("2. Arunachal Pradesh : 9436055743")
    print("3. Assam : 6913347770")
    print("4. Bihar : 104")
    print("5. Chhattisgarh : 104")
    print("6. Goa : 104")
    print("7. Gujrat : 104")
    print("8. Haryana : 8558893911")
    print("9. Himachal Pradesh : 104")
    print("10. Jharkhand : 104")
    print("11. Karnataka : 104")
    print("12. Kerala : 0471-2552056")
    print("13. Madhya Pradesh : 104")
    print("14. Maharashtra : 020-26127394")
    print("15. Manipur : 3852411668")
    print("16. Meghalaya : 108")
    print("17. Mizoram : 102")
    print("18. Nagaland : 7005539653")
    print("19. Odisha : 9439994859")
    print("20. Punjab : 104")
    print("21. Rajasthan : 0141-2225624")
    print("22. Sikkim : 104")
    print("23. Tamil Nadu : 044-29510500")
    print("24. Telangana : 104")
    print("25. Tripura : 0381-2315879")
    print("26. Uttarakhand : 104")
    print("27. Uttar Pradesh  : 18001805145")
    print("28. West Bengal : 1800313444222, 03323412600")
    print("")
    print("1.Andaman and Nicobar Islands : 03192-232102")
    print("2. Chandigarh : 9779558282")
    print("3. Dadra and Nagar Haveli and Daman & Diu 1 : 104")
    print("4. Delhi : 011-22307145")
    print("5. Jammu & Kashmir  : 01912520982, 0194-2440283")
    print("6. Ladakh : 01982256462")
    print("7. Lakshadweep : 104")
    print("8. Puducherry : 104")
    print("")
    print("")
    print("______________HELPFUL LINKS______________")
    print("https://www.mohfw.gov.in/pdf/coronvavirushelplinenumber.pdf")
    print("https://www.mohfw.gov.in/")
    print("https://www.who.int/emergencies/diseases/novel-coronavirus-2019")
    print("https://www.cdc.gov/coronavirus/2019-ncov/faq.html")
    print("https://coronavirus.thebaselab.com/")
    print("")
    print("")
