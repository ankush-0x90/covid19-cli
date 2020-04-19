from covid19 import fetcher, parser, printer
from covid19.logger import log_error

COUNTRY_DETAILS = {}
STATE_DETAILS = {}
WORLD_DETAILS = {}


def fetch_cases(args, VERSION):
    if args.emergency:
        # SOS emergency is set
        fetcher.fetch_sos_details()
    else:
        # Show world details as default
        if args.country:
            if args.country.lower() in ['india', 'in', 'ind']:
                COUNTRY_DETAILS = fetcher.fetch_india_status()
                if not COUNTRY_DETAILS:
                    log_error("During fetching India status! Please try again!")
                    return
                parser.global_parser(COUNTRY_DETAILS)

                if args.state:
                    STATE_DETAILS = fetcher.fetch_india_status(args.state)
                    if not STATE_DETAILS:
                        log_error("State not found or something else!")
                        return
                    # run a different parser if all states are requested
                    if args.state.lower() == "all":
                        parser.global_parser_multiple(STATE_DETAILS)
                    else:
                        parser.global_parser(STATE_DETAILS)
            elif args.country.lower() == "world":
                WORLD_DETAILS = fetcher.fetch_world_details()
                if not WORLD_DETAILS:
                    log_error("Error Occured while fetching world details.")
                parser.global_parser(WORLD_DETAILS)
            else:
                COUNTRY_DETAILS = fetcher.fetch_country_details(args.country)
                if not COUNTRY_DETAILS:
                    log_error("Error Occured whie fetching country details")
                else:
                    parser.global_parser(COUNTRY_DETAILS)
