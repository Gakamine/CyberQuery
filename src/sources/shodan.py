from dotenv import load_dotenv
from shodan import Shodan
import os

load_dotenv()
api = Shodan(os.environ.get('SHODAN_API'))

def run(query,context):
    if context == "ip_address":
        result = ip_context(query)
    return result

def ip_context(query):
    ipinfo = api.host(query)
    return ipinfo