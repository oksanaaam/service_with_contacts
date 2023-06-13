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


file_path = "../data/nimble_contacts.csv"
import_data_from_csv(file_path)