'''
Created on Mar 27, 2016

@author: Jake Shulman
'''
from bs4 import BeautifulSoup
from urllib2  import urlopen
from lxml import html
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import os

BASE_URL = "http://allrecipes.com/recipe/10331/moms-chocolate-chip-cookies"
SEARCH= "http://allrecipes.com/search/results/?wt=chocolate%20chip%20cookies&sort=re"
British="http://allrecipes.co.uk/recipe/4807/best-big--fat--chewy-chocolate-chip-cookies.aspx?o_is=Hub_TopRecipe_1"

def make_soup(url):
    html= urlopen(url).read()
    return BeautifulSoup(html,"lxml")

def getReviews(url):
    soup = make_soup(url)
    return soup.find("meta",{"itemprop":"reviewCount"})['content']
def getRating(url):
    soup = make_soup(url)
    try:
        a= soup.find("meta",{"property":"og:rating"})['content']
    except TypeError:
        a= "0"
        pass
    return a
def getIngredients(url):
    #make browser copy to change values before scraping

    #to Use chrome instead of firefox
    #Currently action keys do not work, so can scrape ingredients
    
#     chromedriver = "/Users/Jake/Downloads/cDriver"
#     os.environ["webdriver.chrome.driver"] = chromedriver
#     driver=webdriver.Chrome(chromedriver)


    driver=webdriver.Firefox()
    driver.set_window_size(800, 1000)
    chain=ActionChains(driver)
    driver.get(url)
    

    #TODO get time and temp
    


    # click the little pie button so elements aren't hidden
    #find and change serving size to 48
    driver.execute_script("window.scrollTo(0, 100)")
    driver.find_element_by_class_name("onoffswitch-switch").click()
    driver.find_element_by_xpath('//*[@id="servings-button"]/span[2]').click()
    driver.find_element_by_css_selector('input[type=\"number\"]').clear()
    driver.find_element_by_css_selector('input[type=\"number\"]').send_keys('48')
      
    # change to metric system
    metric=driver.find_element_by_class_name("measurement-title")
    chain.move_to_element_with_offset(metric,85,-30).click_and_hold().release().perform()
    #click adjust button to put through changes
    driver.find_element_by_id('btn-adjust').click()
    driver.find_element_by_xpath('//*[@id="servings-button"]/span[2]').click()
    #get source from changed web page and copy them to scrape
    body=driver.find_element_by_css_selector("body")
    body.send_keys(Keys.COMMAND,"a")
    body.send_keys(Keys.COMMAND,"c")
    outf= os.popen('pbpaste','r')
    content = outf.read()
    outf.close()
    content = content[content.find('near you')+9:content.find("Directions")]
    content=content.split('\n')
    ingred=[]
    for x in content:
        if x!='':
            ingred.append(x.strip())                                     
    ingred=ingred[0:-1]
    driver.quit()
    return ingred

if __name__ == '__main__':
#     i=getIngredients(BASE_URL)
#     print type(i)
#     print len(i)
    print getReviews(BASE_URL)
    print getRating(BASE_URL)
    print getIngredients(BASE_URL)
    print "done"
#url:[[ing1,ing2,ing3],4.5031,935]
#{cookie:[{ing:amt},4.5,935]}