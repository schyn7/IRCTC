from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
import pandas as pd

chromedriver = r'''C:\Users\SACHIN\Desktop\chromedriver'''

driver = webdriver.Chrome(chromedriver)

driver.get('https://ipindiaservices.gov.in/PublicSearch/PublicationSearch')


#p = driver.find_element_by_xpath('//*[@id="Index"]/a').text
#print(p)

granted = driver.find_element_by_xpath('//*[@id="Granted"]')
granted.click()

date_of_grant = driver.find_element_by_xpath('//*[@id="DateField"]/option[3]')
date_of_grant.click()

from_date = driver.find_element_by_xpath('//*[@id="FromDate"]')
from_date.send_keys('01/01/2000')

to_date = driver.find_element_by_xpath('//*[@id="ToDate"]')
to_date.send_keys('05/23/2020')

filling_office = driver.find_element_by_xpath('//*[@id="ItemField1"]/option[13]')
filling_office.click()

filling_office_name = driver.find_element_by_xpath('//*[@id="TextField1"]')
filling_office_name.send_keys('KOLKATA')

or_option = driver.find_element_by_xpath('//*[@id="LogicField1"]/option[2]')
or_option.click()

applicant_address = driver.find_element_by_xpath('//*[@id="ItemField2"]/option[9]')
applicant_address.click()

applicant_address_state = driver.find_element_by_xpath('//*[@id="TextField2"]')
applicant_address_state.send_keys('KOLKATA')

or_option2 = driver.find_element_by_xpath('//*[@id="LogicField2"]/option[2]')
or_option2.click()

inventors_address = driver.find_element_by_xpath('//*[@id="ItemField3"]/option[12]')
inventors_address.click()

inventors_address_state = driver.find_element_by_xpath('//*[@id="TextField3"]')
inventors_address_state.send_keys('KOLKATA')

time.sleep(9)

search = driver.find_element_by_xpath('//*[@id="home"]/div[18]/div[2]/div/div/div[1]/div[3]/input')
search.click()


patent = 1
j = 0
while(patent <2):
    j+=1
    try:
        w = '//*[@id="tableData"]/tbody/tr[' + str(j) + ']/td[1]/button'
        driver.find_element_by_xpath(w).click()
        for windowHandle in driver.window_handles:
            driver.switch_to.window(windowHandle)
            break

    except NoSuchElementException:  # spelling error making this code not work as expected
        driver.find_element_by_xpath('//*[@id="header"]/div[4]/div/div[1]/form/div/button[3]').click()
        j=0
    except NoSuchWindowException:
        pass
    except ElementClickInterceptedException:
        pass
    patent += 1

i=0
#time.sleep(5)
a=[]
for windowHandle in driver.window_handles:
    #print(windowHandle)

    driver.switch_to.window(windowHandle)
    try:
        elem = driver.find_element_by_xpath('//*[@id="home"]/table/tbody/tr[17]/td')
        if elem.text is not None:
            a.append(elem.text)
        else:
            a.append('None')
    except NoSuchElementException:  # spelling error making this code not work as expected
        pass
    except ElementClickInterceptedException:
        pass
    except NoSuchWindowException:
        pass

print(a)
print(len(a))