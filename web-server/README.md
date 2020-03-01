# Instantiate repo with venv and install required libraries
virtualenv .env && source .env/bin/activate && pip install --user -r requirements.txt
