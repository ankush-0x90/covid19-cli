from covid19 import printer


def log_error(message):
    rangebi = printer.Rangebi()
    print(
        rangebi.get_in_danger("** Error Occured")
    )
    printer.new_lines()
    print(
        rangebi.get_in_warning("\t" + message)
    )
    printer.new_lines()
    print(
        rangebi.get_in_danger("** Exiting...")
    )
    printer.new_lines(2)
