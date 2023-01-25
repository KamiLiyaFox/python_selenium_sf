from selenium import webdriver
import time
import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from time import sleep
_start = time.time()
br = webdriver.Chrome("E:\GIT\Projects\Skillfactory\python_selenium_sf/chromedriver")
br.get("https://google.com")
br.save_screenshot("screenshot-phantom.png")
br.quit()
_end = time.time()
