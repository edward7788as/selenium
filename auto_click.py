#########################################################################
#創立一個隨時可以控制的瀏覽器
# terminal先到 C:\Program Files\Google\Chrome\Application>
# 輸入
# .\chrome.exe --remote-debugging-port=9999 --user-data-dir="C:\gbf"

#dir 放資料位置 隨便你放
#########################################################################




from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9999")
chrome_driver = "C:/Users/guo/PycharmProjects/pythonProject/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)


while 1:
    try:
        WebDriverWait(driver, 1, 0.2).until(
            EC.presence_of_element_located((By.ID, 'buy_yes'))
        )

        driver.find_element_by_css_selector('.buynow').click()
        b = '//*[@id="checkoutBar"]/tbody/tr/td[4]'
        driver.find_element_by_xpath(b).click()

        a = '/html/body/form/div[3]/div[2]/h3/label[1]'
        driver.find_element_by_xpath(a).click()

        driver.find_element_by_id('cardNo_1').send_keys('1234')
        driver.find_element_by_id('cardNo_2').send_keys('5678')
        driver.find_element_by_id('cardNo_3_temp').send_keys('2222')
        driver.find_element_by_id('cardNo_4').send_keys('3333')
        driver.find_element_by_id('cardValidMonth').send_keys('10')
        driver.find_element_by_id('cardValidYear').send_keys('2028')
        driver.find_element_by_id('cardCVV').send_keys('112')
        driver.find_element_by_id('orderSave').click()

        a = '/html/body/div/div/div/form[1]/button'
        driver.find_element_by_xpath(a).click()
        break
    except:



        print("還未定位到元素! 刷新")
        driver.refresh()
