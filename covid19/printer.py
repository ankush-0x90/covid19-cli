import os
import platform


class Rangebi:
    # colour constants
    # Issue#6 temparary printing in white for windows
    if platform.system() == 'Linux' or platform.system() == 'Darwin':
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
    else:
        HEADER = ''
        OKBLUE = ''
        OKGREEN = ''
        WARNING = ''
        FAIL = ''
        ENDC = ''
        BOLD = ''
        UNDERLINE = ''

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
    i = 0
    while i < count:
        print("")
        i += 1
