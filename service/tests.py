import os
import psycopg2
import requests
from dotenv import load_dotenv
from django.test import TestCase
from service.models import Contact
from service.update_contacts_bd import update_contacts
from service.utils import import_data_from_csv

load_dotenv()


class ContactModelTest(TestCase):
    def test_str_representation(self):
        contact = Contact(
            first_name="John", last_name="Doe", email="john.doe@example.com"
        )
        self.assertEqual(str(contact), "John Doe - john.doe@example.com")

    def test_email_uniqueness(self):
        contact1 = Contact(
            first_name="John", last_name="Doe", email="john.doe@example.com"
        )
        contact1.save()

        contact2 = Contact(
            first_name="Jane", last_name="Smith", email="john.doe@example.com"
        )
        with self.assertRaises(Exception):
            contact2.save()


class DBConnectionTest(TestCase):
    def test_database_creation(self):
        connection = psycopg2.connect(
            host=os.environ["POSTGRES_HOST"],
            database=os.environ["POSTGRES_DB"],
            user=os.environ["POSTGRES_USER"],
            password=os.environ["POSTGRES_PASSWORD"],
        )
        cursor = connection.cursor()
        cursor.execute(
            "SELECT datname FROM pg_database WHERE datname=%s",
            (os.environ["POSTGRES_DB"],),
        )
        result = cursor.fetchone()
        connection.close()
        assert result is not None
        assert result[0] == os.environ["POSTGRES_DB"]

        assert connection is not None


class CSVImportTest(TestCase):
    def test_data_import(self):
        file_path = "data/nimble_contacts.csv"

        import_data_from_csv(file_path)

        count = Contact.objects.count()
        expected_count = 10
        self.assertEqual(count, expected_count)


class ContactsUpdateTest(TestCase):
    def test_contacts_update(self):
        update_contacts()

        count = Contact.objects.count()
        self.assertTrue(count > 0)

        contacts = Contact.objects.all()
        for contact in contacts:
            self.assertIsNotNone(contact.first_name)
            self.assertIsNotNone(contact.last_name)
            self.assertIsNotNone(contact.email)


class SearchContactsTest(TestCase):
    def setUp(self):
        Contact.objects.create(
            first_name="John", last_name="Doe", email="johndoe@example.com"
        )
        Contact.objects.create(
            first_name="Jane", last_name="Smith", email="janesmith@example.com"
        )
        Contact.objects.create(
            first_name="David", last_name="Johnson", email="davidjohnson@example.com"
        )

    def test_search_contacts(self):
        query = "John"
        url = "http://127.0.0.1:8000/service/contact/search/"
        response = requests.get(url, params={"query": query})

        self.assertEqual(response.status_code, 200)

        contacts = Contact.objects.all()

        expected_first_name = "John"
        expected_last_name = "Smith"
        expected_email = "davidjohnson@example.com"
        self.assertIn(expected_first_name, [contact.first_name for contact in contacts])
        self.assertIn(expected_last_name, [contact.last_name for contact in contacts])
        self.assertIn(expected_email, [contact.email for contact in contacts])
