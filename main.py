from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Get the webdriver. We'll use Chrome for this example.
driver = webdriver.Chrome()

#You can navigate to the CGC webpage. You can skip this step, but it's here to show you can navigate between pages.
driver.get("https://www.cgc.edu/")

#Let's see what CGC is about.
driver.get("https://www.cgc.edu/about-us")

#We need to wait for the webpage to load, so we use this line of code to do so. 
WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CLASS_NAME, "text-center.lead")))

#Let's get the text from the page. We're going to use the HTML class to get that info.
#Any time you see a space in the class name, replace it with a period.
#In this case, 'text-center lead' from the webpage would become 'text-center.lead' in the code.
cgcText = driver.find_element(By.CLASS_NAME, "text-center.lead").text
print(cgcText)

#Write the about info to a .txt file.
with open('cgc-about.txt', 'a') as f: f.write(cgcText)

#Make sure to clean up and close your webdriver at the end.
driver.close()