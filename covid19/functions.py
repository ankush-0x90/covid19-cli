from covid19 import fetcher, parser, printer
from covid19.logger import log_error


COUNTRY_DETAILS = {}
STATE_DETAILS = {}


def fetch_cases(args, VERSION):
    global COUNTRY_DETAILS
    global STATE_DETAILS
    if args.emergency:
        # SOS emergency is set
        fetcher.fetch_sos_details()
    else:
        # Show world details as default
        if args.country and args.country.lower() == 'india':
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
                parser.global_parser(STATE_DETAILS)


def print_covid19_cli_info(VERSION):
    rangebi = printer.Rangebi()
    printer.new_lines()
    print(
        rangebi.get_in_bold(
            rangebi.get_in_success(
                "\t\tWelcome to Covid19-Cli (Version={})".format(VERSION)
            )
        )
    )
    printer.new_lines()


def print_covid19_cli_credits():
    rangebi = printer.Rangebi()
    print(
        rangebi.get_in_info("## Credits :")
    )
    printer.new_lines()
    print(
        rangebi.get_in_warning("- MIT Licensed")
    )
    printer.new_lines()
    print(
        "- Contributors :"
    )
    print(
        "\t\t- ",
        rangebi.get_in_success(
            "asprazz (https://github.com/asprazz) (owner)"
        )
    )
    printer.new_lines()
    print(
        "\t\t- ",
        rangebi.get_in_success(
            "KulkarniSuraj (https://github.com/KulkarniSuraj)"
        )
    )
    printer.new_lines()
