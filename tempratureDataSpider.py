from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys 
import selenium.webdriver.support.ui as ui
from pythonosc.udp_client import SimpleUDPClient
import time

# udp ->processing/maxmsp

ip = "192.168.1.83"  # change the ip here
port = 6667  # define the udp port


client = SimpleUDPClient(ip, port)

driverLocation = '/usr/local/bin/chromedriver' 
driver = webdriver.Chrome(executable_path=driverLocation) 

driver.get("https://www.ventusky.com/los-angeles") # define the site that you will get data

#driver.implicitly_wait(10)

wait = ui.WebDriverWait(driver,10) # wait for load of page content
wait.until(lambda driver: driver.find_element_by_xpath("//div[@class='ji']"))

temperature = driver.find_element_by_class_name("temperature").text
tempandwind = driver.find_element_by_class_name("info_table").text

print(tempandwind.split("\n"))

climateData = []

def sendUdpData(message):
    currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    client.send_message(f"/python/TemperatureOfLosAngeles{currentTime}", message)
    return (f"sendComplete:{message}")

while True:
    sleeptime = 3; # waiting time
    time.sleep(sleeptime);
    tempandwind = driver.find_element_by_class_name("info_table").text
    result = (tempandwind.split("\n"))
    currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    list = {
        "city" : "Los Angeles",
        "temperature" : result[0],
        "wind" : result[1],
        "time" : currentTime
    }

    climateData.append(list)
    print(climateData)

    # temperature data, send to max
    temperature = driver.find_element_by_class_name("temperature").text
    temText = temperature.split(" ")
    tempResult = temText[0]
    # sending udp
    print(sendUdpData(tempResult))
#driver.close()



