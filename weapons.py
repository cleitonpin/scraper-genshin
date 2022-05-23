from webdriver import start_driver
from selenium.webdriver.common.by import By
import json

driver = start_driver()

driver.get('https://genshin.gg/weapons')

body = driver.find_element(By.CLASS_NAME, 'rt-tbody')

rows = body.find_elements(By.CLASS_NAME, 'rt-tr')

weapons = []

value = 0
for r in range(1, len(rows) + 1):
  value += 1
  name = driver.find_element(By.XPATH, f'//*[@id="root"]/div/section/div[4]/main/div[5]/div/div[1]/div[2]/div[{r}]/div/div[1]')
  print(f'{value}/{len(rows)} - {name.text}')
  icon = driver.find_element(By.XPATH, f'//*[@id="root"]/div/section/div[4]/main/div[5]/div/div[1]/div[2]/div[{r}]/div/div[1]//*[@class="table-image"]')
  type = driver.find_element(By.XPATH, f'//*[@id="root"]/div/section/div[4]/main/div[5]/div/div[1]/div[2]/div[{r}]/div/div[2]')
  atk = driver.find_element(By.XPATH, f'//*[@id="root"]/div/section/div[4]/main/div[5]/div/div[1]/div[2]/div[{r}]/div/div[4]')
  secondary = driver.find_element(By.XPATH, f'//*[@id="root"]/div/section/div[4]/main/div[5]/div/div[1]/div[2]/div[{r}]/div/div[5]')
  passive = driver.find_element(By.XPATH, f'//*[@id="root"]/div/section/div[4]/main/div[5]/div/div[1]/div[2]/div[{r}]/div/div[6]')
  bonus = driver.find_element(By.XPATH, f'//*[@id="root"]/div/section/div[4]/main/div[5]/div/div[1]/div[2]/div[{r}]/div/div[7]')
  location = driver.find_element(By.XPATH, f'//*[@id="root"]/div/section/div[4]/main/div[5]/div/div[1]/div[2]/div[{r}]/div/div[8]')
  stars = driver.find_elements(By.XPATH, f'//*[@id="root"]/div/section/div[4]/main/div[5]/div/div[1]/div[2]/div[{r}]/div/div[3]//*[@class="rarity"]')

  weapons.append({
    "name": name.text,
    "icon": icon.get_attribute('src'),
    "type": type.text,
    "rarity": len(stars),
    "atk": atk.text,
    "secondary": secondary.text,
    "passive": passive.text,
    "bonus": bonus.text,
    "location": location.text
  })

with open('weapons.json', 'w') as outfile:
  json.dump(weapons, outfile, indent=2)
