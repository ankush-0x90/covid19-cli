import argparse
from covid19.functions import fetch_cases
from covid19.logger import log_error


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
    if not args:
        log_error("Error occured")
    fetch_cases(args)


if __name__ == '__main__':
    main()
