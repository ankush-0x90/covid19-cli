import requests
from covid19 import logger, printer

from halo import Halo


def send_request(API_URI, method="GET"):
    spinner = Halo(text='\t Hold on a second ....', spinner='dots')
    spinner.start()
    try:
        response = requests.get(API_URI, timeout=5)
        resp_json = response.json()
        spinner.stop()
        return resp_json
    except Exception:
        logger.log_error(
            "Request Exception Occured! Please check network connection"
        )
    spinner.stop()
