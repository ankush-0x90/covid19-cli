def log_error(message):
    print("")
    print("")
    print("Error Occured ::")
    print(message)
    print("Exiting......")
    print("")
    print("")
    exit(0)


def log_info(message, total_count, unknowns):
    print(message)
    print("\t- Confirmed Found: ", total_count)
    print("\t- Confirmed Unknowns: ", unknowns)
    print("\t- Total Count: ", total_count+unknowns)
