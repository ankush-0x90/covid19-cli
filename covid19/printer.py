import os
import platform
import colorama


class Rangebi:
    # colour constants
    # Issue#6 temparary printing in white for windows
    if platform.system() == 'Windows':
        colorama.init()

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    def get_in_danger(self, message):
        return Rangebi.FAIL + str(message) + Rangebi.ENDC

    def get_in_warning(self, message):
        return Rangebi.WARNING + str(message) + Rangebi.ENDC

    def get_in_bold(self, message):
        return Rangebi.BOLD + str(message) + Rangebi.ENDC

    def get_in_success(self, message):
        return Rangebi.OKGREEN + str(message) + Rangebi.ENDC

    def get_in_info(self, message):
        return Rangebi.OKBLUE + str(message) + Rangebi.ENDC


def new_lines(count=1):
    print(end="\n"*count)


def get_tab(count=1):
    print("\t"*count, end="")


def print_covid19_cli_info(VERSION):
    rangebi = Rangebi()
    new_lines()
    print(
        rangebi.get_in_bold(
            rangebi.get_in_success(
                "\t\tWelcome to Covid19-Cli (Version={})".format(VERSION)
            )
        )
    )
    new_lines()


def print_covid19_cli_credits():
    rangebi = Rangebi()
    print(
        rangebi.get_in_info("## Credits :")
    )
    new_lines()
    print(
        rangebi.get_in_warning("- MIT Licensed")
    )
    new_lines()
    print(
        "- Contributors :"
    )
    print(
        "\t\t- ",
        rangebi.get_in_success(
            "asprazz (https://github.com/asprazz) (owner)"
        )
    )
    new_lines()
    print(
        "\t\t- ",
        rangebi.get_in_success(
            "KulkarniSuraj (https://github.com/KulkarniSuraj)"
        )
    )
    new_lines()
