from simple_salesforce import Salesforce
from core.settings import DATABASES
# from core.settings import USER,SALESFORCE_SECURITY_TOKEN, SALESFORCE_PASSWORD, SALESFORCE_DOMAIN

def login():
    return Salesforce(
        username= USER,
        password=PASSWORD,
        security_token=CONSUMER_KEY,
        domain=SALESFORCE_DOMAIN
    )
