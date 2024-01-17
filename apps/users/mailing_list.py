import json

import requests
from django.conf import settings
from sentry_sdk import capture_exception


def using_mailing_list():
    return settings.EMAIL_OCTOPUS_API_KEY and settings.EMAIL_OCTOPUS_LIST_ID


def subscribe_to_mailing_list(email_address):
    if not using_mailing_list():
        return
    try:
        add_contact_url = f"https://emailoctopus.com/api/1.6/lists/{settings.EMAIL_OCTOPUS_LIST_ID}/contacts"
        parameters = {
            "api_key": settings.EMAIL_OCTOPUS_API_KEY,
            "email_address": email_address,
            "tags": [
                "site-signup",
            ],
        }
        headers = {"Content-Type": "application/json"}
        requests.post(add_contact_url, data=json.dumps(parameters), headers=headers)
    except Exception as e:
        # capture errors but don't crash
        capture_exception(e)
