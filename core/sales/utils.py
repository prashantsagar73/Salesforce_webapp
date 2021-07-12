from simple_salesforce import Salesforce
from core.settings import DATABASES
# from core.settings import USER,CONSUMER_KEY,PASSWORD,DOMAIN

# login through salessorce api creaditional 
def login():
    return Salesforce(
        username= USER,
        password=PASSWORD,
        security_token=CONSUMER_KEY,
        domain=SALESFORCE_DOMAIN
    )
