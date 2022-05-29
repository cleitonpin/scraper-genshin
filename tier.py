from webdriver import start_driver
from selenium.webdriver.common.by import By
import json

driver = start_driver()

driver.get('https://genshin.gg/tier-list')

tier = driver.find_elements(By.CLASS_NAME, "tier")

tiers = {}

for i in range(0, len(tier)):
  tier_title = tier[i].find_element(By.CLASS_NAME, "tier-title").text

  tiers[tier_title] = []

  tier_list = tier[i].find_elements(By.CLASS_NAME, "tier-list")

  for j in range(0, len(tier_list)):
    character_portraits = tier_list[j].find_elements(By.CLASS_NAME, "character-portrait")
    
    for k in range(0, len(character_portraits)):
      name = character_portraits[k].find_element(By.CLASS_NAME, "character-name").text
      designation = character_portraits[k].find_element(By.CLASS_NAME, "character-role").text
      vision = character_portraits[k].find_element(By.CLASS_NAME, "character-type").get_attribute("alt")

      constellation = character_portraits[k].find_element(By.CLASS_NAME, "character-constellation").text

      tiers[tier_title].append({
        "name": name,
        "designation": designation,
        "constellation": constellation,
        "vision": vision
      })

print(tiers)
