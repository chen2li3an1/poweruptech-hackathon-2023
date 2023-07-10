import json
from .company import Company
from .person import Person
from .objects import Contact, Institution, Experience, Education, Interest, Accomplishment
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

# custom JSON encoder to turn linkedin_scraper/ objects into JSON
class Custom_Obj_Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (Company, Person, Contact, Institution, Experience, Education, Interest, Accomplishment)): 
            return obj.__dict__
        elif isinstance(obj, WebDriver):
            return obj.name
        elif isinstance(obj, WebElement):
            return f"webelement"
        return super().default(obj)