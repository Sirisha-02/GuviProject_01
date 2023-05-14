from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import ElementClickInterceptedException
import time
driver=webdriver.Chrome("C:\\Users\\Rakesh Varma\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(20)
## TestID:TC_Login_01(Login to site)----------
driver.find_element(By.XPATH,'//input[@name="username"]').send_keys("Admin")
driver.find_element(By.XPATH,'//input[@name="password"]').send_keys("admin123")
driver.find_element(By.XPATH,'//button[@type="submit"]').click()
driver.implicitly_wait(15)
element=driver.find_element(By.XPATH,'//ul[@class="oxd-main-menu"]/li[2]/a')
driver.execute_script("arguments[0].click()",element)
print("Successufully logged")
time.sleep(5)
##TC_PIM_01(Adding of employee details)---------------
driver.find_element(By.XPATH,'(//button[@type="button"])[4]').click()
time.sleep(5)
driver.find_element(By.NAME,'firstName').send_keys("Sirisha")
driver.find_element(By.NAME,'middleName').send_keys("Sri")
driver.find_element(By.NAME,'lastName').send_keys("Puvvala")
time.sleep(5)
driver.find_element(By.XPATH,'//button[@type="submit"]').click()
time.sleep(10)
driver.find_element(By.XPATH,'(//i[@class="oxd-icon bi-caret-down-fill oxd-select-text--arrow"])[1]').click()
time.sleep(5)
driver.find_element(By.XPATH,'//div[@role="option"]/span[text()="Indian"]').click()
time.sleep(5)
driver.find_element(By.XPATH,'(//i[@class="oxd-icon bi-caret-down-fill oxd-select-text--arrow"])[2]').click()
time.sleep(5)
driver.find_element(By.XPATH,'//span[text()="Single"]').click()
time.sleep(3)
try:
    driver.find_element(By.XPATH,'(//i[@class="oxd-icon bi-calendar oxd-date-input-icon"])[2]').send_keys("2000-08-02")
except ElementNotInteractableException as ec:
    pass
time.sleep(5)
click=driver.find_element(By.XPATH,'//label[text()="Female"]')
driver.execute_script("arguments[0].click()",click)
time.sleep(5)
ele=driver.find_element(By.XPATH,'(//button[@type="submit"])[1]')
driver.execute_script("arguments[0].click()",ele)
print("successfully added and saved the employee details")
### TestID:TC_PIM_02(Updating of existing employee details)----------
driver.find_element(By.XPATH,'//a[text()="Employee List"]').click()
time.sleep(10)
driver.find_element(By.XPATH,'//i[@class="oxd-icon bi-pencil-fill"]').click()
time.sleep(10)
driver.find_element(By.NAME,'firstName').send_keys(Keys.CONTROL+"a")
driver.find_element(By.NAME,'firstName').send_keys(Keys.DELETE)
time.sleep(3)
driver.find_element(By.NAME,'firstName').send_keys("Teja")
time.sleep(3)
driver.find_element(By.NAME,'middleName').send_keys(Keys.CONTROL+"a")
driver.find_element(By.NAME,'middleName').send_keys(Keys.DELETE)
time.sleep(3)
driver.find_element(By.NAME,'middleName').send_keys("Swi")
time.sleep(3)
driver.find_element(By.NAME,'lastName').send_keys(Keys.CONTROL+"a")
driver.find_element(By.NAME,'lastName').send_keys(Keys.DELETE)
time.sleep(3)
driver.find_element(By.NAME,'lastName').send_keys("P")
driver.execute_script("window.scrollBy(0,500)")
driver.implicitly_wait(20)
driver.find_element(By.XPATH,'(//i[@class="oxd-icon bi-caret-down-fill oxd-select-text--arrow"])[1]').click()
time.sleep(5)
driver.find_element(By.XPATH,'//div[@role="option"]/span[text()="Afghan"]').click()
driver.find_element(By.XPATH,'(//i[@class="oxd-icon bi-caret-down-fill oxd-select-text--arrow"])[2]').click()
time.sleep(10)
try:
    driver.find_element(By.XPATH,'//div[@class="oxd-select-text-input"][text()="Single"]').click()
except NoSuchElementException as ec:
    pass
time.sleep(5)
try:
    driver.find_element(By.XPATH,'(//i[@class="oxd-icon bi-calendar oxd-date-input-icon"])[2]').send_keys("2000-08-02")
except ElementNotInteractableException as ec:
    pass
time.sleep(5)
try:
    driver.find_element(By.XPATH,'(//i[@class="oxd-icon bi-calendar oxd-date-input-icon"])[2]').send_keys("2000-12-13")
except ElementNotInteractableException as ec:
    pass
time.sleep(5)
click=driver.find_element(By.XPATH,'//label[text()="Female"]')
driver.execute_script("arguments[0].click()",click)
time.sleep(5)
ele=driver.find_element(By.XPATH,'(//button[@type="submit"])[1]')
driver.execute_script("arguments[0].click()",ele)
time.sleep(10)
print("successfully edited/updated the existing employee details")
# ### TestID:TC_PIM_03(Deleting of employee)----------
driver.back()
time.sleep(10)
driver.find_element(By.XPATH,'(//i[@class="oxd-icon bi-trash"])[1]').click()
time.sleep(10)
driver.find_element(By.XPATH,'//button[@class="oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin"]').click()
time.sleep(10)
print("Deleted the user")
#-----------logout------
element=driver.find_element(By.XPATH,'//ul[@class="oxd-main-menu"]/li[8]/a')
driver.execute_script("arguments[0].click()",element)
time.sleep(5)
driver.find_element(By.CLASS_NAME,'oxd-userdropdown-name').click()
driver.find_element(By.XPATH,'//ul[@class="oxd-dropdown-menu"]/li[4]/a').click()
print("logged out from the portal")
#### ## TestID:TC_Login_02(Invalid credentials)---------------------
driver.find_element(By.XPATH,'//input[@name="username"]').send_keys("Admin")
driver.find_element(By.XPATH,'//input[@name="password"]').send_keys("Invalid Password")
driver.find_element(By.XPATH,'//button[@type="submit"]').click()
print("Invalid Credentials")