#this class has all the UI components which can be accessed from different tests
'''
Author:braddy
Email:baryasom@asu.edu

8/1/2016
'''
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


class Class_Search_homepage(unittest.TestCase):
    def access_url(self, url):
        self.url = url
        try:
            self.driver=webdriver.Chrome(("C:\Users\bharadwaj\chromedriver.exe").replace("\\","//"))
        except Exception:
            self.driver = webdriver.Firefox()
        global driver;
        driver = self.driver
        driver.get(url)
    def menuitem_Allclasses_radio(self,url):
        #self.access_url(url)
        radio=driver.find_element_by_id("searchTypeAllClass")
        radio.click()
        assert_true(radio.is_selected())
        print"test radio_buttton completed"
        #driver.close()
    def menuitem_Openclasses_radio(self,url):
        #self.access_url(url)
        radio = driver.find_element_by_id("searchTypeOpen")
        radio.click()
        assert_true(radio.is_selected())
        print"test radio_buttton_open completed"
        #driver.close()
    def menuitem_term_open(self, url):
        self.access_url(url)
        select=Select(driver.find_element_by_id("term"))
        length=len(select.options)
        driver.find_element_by_id("searchTypeOpen").click()
        select.select_by_index(0)
        driver.find_element_by_id("subjectEntry").send_keys("CSE")
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "Go")))
        driver.find_element_by_id("Go").click()
        self.openclass=driver.find_element_by_id("NumResults").text
        assert_true(int(self.openclass)>=0)

    def menuitem_term_all(self, url):
        self.access_url(url)
        select = Select(driver.find_element_by_id("term"))
        length = len(select.options)
        driver.find_element_by_id("searchTypeAllClass").click()
        select.select_by_index(0)
        driver.find_element_by_id("subjectEntry").send_keys("CSE")
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "Go")))
        driver.find_element_by_id("Go").click()
        self.allclass = driver.find_element_by_id("NumResults").text
        assert_true(int(self.allclass) >= int(self.openclass))

    def setUp(self):
        print"Start testing"

    def test_radio_buttonall(self):
        url="https://webapp4.asu.edu/catalog/"

        self.menuitem_Allclasses_radio(url)

    def test_radio_buttonopen(self):
        url="https://webapp4.asu.edu/catalog/"
        self.menuitem_Openclasses_radio(url)

    if __name__ == "__main__":
        access_url("https://webapp4.asu.edu/catalog/")
        unittest.main()
