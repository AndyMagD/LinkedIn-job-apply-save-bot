from selenium import webdriver
from selenium.webdriver.common.by import By
import secret  # Hidden personal information used for loging in
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--start-maximized")

url_1 = "https://www.linkedin.com/jobs/search/?currentJobId=3801269709&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom"
url_2 = "https://www.linkedin.com/login"
driver = webdriver.Chrome(options)
driver.get(url_2)

time.sleep(2)

#logging in
input_username = driver.find_element(By.ID, value="username")
input_username.send_keys(secret.my_mail)
input_passw = driver.find_element(By.ID, value="password")
input_passw.send_keys(secret.my_passw)
agree_click = driver.find_element(By.CLASS_NAME, value="btn__primary--large")
agree_click.click()

time.sleep(1)
driver.get(url_1)

time.sleep(1)
job_cards = driver.find_elements(By.CLASS_NAME, "job-card-container")


for job in job_cards[:5]:
    job.click()
    time.sleep(2)

    try:
        save_button = driver.find_element(By.XPATH, "//button[contains(., 'Save')]")
        save_button.click()
    except Exception as e:
        print(f"Could not find the Save button for the job: {e}")



