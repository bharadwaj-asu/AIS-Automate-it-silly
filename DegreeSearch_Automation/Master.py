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


class master:
    def access_url(self,url):
        self.url=url
        self.driver = webdriver.Firefox()
        global  driver;
        driver = self.driver
        driver.get(url)
    '''
    This test is to check and determine if they navigate to required pages
    NOTE:Will not check the page if it has all elements'''
    def menuitem_location(self,url):

        self.access_url(url)
        #check if the dropdown label is correct
        locationdropdown=driver.find_element_by_xpath("(//label[@for='location-dropdown'])[1]").text
        #assert_equals(str(locationdropdown),"Where do you want to Study?")
        select=Select(driver.find_element_by_id("location-dropdown"))
        length=len(select.options)
        #check it has all the elements
        assert_equals(9,int(length))
        for i in range(0,length):
            select.select_by_index(i)
            driver.find_element_by_id("GoCollege").click()
            divElement = driver.find_element_by_css_selector("h3").text
            # check if it navigates to correct page
            assert_equals(divElement,driver.find_element_by_css_selector('.easy-breadcrumb_segment-title').text)
            print "verified "+str(i)+""+divElement
            driver.back()
            element1 = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "location-dropdown")))
            select = Select(driver.find_element_by_id("location-dropdown"))
        driver.close()

    def keywordsearch(self,url):
        self.access_url(url)
        # check if the keyword label is correct
        keywordlabel = driver.find_element_by_xpath("(//label[@for='keywordEntry'])[1]").text
        assert_equals(str(keywordlabel), "What do you want to study?")
        #positive test
        driver.find_element_by_css_selector(".keywordEntry").send_keys("computer")
        driver.find_element_by_id("GoCollege").click()
        length=driver.find_elements_by_xpath("//span[@class='majorDescriptionLink']")
        assert_true(len(length)>0)
        driver.back()
        #negative test
        element = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".keywordEntry")))
        driver.find_element_by_css_selector("input#keywordEntry.defaultText.keywordEntry").send_keys("qwert")
        driver.find_element_by_id("GoCollege").click()
        #div=driver.find_element_by_css_selector("div.pane-content > h2").text
        #assert_equals("This Search returned no results".str(div))
        driver.find_element_by_link_text('Undergraduate Degrees').click()
        driver.close()
    def additional_Options(self,url):
        self.access_url(url)
        additional=driver.find_element_by_xpath("(//div[@class='menuHeader'])[1]").text
        assert_equals(str(additional),"Additional Options")
        list=['ONLNE','accelerate','concurrent']
        names=['Online','Search Results: Accelerated Programs','Concurrent Degrees']
        length=driver.find_elements_by_xpath("//div[@class='form-type-checkbox form-item-submitted-checkboxes-Check1 form-item checkbox']")
        assert_equals(3,len(length))
        listlabels=['Online Programs','Accelerated Programs ','	Concurrent Programs']
        for i in range(1,len(length)):
            assert_equals(str(listlabels[i]),str(driver.find_elements_by_xpath("//div[@class='form-type-checkbox form-item-submitted-checkboxes-Check1 form-item checkbox'][%d]/label"%(i))))
        for i in range(0,3):
            driver.find_element_by_id(list[i]).click()
            driver.find_element_by_id(list[i]).send_keys(Keys.SPACE)
            driver.find_element_by_id("GoCollege").click()
            assert_equals(names[i],driver.find_element_by_css_selector('.easy-breadcrumb_segment-title').text)
            print("*******"+list[i]+"passed *********")
        driver.close()
    def advancedsearch_college(self,url):
        self.access_url(url)
        driver.find_element_by_id("advSearchLink").click()
        label=driver.find_element_by_xpath("//label[@for='mySchoolSelection']").text
        assert_equals("Interested in a specific college at ASU?",str(label))
        mySelect = Select(driver.find_element_by_id("mySchoolSelection"))
        length=len(mySelect.options)
        assert_equals(16,length)
        for i in range(0,length):
            mySelect.select_by_index(i)
            driver.find_element_by_id("GoCollege").click()
            element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".easy-breadcrumb_segment-title")))
            divElement = driver.find_element_by_css_selector("h3").text

            assert_equals(divElement,driver.find_element_by_css_selector('.easy-breadcrumb_segment-title').text)
            print "verified"+""+str(i)+divElement
            driver.back()
            element1 = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "advSearchLink")))
            driver.find_element_by_id("advSearchLink").click()
            mySelect = Select(driver.find_element_by_id("mySchoolSelection"))
            driver.find_element_by_css_selector('.form-select')
        driver.close()
    def radio_secondlanguage(self,url):
        self.access_url(url)
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "advSearchLink")))
        search = driver.find_element_by_id("advSearchLink")
        search.click()
        list=['required','notrequired','nopreference']
        for i in list:
            driver.find_element_by_id(i).click()
            driver.find_element_by_id(i).send_keys(Keys.SPACE)
            driver.find_element_by_id("GoCollege").click()
            element = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".easy-breadcrumb_segment-title")))
            divElement = driver.find_element_by_css_selector("h3").text

            assert_equals(divElement, driver.find_element_by_css_selector('.easy-breadcrumb_segment-title').text)
            print "verified" + "" + i + divElement
            element1 = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "advSearchLink")))
            driver.find_element_by_id("advSearchLink").click()
        driver.close()
    def checkalphabets(self):
        options=driver.find_elements_by_xpath("//a[@class='browseLetter']")
        length=len(options)
        for i in range(1,length):
            driver.find_element_by_xpath("(//a[@class='browseLetter'])[%d]"%(i)).click()
            noofelements=driver.find_elements_by_xpath("//td[@class='majorDescription']")
            assert_true(len(noofelements)>=1)
            print str(noofelements)

    def accesslinks(self,url):
        self.access_url(url)
        options=driver.find_elements_by_xpath("//img[@id='byInterest']")
        length=len(options)
        print length
        for i in range(1,3):

            driver.find_element_by_xpath("(//img[@id='byInterest'])[%d]"%(i)).click()
            element = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".easy-breadcrumb_segment-title")))
            divElement = driver.find_element_by_css_selector("h3").text

            assert_equals(divElement, driver.find_element_by_css_selector('.easy-breadcrumb_segment-title').text)
            #print "verified" + "" + divElement
            self.checkalphabets()
            driver.back()
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "byInterest")))
            print "element present"

        driver.close()

