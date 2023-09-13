# autom encam/envio msgs whatsapp web #

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import FirefoxDriverManager


service = Service(FirefoxDriverManager().install())
nav = webdriver.Firefox(service=service)
nav.get("https://web.whatsapp.com/")


