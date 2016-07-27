import unittest
from nose.tools import assert_equals
from nose.tools import assert_true
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

#this class has all the UI components which can be accessed from different tests
class master:
    def access_url(self,url):
        self.url=url
        self.driver = webdriver.Firefox()
        global  driver;
        driver = self.driver
        driver.get(url)
    def menuitem_location(self):
        url="https://webapp4-qa.asu.edu/programs/t5/undergrad/false"
        self.access_url(url)
        #for downtown phoenix
        select=Select(driver.find_element_by_id("location-dropdown"))
        select.select_by_visible_text('Downtown Phoenix campus')
        driver.find_element_by_id("GoCollege").click()
        assert_equals('Downtown Phoenix',driver.find_element_by_css_selector('.easy-breadcrumb_segment-title').text)
        #for poly campus
        driver.get("https://webapp4-qa.asu.edu/programs/t5/undergrad/false")
        select = Select(driver.find_element_by_id("location-dropdown"))
        select.select_by_visible_text('Polytechnic campus')
        driver.find_element_by_id("GoCollege").click()
        assert_equals('Polytechnic', driver.find_element_by_css_selector('.easy-breadcrumb_segment-title').text)
        # for ASU @GILA VALLEY
        driver.get("https://webapp4-qa.asu.edu/programs/t5/undergrad/false")
        select = Select(driver.find_element_by_id("location-dropdown"))
        select.select_by_visible_text('Polytechnic campus')
        driver.find_element_by_id("GoCollege").click()
        assert_equals('ASU@TheGilaValley', driver.find_element_by_css_selector('.easy-breadcrumb_segment-title').text)
        driver.find_element_by_link_text('Undergraduate Degrees').click()
        driver.close()
    def keywordsearch(self):
        url="https://webapp4-qa.asu.edu/programs/t5/undergrad/false"
        self.access_url(url)
        #positive test
        driver.find_element_by_css_selector(".keywordEntry").send_keys("computer")
        driver.find_element_by_id("GoCollege").click()
        assert(True,driver.find_element_by_id('programsTable'))
        driver.find_element_by_link_text('Undergraduate Degrees').click()
        #negative test
        self.access_url(url)
        driver.find_element_by_css_selector("input#keywordEntry.defaultText.keywordEntry").send_keys("qwert")
        driver.find_element_by_id("GoCollege").click()
        assert_true(driver.page_source.contains("This Search returned no results"))
        driver.find_element_by_link_text('Undergraduate Degrees').click()
        driver.close()
    def additional_Options(self):
        url = "https://webapp4-qa.asu.edu/programs/t5/undergrad/false"
        self.access_url(url)
        list=['ONLNE','accelerate','concurrent']
        names=['Online','','Concurrent Degrees']
        for i in range(0,3):
            driver.find_element_by_id(list[i]).click()
            driver.find_element_by_id(list[i]).send_keys(Keys.SPACE)
            driver.find_element_by_id("GoCollege").click()
            assert_equals(names[i],driver.find_element_by_css_selector('.easy-breadcrumb_segment-title').text)
            print("*******"+list[i]+"passed *********")










x=master()
x.additional_Options()

