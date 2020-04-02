from covid19.helpers import send_request

DATA_API = "https://api.covid19india.org/data.json"
DISTRICT_WISE_API = "https://api.covid19india.org/state_district_wise.json"


def fetch_country_status():
    DATA = send_request(DATA_API)
    COUNTRY_DETAILS = {}
    COUNTRY_DETAILS = DATA['statewise'][0]
    COUNTRY_DETAILS['key_values'] = DATA['key_values']
    return COUNTRY_DETAILS
