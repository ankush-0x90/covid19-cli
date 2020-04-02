from .helpers import send_request
from .logger import log_error


def fetch_details(API_URI):
    return send_request(API_URI)


def fetch_country_details(COVID_JSON):
    total_count = 0
    state_unknowns = 0

    for state in COVID_JSON:
        try:
            if state == "Unknown":
                for district in COVID_JSON[state]['districtData']:
                    state_unknowns += int(COVID_JSON[state]['districtData'][district]['confirmed'])
            else:
                for district in COVID_JSON[state]['districtData']:
                    total_count += int(COVID_JSON[state]['districtData'][district]['confirmed'])
        except Exception as e:
            log_error("Data missplaced! Try after some time")
    return total_count, state_unknowns


def print_sos_details():
    print("_______Helpline Numbers___________\n")
    print("1. Andra Pradesh : 0866-2410978")
    print("2. Arunachal Pradesh : 9436055743")
    print("3. Assam : 6913347770")
    print("4. Bihar : 104")
    print("5. Chhattisgarh : 104")
    print("6. Goa : 104")
    print("7. Gujrat : 104")
    print("8. Haryana : 8558893911")
    print("9. Himachal Pradesh : 104")
    print("10. Jharkhand : 104")
    print("11. Karnataka : 104")
    print("12. Kerala : 0471-2552056")
    print("13. Madhya Pradesh : 104")
    print("14. Maharashtra : 020-26127394")
    print("15. Manipur : 3852411668")
    print("16. Meghalaya : 108")
    print("17. Mizoram : 102")
    print("18. Nagaland : 7005539653")
    print("19. Odisha : 9439994859")
    print("20. Punjab : 104")
    print("21. Rajasthan : 0141-2225624")
    print("22. Sikkim : 104")
    print("23. Tamil Nadu : 044-29510500")
    print("24. Telangana : 104")
    print("25. Tripura : 0381-2315879")
    print("26. Uttarakhand : 104")
    print("27. Uttar Pradesh  : 18001805145")
    print("28. West Bengal : 1800313444222, 03323412600")
    print("")
    print("1.Andaman and Nicobar Islands : 03192-232102")
    print("2. Chandigarh : 9779558282")
    print("3. Dadra and Nagar Haveli and Daman & Diu 1 : 104")
    print("4. Delhi : 011-22307145")
    print("5. Jammu & Kashmir  : 01912520982, 0194-2440283")
    print("6. Ladakh : 01982256462")
    print("7. Lakshadweep : 104")
    print("8. Puducherry : 104")
    print("")
    print("")
    print("______________HELPFUL LINKS______________")
    print("https://www.mohfw.gov.in/pdf/coronvavirushelplinenumber.pdf")
    print("https://www.mohfw.gov.in/")
    print("https://www.who.int/emergencies/diseases/novel-coronavirus-2019")
    print("https://www.cdc.gov/coronavirus/2019-ncov/faq.html")
    print("https://coronavirus.thebaselab.com/")
    print("")
    print("")
