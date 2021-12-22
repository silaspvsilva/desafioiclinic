from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://app.iclinic.com.br')

driver.find_element_by_xpath('//*[@id="email"]').send_keys('silas.admb@gmail.com')

driver.find_element_by_xpath('//*[@id="password"]').send_keys('Test2525')

driver.find_element_by_xpath('//*[@id="webapp-root"]/div[2]/div[1]/div/div/div[2]/form/button/span[1]').click()
time.sleep(5)
#agenda

driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul[1]/li[2]/a').click()
time.sleep(5)
#clic calendario

driver.find_element_by_xpath('/html/body/div[2]/div[5]/div[3]/div/div/div/div[2]/div[1]/div/div[1]/div[1]/div/span[1]').click()

#escolher dia

driver.find_element_by_xpath('/html/body/div[2]/div[5]/div[3]/div/div/div/div[2]/div[1]/div/div[1]/div[1]/div/div/div/div/div[1]/table/tbody/tr[4]/td[5]').click()

driver.find_element_by_xpath('/html/body/div[2]/div[5]/div[3]/div/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/ul[3]/li[5]/div').click()

#nome paciente
driver.find_element_by_xpath('/html/body/div[25]/div/div[2]/div/div/form/div[1]/div[2]/div[2]/div[2]/span/input[1]').send_keys('Silas Teste')
time.sleep(2)

#celular

driver.find_element_by_xpath('/html/body/div[25]/div/div[2]/div/div/form/div[1]/div[2]/div[3]/div[1]/input').send_keys('1988886666')
time.sleep(2)

#convenio

driver.find_element_by_xpath('/html/body/div[25]/div/div[2]/div/div/form/div[1]/div[2]/div[5]/div/button/span/span').click()
time.sleep(2)

driver.find_element_by_xpath('//*[@id="bs-select-2-1"]/span').click()
time.sleep(2)

driver.find_element_by_xpath('/html/body/div[25]/div/div[2]/div/div/form/div[2]/button[2]/span/span').click()


