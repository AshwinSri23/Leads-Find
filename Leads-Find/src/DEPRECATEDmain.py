
#! Currently not being used - Attempting with Selenium

"""
This file contains all the functions (request and helper) that are
abstracted away from the CLI.

Abbreviations:
- SB: ScrapingBee, in-between request proxy server
- RR: RocketReach, main leads search platform
"""

# --- Imports
import os
import requests
from dotenv import load_dotenv
import json


# --- Setup & Constants
load_dotenv()
SB_KEY = os.getenv("SB_KEY")
RR_TEMP_COOKIE = os.getenv("TEMP_COOKIE")
RR_TEMP_CSRFTOKEN = os.getenv("RR_TEMP_CSRFTOKEN")


# --- Functions
def get_temp_mails() -> list[str]:
    """
    Gets a list of temporary email account from the API,
    stores it into a list of used accounts, and returns it.
    """
    pass

def verify_mail(mail: str):
    """
    Opens the verification email in the inbox, extracts the link using BS4,
    and opens it with ScrapingBee to verify account.
    """
    pass

def sb_rr_get_account_info() -> dict:
    """
    Gets RocketReach's currently logged-in user info,
    through the proxy ScrapingBee (requires API key).
    Returns in a subscriptable JSON format.
    For response data format, see example on Postman.
    """

    # Create request and get response
    response = requests.get(
        url='http://rocketreach.co/v1/user',
        params={
            'api_key': SB_KEY,
            'render_js': 'false',
        },
        headers = {
            'Cookie': RR_TEMP_COOKIE
        }
    )

    if (not response.ok):
        # Verify status code
        print("Potential error while running: get_account_info()")
        print('Status Code: ', response.status_code)
        print('Response Body: ', response.content)
    else:
        return json.loads(response.text)

def sb_rr_get_people_by_keywords(keywords: dict) -> dict:
    #! Use RocketReach API V2 instead
    #! https://rocketreach.co/api/docs/#tag/Account

    """
    Gets RocketReach's currently logged-in user info,
    through the proxy ScrapingBee (requires API key).
    Returns in a subscriptable JSON format.
    For keywords & response data format, see example on Postman.
    """

    # Create request and get response
    response = requests.post(
        url='https://rocketreach.co/v2/services/search/person',
        params={
            'api_key': SB_KEY,
            'render_js': 'false',
        },
        headers={
            'accept': 'application/json, text/plain, */*',
            'content-type': 'application/json;charset=UTF-8',
            'cookie': RR_TEMP_COOKIE,
            'referer': 'https://rocketreach.co/person',
            'x-csrftoken': RR_TEMP_CSRFTOKEN
        },
        data='{\"start\":1,\"pageSize\":10,\"excludeContacts\":false,\"searchEventsSessionId\":\"a87fc40b-c97a-4d00-8b9a-36d25ac2035e\",\"name\":\"\",\"geo\":[],\"current_title\":[],\"normalized_title\":[],\"department\":[],\"management_levels\":[],\"job_change_range_days\":null,\"skills\":[],\"years_experience\":null,\"gender\":[],\"veteran_status\":[],\"ethnicity\":[],\"employer\":[\"Microsoft\"],\"company_id\":[],\"company_size\":null,\"company_revenue\":null,\"company_industry\":[],\"company_sic_code\":[],\"company_naics_code\":[],\"major\":[],\"school\":[],\"degree\":[],\"contact_info\":\"\",\"link\":\"\",\"keyword\":\"\",\"company_list\":\"\",\"email_grade\":\"\"}'
    )

    if (response.status_code != 200):
        # Verify status code
        print("Potential error while running: get_account_info()")
        print('Status Code: ', response.status_code)
        print('Response Body: ', response.content)
    else:
        return json.loads(response.text)