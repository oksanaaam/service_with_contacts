import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "service_with_contacts.settings")
django.setup()

import csv
from service.models import Contact


def import_data_from_csv(file_path):
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            contact = Contact(
                first_name=row["first name"],
                last_name=row["last name"],
                email=row["email"],
            )
            contact.save()


if __name__ == "__main__":
    file_path = "../data/nimble_contacts.csv"
    import_data_from_csv(file_path)
