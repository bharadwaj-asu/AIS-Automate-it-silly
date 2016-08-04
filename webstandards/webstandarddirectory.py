#this class has all the UI components which can be accessed from different tests
'''
Author:braddy
Email:baryasom@asu.edu

8/1/2016
'''
import unittest
from nose.tools import assert_equals
from nose.tools import assert_true
from selenium import webdriver
from selenium.webdriver.remote import webelement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement


from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class webstandardsdirectory:
    def asu_headerstandard(self):

        self.asuheader_backgroundcolor="rgba(255, 255, 255, 1)"
        self.asuheader_linkcolor="rgba(0, 0, 0, 1)"
        self.maninmenucolor="rgba(237, 237, 237, 1)"
        self.mainmenucolor_click="rgba(255, 178, 4, 1)"
        self.fontmenu="\"Roboto\""
        self.fontsize="16px"
        self.fontweight="normal"
    def pagecontent_webstandards(self):
        self.font_family_standard = "Roboto,Helvetica Neue,Helvetica,Arial,sans-serif"
        self.primary_font_family_standard="Roboto"