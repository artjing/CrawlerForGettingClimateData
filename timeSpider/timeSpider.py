from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys 
import selenium.webdriver.support.ui as ui
from pythonosc.udp_client import SimpleUDPClient
import time

ip = "10.40.64.5"
port = 12000

client = SimpleUDPClient(ip, port)


driverLocation = '/usr/local/bin/chromedriver' 
driver = webdriver.Chrome(executable_path=driverLocation) 

driver.get("https://www.worldometers.info/world-population/")
 
print('success')

wait = ui.WebDriverWait(driver,10)
wait.until(lambda driver: driver.find_element_by_xpath("//div[@class='maincounter-number']"))
bornNum = driver.find_elements_by_xpath("//div[@class='sec-counter']")[0].text
deadNum =  driver.find_elements_by_xpath("//div[@class='sec-counter']")[1].text
print(bornNum,deadNum)

while True:
    sleeptime = 3;
    time.sleep(sleeptime);
    bornNum = driver.find_elements_by_xpath("//div[@class='sec-counter']")[0].text
    deadNum =  driver.find_elements_by_xpath("//div[@class='sec-counter']")[1].text

    list = []
    list.append(bornNum)
    list.append(deadNum)
    
    print("How much people born today:",bornNum,"=============","die today:",deadNum)
    client.send_message("/python/pupulationdata", list)
#driver.close()
