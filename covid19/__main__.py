#! /usr/bin/env python3

import argparse
from covid19 import functions


def main():
    VERSION = "1.0.3"

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
            "-s",
            "--state",
            help="(string) state name (correct, case-insensetive) to track"
        )

    args = parser.parse_args()

    functions.print_covid19_cli_info(VERSION)
    functions.fetch_cases(args, VERSION)
    functions.print_covid19_cli_credits()


if __name__ == '__main__':
    main()
