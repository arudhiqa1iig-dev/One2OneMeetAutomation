# One2One Meet - POM Automation

## Setup
1. Install dependencies:
   pip install -r requirements.txt

2. Open test.py and update your credentials:
   USERNAME = "your_username"
   PASSWORD = "your_password"

## Run
   python test.py

## Project Structure
   one2one_pom/
   ├── test.py              ← run this
   ├── requirements.txt
   └── pages/
       ├── home_page.py     ← scroll + go to contact
       ├── contact_page.py  ← fill contact form
       └── login_page.py    ← fill login + click button
