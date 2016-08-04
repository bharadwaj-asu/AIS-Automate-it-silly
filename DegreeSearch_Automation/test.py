#this class has all the UI components which can be accessed from different tests
'''
Author:braddy
Email:baryasom@asu.edu

8/1/2016
'''
from Master import master
import unittest
from nose.tools import assert_equals
from nose.tools import assert_true
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class test(unittest.TestCase):
    def setUp(self):
        self.url="https://webapp4-qa.asu.edu/programs/t5/graduate/false"
        self.mast=master()
        global mas
        mas =self.mast

    def test_locaationdropdown(self):
        mas.menuitem_location(self.url)
        print "completed testlocation"
    def test_keywordsearch(self):
        mas.keywordsearch(self.url)

    def test_additionaloptions(self):
        mas.additional_Options(self.url)

    def test_advancedsearchcollege(self):
        mas.advancedsearch_college(self.url)

    def test_secondlanguage(self):
        mas.radio_secondlanguage(self.url)

    def test_accessimagelinks(self):
        mas.accesslinks(self.url)


if __name__=="__main__":
        unittest.main()
