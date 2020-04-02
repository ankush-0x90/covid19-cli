from covid19.helpers import print_sos_details
from covid19.fetcher import fetch_country_status
from covid19.logger import log_error


DATA = {}
COUNTRY_DETAILS = {}


def fetch_cases(args):
    # Show country details as default
    if not args.emergency and not args.district and \
       not args.state:
        COUNTRY_DETAILS = fetch_country_status()
    else:
        # SOS emergency is set
        district_set = False
        state_set = False
        country_set = args.country

        if args.emergency:
            print_sos_details()
        else:
            pass
    print(COUNTRY_DETAILS)
