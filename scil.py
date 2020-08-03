from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options as ChromeOptions
from time import sleep

import sys

date = '7/28/20'
SCIL_URL_TOD = 'https://www.scottcountyiowa.us/sheriff/temp-inmates.php?comdate=today'
SCIL_URL = 'https://www.scottcountyiowa.us/sheriff/temp-inmates.php?comdate='
TR_XPATH = '/html/body/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/table/tbody/tr'

def ret_inmates(driver):
    #table_rows = driver.find_elements_by_class_name("inmate")
    inmates = set()
    table_rows = driver.find_elements_by_xpath(TR_XPATH)
    print('[Found: ' + str(len(table_rows)) + ' inmates for ' + date + ']')
    for row in table_rows:
        inmates.add(row.find_element_by_class_name('inmate').text)
    return inmates

def main():
    print("[Loading " + SCIL_URL + date +  "]")

    chr_options = ChromeOptions()
    chr_options.add_argument('--headless')
    chr_options.add_argument('window-size=1400,1000')
    driver = webdriver.Chrome(options=chr_options)
    driver.get(SCIL_URL+date)

    sleep(1)
    assert "Scott County, Iowa" in driver.title

    print('[Finding inmates]')
    inmates = ret_inmates(driver)
    print('--------------------------------------------------------------------------')
    for inmate in inmates:
        print('[' + inmate + ']')
    driver.close()


if __name__ == main():
    main()
