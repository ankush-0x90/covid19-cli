import requests
from .logger import log_error


def send_request(API_URI, method="GET"):
    try:
        response = requests.get(API_URI)
        resp_json = response.json()
        return resp_json
    except requests.RequestException:
        log_error("Request Exception Occured! Please check network connection")
