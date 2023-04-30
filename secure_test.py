# https://github.com/ultrafunkamsterdam/undetected-chromedriver
# pip install undetected-chromedriver 
import undetected_chromedriver as uc 
 
# Initializing driver 
driver = uc.Chrome() 
 
# Try accessing a website with antibot service 
driver.get("https://nowsecure.nl")