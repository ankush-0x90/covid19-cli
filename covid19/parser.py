from covid19 import printer
from covid19.logger import log_error

from prettytable import PrettyTable


def global_parser(DETAILS):
    try:
        x = PrettyTable(padding_width=3)
        rangebi = printer.Rangebi()

        # parsing country details

        last_updated_on = DETAILS['lastupdatedtime']
        details_for = DETAILS['state']
        if details_for.lower() == 'total':
            details_for = 'India'

        total_confirmed_cases = DETAILS['confirmed']
        total_active_cases = DETAILS['active']
        total_recovered_cases = DETAILS['recovered']
        total_deceased_cases = DETAILS['deaths']

        delta_confirmed_cases = DETAILS['deltaconfirmed']
        delta_active_cases = 0
        delta_recovered_cases = DETAILS['deltarecovered']
        delta_deceased_cases = DETAILS['deltadeaths']

        if ('delta' in DETAILS):
            delta_confirmed_cases = DETAILS['delta']['confirmed']
            delta_active_cases = DETAILS['delta']['active']
            delta_recovered_cases = DETAILS['delta']['recovered']
            delta_deceased_cases = DETAILS['delta']['deaths']

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
            rangebi.get_in_warning(" (+" + str(delta_active_cases) + ")"),
            str(total_recovered_cases) +
            rangebi.get_in_success(" (+" + str(delta_recovered_cases) + ")"),
            str(total_deceased_cases) +
            rangebi.get_in_danger(" (+" + str(delta_deceased_cases) + ")")
        ])

        printer.get_tab()
        print(
            rangebi.get_in_bold(
                rangebi.get_in_warning("# {} Status \t").format(details_for)
            ),
            "last update on :",
            rangebi.get_in_info(last_updated_on)
        )

        print(x)
        printer.new_lines(1)

    except Exception as e:
        log_error("Excpetion occured while parsing")
