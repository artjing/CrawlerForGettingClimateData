# CrawlerForGettingClimateData


## Python

### How to make a simple data spider 
### 

#### Setup
 
Selenium is a automatically test tool for web. It can run inside the browser and interact with the elements of the page. Almost like a how a user use webpage, selenium could get userful data and storage data in whole process.

#####  Install selenium
```
$ pip3 install selenium
```

#####  Download chrome driver


1, Checking the version of your chrome browser
![d7e5346263ffa166fd0f3c0b89a57ef7.png](evernotecid://4920FC1F-2801-487E-B865-128CE5E4C0D9/appyinxiangcom/2071823/ENResource/p2943)

Then download the same version from following site: 
[http://chromedriver.chromium.org/downloads](http://chromedriver.chromium.org/downloads)
![3c198b4b022ee728a8c1e5fa82c6efa9.png](evernotecid://4920FC1F-2801-487E-B865-128CE5E4C0D9/appyinxiangcom/2071823/ENResource/p2944)

2, Copy the chrome driver file you downlod to folder: **/usr/local/bin**

##### Test if the selenirm and webdriver works

```
$ ipython

$ In [1]: from selenium import webdriver

$ In [2]: browser = webdriver.Chrome()
```