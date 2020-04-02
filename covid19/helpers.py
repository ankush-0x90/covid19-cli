import requests
from .logger import log_error


def send_request(API_URI, method="GET"):
    try:
        response = requests.get(API_URI)
        COVID_JSON = response.json()
        return COVID_JSON
    except requests.RequestException:
        log_error("Request Exception Occured!\nPlease check network connectivity or try again.")