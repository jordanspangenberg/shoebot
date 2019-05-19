import requests
import json
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import datetime
import time

def getCatalog():
    base_url = 'https://feature.com/products/'

    i = 1
    productCatalog = []

    while True:
        getUrl = ('https://feature.com/collections/footwear/products.json?page={}').format(i)
        r = requests.get(getUrl)
        products = json.loads(r.text)["products"]

        if products:
            for product in products:
                print(product['title'])
                productName = product['title']
            i = i + 1
            productCatalog.append(products)
        else:
            now = datetime.datetime.now()
            with open('{}-feature.json'.format(now.strftime('%m-%d-%y-%H-%M-%S')), 'w') as outfile:
                json.dump(productCatalog, outfile)
            return productCatalog

def checkAvailability(fileName, searchTerm):
    base_url = 'https://feature.com/products/'
    with open(fileName) as infile:

        productCatalog = json.load(infile)
        for page in productCatalog:
            for product in page:
                productName = product['title']
                print(productName)
                if productName == searchTerm:
                    theShoe = product
                    productHandle = product['handle']
                    productUrl = base_url + productHandle
                    return productUrl
                
        return False

def availabilityCheck(productName):
    pass


def buyProduct(url, size):
    driver = webdriver.Chrome(executable_path =r'C:\Users\Jordan\shoebot\chromedriver.exe')

    driver.implicitly_wait(3)
    driver.get(str(url))

    driver.find_element_by_xpath('//div[@data-value="{}"]'.format(size)).click()
    driver.find_element_by_xpath('//button[@class="AddToCart default-btn"]').click()
    driver.find_element_by_xpath('//button[@class="btn--secondary btn--full cart__checkout"]').click()

    time.sleep(1)
    driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys('jordan.spang@gmail.com')

    time.sleep(1)
    driver.find_element_by_xpath('//input[@placeholder="First name"]').send_keys('Jordan')

    time.sleep(1)
    driver.find_element_by_xpath('//input[@placeholder="Last name"]').send_keys('Spangenberg')

    time.sleep(1)
    driver.find_element_by_xpath('//input[@id="checkout_shipping_address_address1"]').send_keys('1045 W Nelson Ln')

    time.sleep(1)
    driver.find_element_by_xpath('//input[@placeholder="City"]').send_keys('Hermiston')

    time.sleep(1)
    select = Select(driver.find_element_by_id('checkout_shipping_address_province'))
    select.select_by_visible_text('Oregon')

    time.sleep(1)
    driver.find_element_by_xpath('//input[@class="field__input field__input--zip"]').send_keys('97838')

    time.sleep(1)
    driver.find_element_by_xpath('//input[@id="checkout_shipping_address_phone"]').send_keys('5417202859' + u'\ue007')

if __name__ == '__main__':
    #productCatalog = getCatalog()
    print(checkAvailability(
        fileName="C:/Users/Jordan/shoebot/04-22-19-18-13-08-feature.json", 
        searchTerm="Adidas Originals x White Mountaineering Superstar - Core Black/Grey" ))
""" 
    myUrl = availabilityCheck()
    if myUrl != False:
        buyProduct()
    else:
        print("Product is not available")
 """