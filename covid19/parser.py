from datetime import datetime

from prettytable import PrettyTable

from covid19 import printer, logger, helpers


def global_parser(DETAILS):
    try:
        x = PrettyTable(padding_width=3)
        rangebi = printer.Rangebi()

        # parsing country details

        last_updated_on = DETAILS['lastupdatedtime']
        details_for = DETAILS['state']
        if details_for.lower() == 'total':
            details_for = 'India'

        total_confirmed_cases = helpers.formate_num(int(DETAILS['confirmed']))
        total_active_cases = helpers.formate_num(int(DETAILS['active']))
        total_recovered_cases = helpers.formate_num(int(DETAILS['recovered']))
        total_deceased_cases = helpers.formate_num(int(DETAILS['deaths']))

        delta_confirmed_cases = helpers.formate_num(
                                int(DETAILS['deltaconfirmed'])
                            )
        delta_active_cases = 0
        delta_recovered_cases = helpers.formate_num(
                                int(DETAILS['deltarecovered'])
                            )
        delta_deceased_cases = helpers.formate_num(
                                int(DETAILS['deltadeaths'])
                            )

        if ('delta' in DETAILS):
            delta_confirmed_cases = helpers.formate_num(
                                    int(DETAILS['delta']['confirmed'])
                                )
            delta_active_cases = helpers.formate_num(
                                    int(DETAILS['delta']['active'])
                                )
            delta_recovered_cases = helpers.formate_num(
                                    int(DETAILS['delta']['recovered'])
                                )
            delta_deceased_cases = helpers.formate_num(
                                    int(DETAILS['delta']['deaths'])
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
            rangebi.get_in_warning(" (+" + str(delta_active_cases) + ")"),
            str(total_recovered_cases) +
            rangebi.get_in_success(" (+" + str(delta_recovered_cases) + ")"),
            str(total_deceased_cases) +
            rangebi.get_in_danger(" (+" + str(delta_deceased_cases) + ")")
        ])

        printer.new_lines()
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

        if details_for.lower() == "world":
            print(
                rangebi.get_in_danger(
                    "Total Countries Affected: "
                ),
                rangebi.get_in_bold(
                    DETAILS['affectedCountries']
                )
            )
        printer.new_lines(1)

    except Exception as e:
        logger.log_error("Excpetion occured while parsing")


def global_parser_multiple(MULTIPLE_DETAILS, title="State"):
    try:
        x = PrettyTable()
        rangebi = printer.Rangebi()

        x.field_names = [
            rangebi.get_in_info(title),
            rangebi.get_in_info(" Confirmed "),
            rangebi.get_in_warning(" Active "),
            rangebi.get_in_success(" Recovered "),
            rangebi.get_in_danger(" Deceased "),
            rangebi.get_in_danger(" Last Update On "),
        ]
        x.align = "c"
        x.align[rangebi.get_in_info(title)] = "l"
        state_name = ""
        # not used last_udpated_on_obj ?
        last_updated_on = ""
        # parsing country details
        for DETAILS in MULTIPLE_DETAILS:

            # parsing country details
            if title == "State":
                last_updated_on_obj = datetime.strptime(
                    DETAILS['lastupdatedtime'],
                    "%d/%m/%Y %H:%M:%S"
                )
                last_updated_on = last_updated_on_obj.strftime(
                    "%H:%M, on %b %d"
                )
            state_name = DETAILS['state']
            if state_name.lower() == 'total':
                state_name = 'India'

            if len(state_name) > 15:
                state_name_split = state_name.split()
                state_name = state_name_split[0]
                for i in state_name_split[1:]:
                    state_name += " " + i[0] + "."

            total_confirmed_cases = helpers.formate_num(
                                    int(DETAILS['confirmed'])
                                )
            total_active_cases = helpers.formate_num(
                                int(DETAILS['active'])
                            )
            total_recovered_cases = helpers.formate_num(
                                    int(DETAILS['recovered'])
                                )
            total_deceased_cases = helpers.formate_num(int(DETAILS['deaths']))

            delta_confirmed_cases = helpers.formate_num(
                                    int(DETAILS['deltaconfirmed'])
                                )
            delta_active_cases = 0
            delta_recovered_cases = helpers.formate_num(
                                    int(DETAILS['deltarecovered'])
                                )
            delta_deceased_cases = helpers.formate_num(
                                    int(DETAILS['deltadeaths'])
                                )

            if ('delta' in DETAILS):
                delta_confirmed_cases = helpers.formate_num(
                                        int(DETAILS['delta']['confirmed'])
                                    )
                delta_active_cases = helpers.formate_num(
                                        int(DETAILS['delta']['active'])
                                    )
                delta_recovered_cases = helpers.formate_num(
                                        int(DETAILS['delta']['recovered'])
                                    )
                delta_deceased_cases = helpers.formate_num(
                                        int(DETAILS['delta']['deaths'])
                                    )

            x.add_row([
                str(state_name),
                str(total_confirmed_cases) +
                rangebi.get_in_danger(
                    " (+" + str(delta_confirmed_cases) + ")"
                    ),
                str(total_active_cases) +
                rangebi.get_in_warning(
                    " (+" + str(delta_active_cases) + ")"
                    ),
                str(total_recovered_cases) +
                rangebi.get_in_success(
                    " (+" + str(delta_recovered_cases) + ")"
                    ),
                str(total_deceased_cases) +
                rangebi.get_in_danger(
                    " (+" + str(delta_deceased_cases) + ")"
                    ),
                str(last_updated_on)
            ])

        printer.new_lines()
        printer.get_tab()
        print(
            rangebi.get_in_bold(
                rangebi.get_in_warning(
                    "# {} Status \t"
                ).format(title)
            ),
            "Stay Home Stay Safe"
        )
        print(x)
        printer.new_lines(1)

    except Exception as e:
        print(e)
        logger.log_error("Excpetion occured while parsing")
