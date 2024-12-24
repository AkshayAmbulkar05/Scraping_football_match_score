#All Football match Scroes scapper
import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd

# URL and path to ChromeDriver
web = 'https://www.adamchoi.co.uk/overs/detailed'
path = 'D:/this_is_output/Comparison/chromedriver-win64/chromedriver-win64/chromedriver.exe'

# Set up ChromeDriver service
service = Service(path)
driver = webdriver.Chrome(service=service)

# Open the website
driver.get(web)

# Click the "All matches" label
clicked = driver.find_element(By.XPATH, '//label[@analytics-event="All matches"]')
clicked.click()
time.sleep(10)  # Wait for the table to load (better to use WebDriverWait)

Country= Select(driver.find_element(By.ID,'country'))
select_country =input("which Country you want me to show the score:")
Country.select_by_visible_text(select_country)
sleep(5)
League = Select(driver.find_element(By.ID,'league'))
select_league = input("please select League:")
League.select_by_visible_text(select_league)
sleep(5)
Season = Select(driver.find_element(By.ID,'season'))
select_season = input('Please select season:')
Season.select_by_visible_text(select_season)

sleep(5)

# Extract data from the table
matches = driver.find_elements(By.TAG_NAME, 'tr')

# Lists to store extracted data
date = []
home_team = []
score = []
away_team = []

for match in matches:
    try:
        # Extract data from each row's cells using find_element (singular)
        date_text = match.find_element(By.XPATH, './td[1]').text
        home_text = match.find_element(By.XPATH, './td[2]').text
        score_text = match.find_element(By.XPATH, './td[3]').text
        away_text = match.find_element(By.XPATH, './td[4]').text

        # Append the text to the respective lists
        date.append(date_text)
        home_team.append(home_text)
        score.append(score_text)  # Keep score as a string
        away_team.append(away_text)

        # Print row data for debugging
        print(f"Date: {date_text}, Home Team: {home_text}, Score: {score_text}, Away Team: {away_text}")
    except Exception as e:
        # Handle rows that might not have the expected structure
        print(f"Error processing row: {e}")

# Close the driver
# driver.quit()

# Create a DataFrame and save it to CSV
df = pd.DataFrame({'date': date, 'home_team': home_team, 'score': score, 'away_team': away_team})
df.to_excel('football.xlsx', index=False)
print(df)


