from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options
from functools import cached_property

class BrowserDriver:
    @cached_property
    def driver(self):
        firefox_options = Options();
        firefox_options.add_argument("-profile")
        # user_profile
        user_profile_name = "User"
        # user_profile_name = "dbura"
        firefox_options.add_argument("C:/Users/"+ user_profile_name + "/AppData/Roaming/Mozilla/Firefox/Profiles/searchpartuser")
       

        return webdriver.Firefox(service=Service('./geckodriver.exe'), options=firefox_options)