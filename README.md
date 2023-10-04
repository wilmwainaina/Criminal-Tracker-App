## Project Overview
This is a Crime Management System designed with Flask. It allows users to manage crimes, victims, and suspects. It uses PostgreSQL as a database for data storage.
The system includes authentication using JWT and checks for user identity before accessing certain routes. The application is well-tested and includes a set of unit tests for important functions.
## Setup & Installation
1. Clone this repository.
```bash
git clone https://github.com/wilmwainaina/Criminal-Tracker-App
cd app
Shell Script

Copy

Insert
cd Crime-Management-System
Install the required packages.
Shell Script

Copy

Insert
pip install -r requirements.txt
Update the SQLALCHEMY_DATABASE_URI configuration in main.py with your sqliteinstance.

Run the server.

Shell Script

Copy

Insert
python app.py
Routes
The application supports the following operations:

Login: POST /login
Retrieve all crimes: GET /crimes
Create new crime: POST /crimes
Retrieve all suspects: GET /suspects
Create new suspect: POST /suspects
Retrieve/Update/Delete specific suspect by id: GET/PUT/DELETE /suspects/<int:id>
Retrieve all victims: GET /victims
Create new victim: POST /victims
Retrieve/Update/Delete specific victim by id: GET/PUT/DELETE /victims/<int:id>
Testing
Run the tests.

Shell Script

Copy

Insert
python -m unittest test_auth.py
Seeding the Database
Run the seed file.

Shell Script

Copy

Insert
python seed.py
Contributing
[Pull requests are welcome.]