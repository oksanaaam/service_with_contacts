import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "service_with_contacts.settings")
django.setup()

import requests
from service.models import Contact


API_URL = "https://api.nimble.com/api/v1/contacts"
HEADERS = {"Authorization": "Bearer dpeiNkeJZCOUEIMThVOzp6JdTa3KIg"}


def update_contacts():
    response = requests.get(API_URL, headers=HEADERS)
    contacts_data = response.json()

    valid_contacts = []
    for contact in contacts_data["resources"]:
        if (
            "object_type" in contact
            and contact["object_type"] == "contact"
            and "fields" in contact
            and "first name" in contact["fields"]
        ):
            valid_contacts.append(contact)

    for contact in valid_contacts:
        first_name = contact["fields"]["first name"][0]["value"]
        last_name = contact["fields"]["last name"][0]["value"]
        email = contact["fields"].get("email", [{"value": "N/A"}])[0]["value"]

        contact_obj, created = Contact.objects.get_or_create(email=email)
        contact_obj.first_name = first_name
        contact_obj.last_name = last_name
        contact_obj.save()

        if created:
            print(f"Created Contact: {contact_obj}")
        else:
            print(f"Updated Contact: {contact_obj}")
