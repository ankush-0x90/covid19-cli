class Rangebi:
    # colour constants
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    def get_in_danger(_self, message):
        return Rangebi.FAIL + str(message) + Rangebi.ENDC

    def get_in_warning(_self, message):
        return Rangebi.WARNING + str(message) + Rangebi.ENDC

    def get_in_bold(_self, message):
        return Rangebi.BOLD + str(message) + Rangebi.ENDC

    def get_in_success(_self, message):
        return Rangebi.OKGREEN + str(message) + Rangebi.ENDC

    def get_in_info(_self, message):
        return Rangebi.OKBLUE + str(message) + Rangebi.ENDC


def new_lines(count=1):
    i = 0
    while i < count:
        print("")
        i += 1
