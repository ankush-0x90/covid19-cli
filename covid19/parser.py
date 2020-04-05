from covid19 import printer
from covid19.logger import log_error

from prettytable import PrettyTable


def parse_country_details(COUNTRY_DETAILS):
    try:
        x = PrettyTable()
        rangebi = printer.Rangebi()

        # parsing country details

        last_updated_on = COUNTRY_DETAILS['lastupdatedtime']

        total_confirmed_cases = COUNTRY_DETAILS['confirmed']
        total_active_cases = COUNTRY_DETAILS['active']
        total_recovered_cases = COUNTRY_DETAILS['recovered']
        total_deceased_cases = COUNTRY_DETAILS['deaths']

        delta_confirmed_cases = COUNTRY_DETAILS['deltaconfirmed']
        delta_active_cases = 0
        delta_recovered_cases = COUNTRY_DETAILS['deltarecovered']
        delta_deceased_cases = COUNTRY_DETAILS['deltadeaths']

        if ('delta' in COUNTRY_DETAILS):
            delta_confirmed_cases = COUNTRY_DETAILS['delta']['confirmed']
            delta_active_cases = COUNTRY_DETAILS['delta']['active']
            delta_recovered_cases = COUNTRY_DETAILS['delta']['recovered']
            delta_deceased_cases = COUNTRY_DETAILS['delta']['deaths']

        print(
            rangebi.get_in_bold(rangebi.get_in_warning("# INDIA Status \t")),
            "last update on :",
            rangebi.get_in_info(last_updated_on)
        )

        x.field_names = [
            rangebi.get_in_info(" Confirmed "),
            rangebi.get_in_warning(" Active "),
            rangebi.get_in_success(" Recovered "),
            rangebi.get_in_danger(" Deceased "),
        ]

        x.add_row([
            str(total_confirmed_cases) +
            rangebi.get_in_danger(" (+" + str(delta_confirmed_cases) + ")"),
            str(total_active_cases) +
            rangebi.get_in_danger(" (+" + str(delta_active_cases) + ")"),
            str(total_recovered_cases) +
            rangebi.get_in_success(" (+" + str(delta_recovered_cases) + ")"),
            str(total_deceased_cases) +
            rangebi.get_in_danger(" (+" + str(delta_deceased_cases) + ")")
        ])

        print(x)
        printer.new_lines(1)

    except Exception as e:
        print(e)
        log_error("Excpetion occured while parsing")


def parse_state_details(STATE_DETAILS):
    try:
        x = PrettyTable()
        rangebi = printer.Rangebi()

        # parsing state details
        state = STATE_DETAILS['state']
        last_updated_on = STATE_DETAILS['lastupdatedtime']

        total_confirmed_cases = STATE_DETAILS['confirmed']
        total_active_cases = STATE_DETAILS['active']
        total_recovered_cases = STATE_DETAILS['recovered']
        total_deceased_cases = STATE_DETAILS['deaths']

        delta_confirmed_cases = STATE_DETAILS['deltaconfirmed']
        delta_active_cases = 0
        delta_recovered_cases = STATE_DETAILS['deltarecovered']
        delta_deceased_cases = STATE_DETAILS['deltadeaths']

        if ('delta' in STATE_DETAILS):
            delta_confirmed_cases = STATE_DETAILS['delta']['confirmed']
            delta_active_cases = STATE_DETAILS['delta']['active']
            delta_recovered_cases = STATE_DETAILS['delta']['recovered']
            delta_deceased_cases = STATE_DETAILS['delta']['deaths']

        print(
            rangebi.get_in_bold(
                rangebi.get_in_warning(
                    "# {} Status ".format(state)
                )
            ),
            "last update on :",
            rangebi.get_in_info(last_updated_on)
        )

        x.field_names = [
            rangebi.get_in_info(" Confirmed "),
            rangebi.get_in_warning(" Active "),
            rangebi.get_in_success(" Recovered "),
            rangebi.get_in_danger(" Deceased "),
        ]

        x.add_row([
            str(total_confirmed_cases) +
            rangebi.get_in_danger(" (+" + str(delta_confirmed_cases) + ")"),
            str(total_active_cases) +
            rangebi.get_in_danger(" (+" + str(delta_active_cases) + ")"),
            str(total_recovered_cases) +
            rangebi.get_in_success(" (+" + str(delta_recovered_cases) + ")"),
            str(total_deceased_cases) +
            rangebi.get_in_danger(" (+" + str(delta_deceased_cases) + ")")
        ])

        print(x)
        printer.new_lines(1)

    except Exception as e:
        log_error("Excpetion occured while parsing")
