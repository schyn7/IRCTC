from selenium import webdriver
import time

chromedriver = r'''C:\Users\SACHIN\Desktop\chromedriver'''

driver = webdriver.Chrome(chromedriver)

driver.get('https://www.irctc.co.in/nget/train-search')

def sign_in( username, password):

    login = driver.find_element_by_id('loginText')
    login.click()

    time.sleep(1)

    user = driver.find_element_by_id('userId')
    user.clear()

    user.send_keys(username)

    time.sleep(1)

    signi = driver.find_element_by_id('pwd')
    signi.clear()

    signi.send_keys(password)

    time.sleep(10)

    button = driver.find_element_by_xpath('//*[@id="login_header_disable"]/div/div[2]/div[2]/div/div[2]/div[3]/div[2]/form/button')
    button.click()

    time.sleep(2)

    form = driver.find_element_by_xpath('//*[@id="origin"]/span/input')
    form.clear()
    form.send_keys('NEW DELHI - NDLS')


    formo = driver.find_element_by_xpath('//*[@id="destination"]/span/input')
    formo.clear()
    formo.send_keys('PUNE JN - PUNE')

    time.sleep(1)

    date = driver.find_element_by_xpath('//*[@id="divMain"]/div/app-main-page/div[2]/div/div[1]/div/div/div[1]/div/app-jp-input/div[3]/form/div[3]/p-calendar/span')
    date.click()

    time.sleep(1)
    dat = driver.find_element_by_xpath('//*[@id="divMain"]/div/app-main-page/div[2]/div/div[1]/div/div/div[1]/div/app-jp-input/div[3]/form/div[3]/p-calendar/span/div/table/tbody/tr[5]/td[1]')
    dat.click()

    time.sleep(1)

    clas = driver.find_element_by_xpath('//*[@id="journeyClass"]/div/div[3]/span')
    clas.click()
    sleeper = driver.find_element_by_xpath('//*[@id="journeyClass"]/div/div[4]/div/ul/li[10]')
    sleeper.click()

    time.sleep(2)


    submo = driver.find_element_by_xpath('//*[@id="divMain"]/div/app-main-page/div[2]/div/div[1]/div/div/div[1]/div/app-jp-input/div[3]/form/div[7]')
    submo.click()


    time.sleep(2)

    availability = driver.find_element_by_xpath('//*[@id="divMain"]/div/app-train-list/div/div[5]/div/div[2]/div[1]/div[2]/div[4]/div[1]/div[1]/app-train-avl-enq/div[2]/div[1]/div[3]/div[2]/div/div')
    availability.click()


    butto = driver.find_element_by_xpath('//*[@id="divMain"]/div/app-train-list/div/div[5]/div/div[2]/div[1]/div[2]/div[4]/div[1]/div[1]/app-train-avl-enq/div[2]/div[1]/div[3]/div[2]/div')

    butto.click()
    time.sleep(1)
    book = driver.find_element_by_xpath('//*[@id="ui-panel-0-content"]/div/div/div/table/tbody/tr/td/div/div[3]/button')
    book.click()
    time.sleep(1)
    root = driver.find_element_by_xpath('//*[@id="divMain"]/div/app-train-list/div/p-confirmdialog[2]/div/div[3]/p-footer/div/button[2]')
    root.click()

    time.sleep(2)

    name = driver.find_element_by_xpath('//*[@id="psgn-name"]')
    name.send_keys('sachin kamble')
    time.sleep(1)
    age = driver.find_element_by_xpath('//*[@id="divMain"]/div/app-passenger-input/div[5]/form/div/div[1]/div[3]/div[1]/div/div[2]/app-passenger/div/div[1]/div[2]/input')
    age.click()
    time.sleep(1)
    gender = driver.find_element_by_xpath('//*[@id="divMain"]/div/app-passenger-input/div[5]/form/div/div[1]/div[3]/div[1]/div/div[2]/app-passenger/div/div[1]/div[3]/select')
    gender.click()
    time.sleep(1)
    insu= driver.find_element_by_xpath('//*[@id="divMain"]/div/app-passenger-input/div[5]/form/div/div[1]/div[3]/div[6]/div[3]/span[2]/label')
    insu.click()
    time.sleep(1)
    mobile = driver.find_element_by_xpath('//*[@id="mobileNumber"]')
    mobile.clear()
    mobile.send_keys('9975901233')
    time.sleep(1)
    boo = driver.find_element_by_xpath('//*[@id="divMain"]/div/app-passenger-input/div[5]/form/div/div[1]/div[5]/div/button[2]')
    boo.click()
    time.sleep(1)








sign_in('userid','password')











