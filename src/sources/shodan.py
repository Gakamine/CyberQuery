from dotenv import load_dotenv
from shodan import Shodan
import os

load_dotenv()
api = Shodan(os.environ.get('SHODAN_API'))

def run(query):
    ipinfo = api.host(query)
    return ipinfo