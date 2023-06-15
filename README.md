# Service with Contacts
This project is a service that allows users to search for contacts. It integrates with the Nimble API to periodically update and synchronize contacts from an external source. Users can perform a full-text search on the contacts stored in the database.

## Features
Periodically updates contacts from the Nimble API.
Stores contact information in a PostgreSQL database.
Provides a search API endpoint for searching contacts.
Imports contacts from a CSV file.


### Installation and Setup

1. Clone the repo
`git clone https://github.com/oksanaaam/service_with_contacts.git`
2. Open the project folder in your IDE
3. Open a terminal in the project folder
4. If you are using PyCharm - it may propose you to automatically create venv for your project and install requirements in it, but if not:
```
python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
pip install -r requirements.txt
```


### Installation PostgreSQL and create database.

Set the required environment variables in .env.sample file:

```
SECRET_KEY=<your SECRET_KEY>
ALLOWED_HOSTS=<your ALLOWED_HOSTS>
DEBUG = <your debug>

POSTGRES_HOST=<your db hostname>
POSTGRES_DB=<your db name>
POSTGRES_USER=<your user name>
POSTGRES_PASSWORD=<your password>

HEADERS_AUTHORIZATION=<your headers password>
```

### Run database migrations:

```
python manage.py makemigrations
python manage.py migrate
``` 

Import contacts from a CSV file:

`python utils.py`

## Usage

Start the server:

`python manage.py runserver`

### API documentation

Access the API documentation at http://localhost:8000/swagger to view the available API endpoints and their usage details.

Perform a search for contacts by making a GET request to the search API endpoint:

GET "http://localhost:8000/service/contact/search/?query=<search_query>"
Replace <search_query> with the desired text to search for in the contacts.

![doc_query.png](img%20for%20README.md%2Fdoc_query.png)

![doc_response.png](img%20for%20README.md%2Fdoc_response.png)

![API_searching.png](img%20for%20README.md%2FAPI_searching.png)

The response will be a list of contacts matching the search query.

### Scheduled Contact Update
The project includes a scheduled task that updates the contacts from the Nimble API periodically. By default, the task runs every day at 12:00 PM. You can customize the schedule in the update_contacts_scheduler.py file.

### Testing
To run tests for the project, execute the following command:

`python manage.py test`

