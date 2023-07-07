import getpass
import json
import sys
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# importing 'session' variables from file
PATH_TO_PROJECT = ""
LINKEDIN_USERNAME = ""
with open("variables_liam.json", "r") as f:
    variables = json.loads(f.read())
    PATH_TO_PROJECT = variables["path_to_project"]
    LINKEDIN_USERNAME = variables["linkedin_username"]

# necessary for linkedin_scraper to be able to be imported
sys.path.append(PATH_TO_PROJECT)
from linkedin_scraper import Company, Person, actions, Custom_Obj_Encoder

# setting up selenium webdriver
DRIVER_PATH = 'chromedrivers/chromedriver'
options = Options()
options.add_argument("--window-size=1920,1080")
options.add_argument("--incognito")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
driver = webdriver.Chrome(options=options)


# login to LinkedIn using someone's credentials
email = LINKEDIN_USERNAME
password = getpass.getpass()
actions.login(driver, email, password) # prompts for password in terminal


# helper method to remove illegal chars from a filename
def slugify(filename):
    prohibited = " ().,/\[]\{\}\'\""
    return "".join(x for x in filename if x not in prohibited)


# scraping a specific company
company_url = "https://www.linkedin.com/company/sayyesbuffalo/"
company = Company(linkedin_url=company_url, driver=driver, close_on_complete=False)
print(json.dumps(company, cls=Custom_Obj_Encoder))
with open(f"output/{slugify(company.name)}.json", "w+") as f:
    json.dump(company, f, cls=Custom_Obj_Encoder, indent=4)


# scraping a specified person
person_url = "https://www.linkedin.com/in/keiraogrant/"
person = Person(linkedin_url=person_url, driver=driver, close_on_complete=True)
print(json.dumps(person, cls=Custom_Obj_Encoder))
with open(f"output/{slugify(person.name)}.json", "w+") as f:
    json.dump(person, f, cls=Custom_Obj_Encoder, indent=4)


# export to CSV if needed
# df_person = pd.read_json(person_data)
# df_person.to_csv(f"{person.name}.csv")

