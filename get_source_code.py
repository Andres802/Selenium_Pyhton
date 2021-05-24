# import modules
import unittest
import codecs
import os

# import webdriver
from selenium import webdriver

 
# create webdriver object
driver = webdriver.Chrome(executable_path = "./chromedriver")
driver.implicitly_wait(0.5)
#maximisize browser
#driver.maximize_window()

# launch URL
driver.get("https://www.montacargasrentaldelvalle.com")

# get the file path to save the page
n=os.path.join("/Users/Andres/Documents/Selenium","source-code.html")

# open file in write mode with encoding
f = codecs.open( n, "w", "utf-8")

# obtain page source
h = driver.page_source 

# write the source code content
f.write(h)

# get page_source
driver.quit()




# if __name__ == "__main__":
# 	unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'source-code-report'))