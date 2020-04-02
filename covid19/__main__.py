import argparse
from .functions import \
            fetch_details, \
            fetch_country_details, \
            print_sos_details
from .logger import log_info


API_URI = "https://api.covid19india.org/state_district_wise.json"
COVID_JSON = {}


def main():
    parser = argparse.ArgumentParser(
        description="A CLI for fetching covid19 info."
    )

    # adding arguments
    parser.add_argument(
            "-e",
            "--emergency",
            help="print emergency contact numbers and helpful links",
            action="store_true"
        )
    parser.add_argument(
            "-d",
            "--district",
            help="(string) district name (correct, case-insensetive) to track"
        )
    parser.add_argument(
            "-s",
            "--state",
            help="(string) state name (correct, case-insensetive) to track"
        )
    parser.add_argument(
            "-c",
            "--country",
            default=True,
            help="(boolean) true/false for showing country details",
            action="store_true"
        )
    args = parser.parse_args()

    # Fetch details from api
    COVID_JSON = fetch_details(API_URI)

    # Show country details as default
    if not args.emergency and not args.district and \
       not args.state:
        total_count, state_unknowns = fetch_country_details(COVID_JSON)
        log_info("Country Status : ", total_count, state_unknowns)
    else:
        # SOS emergency is set
        district_set = False
        state_set = False
        country_set = args.country

        if args.emergency:
            print_sos_details()
        else:
            pass


if __name__ == '__main__':
    main()
