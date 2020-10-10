#! /usr/bin/env python3

import argparse
from covid19 import functions, printer

VERSION = "1.1.2"


def main():

    parser = argparse.ArgumentParser(
        description="A CLI for fetching covid19 info."
    )

    # adding arguments
    parser.add_argument(
            "country",
            help="(str) which country you want to fetch details of"
        )
    parser.add_argument(
            "-a",
            "--all",
            default=False,
            help="Display all the info available i. if world -> all countries",
            action="store_true"
        )
    parser.add_argument(
            "-s",
            "--state",
            help="(string) state name (correct, case-insensetive) to track"
        )
    parser.add_argument(
            "-e",
            "--emergency",
            help="print emergency contact numbers and helpful links",
            action="store_true"
        )
    parser.add_argument(
            "-i",
            "--interactive",
            default=False,
            help="start interactive interface",
            action="store_true"
        )

    args = parser.parse_args()

    printer.print_covid19_cli_info(VERSION)
    functions.fetch_cases(args, VERSION)
    printer.print_covid19_cli_credits()


def __get_version():
    return VERSION


if __name__ == '__main__':
    main()
