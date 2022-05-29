from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import json
import re
from constants import Constants
from webdriver import start_driver

driver = start_driver()

def get_skills_and_talents(title: str, list_to_json: list) -> None:

  list_name = {
    "character": "character-skills-list",
    "passives": "passives-list",
    "constellations": "constellations-list"
  }

  list_item = {
    "character": "character-skills-item",
    "passives": "passives-list-item",
    "constellations": "constellations-list-item"
  }

  # class_name_list = "character-skills-list" if title == "character" else "passives-list"
  # class_name_item = "character-skills-item" if title == "character" else "passives-list-item"

  list = driver.find_element(By.CLASS_NAME, list_name[title])
  items = list.find_elements(By.CLASS_NAME, list_item[title])


  for i in range(0, len(items)):
    class_sufix = {
      "character": "skills",
      "passives": "passives",
      "constellations": "constellations",
    }

    description = items[i].find_element(By.CLASS_NAME, f"{class_sufix[title]}-description")

    if (title == "constellations"):
      icon = items[i].find_element(By.CLASS_NAME, "constellations-icon").get_attribute("src")
      header = items[i].find_element(By.CLASS_NAME, f"constellations-meta")
      name = header.find_element(By.CLASS_NAME, f"{class_sufix[title]}-name")
      unlock = header.find_element(By.CLASS_NAME, f"{class_sufix[title]}-unlock")
    else:
      meta = items[i].find_element(By.CLASS_NAME, f"{class_sufix[title]}-meta")
      icon = meta.find_element(By.CLASS_NAME, f"{class_sufix[title]}-icon").get_attribute("src")
      header = meta.find_element(By.CLASS_NAME, f"{class_sufix[title]}-header")
      name = header.find_element(By.CLASS_NAME, f"{class_sufix[title]}-name")
      unlock = header.find_element(By.CLASS_NAME, f"{class_sufix[title]}-unlock")

    list_to_json.append({
      "name": name.text,
      "unlock": unlock.text,
      "description": description.text,
      "icon": icon
    })

character = { "characters": [] }

driver.get('https://genshin.gg')

all_characters_names = driver.find_elements(By.CLASS_NAME, "character-name")
list_of_all_characters = []

for i in range(0, len(all_characters_names)):
  list_of_all_characters.append(all_characters_names[i].text)

value = 0

for i in range(len(all_characters_names)):
  value += 1
  print(f"{value}/{len(list_of_all_characters)} - {list_of_all_characters[i].replace(' ', '')}")

  driver.get(f"https://genshin.gg/characters/{list_of_all_characters[i].replace(' ', '')}")

  icon = driver.find_element(By.CLASS_NAME, "character-icon").get_attribute("src")
  name = driver.find_element(By.CLASS_NAME, "character-name")
  rarityElement = driver.find_element(By.CLASS_NAME, "character-rarity")
  stars = len(rarityElement.find_elements(By.CLASS_NAME, "rarity"))
  details = driver.find_elements(By.CLASS_NAME, "character-details-item")

  url_icon = re.split('https://rerollcdn.com', icon)

  skillTalents =  []
  get_skills_and_talents("character", skillTalents)
  passiveTalents = []
  get_skills_and_talents("passives", passiveTalents)
  constellations = []
  get_skills_and_talents("constellations", constellations)
  upgrades = []

  


  
  character["characters"].append({
    'id': list_of_all_characters[i].lower(),
    'name': list_of_all_characters[i],
    'description': list_of_all_characters[i],
    'vision': details[0].text,
    'weapon': details[1].text,
    'rarity': stars,
    'icon': url_icon[1],
    'skillTalents': skillTalents,
    'passiveTalents': passiveTalents,
    'constellations': constellations,
    'upgrades': upgrades
  })

driver.close()

with open('./json/character.json', 'w') as outfile:
  json.dump(character, outfile, indent=2)

class Character:
  def __init__(self, character):
    self.character = character

  def get_ascension_upgrades(self):
    tableBody = driver.find_element(By.CLASS_NAME, Constants.TABLE)
    rows = tableBody.find_elements(By.CLASS_NAME, Constants.ROWS)

    for x in range(1, len(rows) + 1):

        rank = driver.find_element(By.XPATH, Constants.get_div_table_rank(x, 1))
        level = driver.find_element(By.XPATH, f'//*[@id="ascension"]/div/div/div[1]/div[2]/div[{x}]/div/div[2]')
        cost = driver.find_element(By.XPATH, f'//*[@id="ascension"]/div/div/div[1]/div[2]/div[{x}]/div/div[3]')
        name = driver.find_element(By.XPATH, f'//*[@id="ascension"]/div/div/div[1]/div[2]/div[{x}]/div/div[4]')
        icon = driver.find_element(By.XPATH, f'//*[@id="ascension"]/div/div/div[1]/div[2]/div[{x}]/div/div[4]{Constants.IMAGE_WRAPPER}')
        name5 = driver.find_element(By.XPATH, f'//*[@id="ascension"]/div/div/div[1]/div[2]/div[{x}]/div/div[5]')

        for j in range(2, len(rows) + 1):
          icon5 = driver.find_element(By.XPATH, f'//*[@id="ascension"]/div/div/div[1]/div[2]/div[{j}]/div/div[5]{Constants.IMAGE_WRAPPER}')

        name2 = driver.find_element(By.XPATH, f'//*[@id="ascension"]/div/div/div[1]/div[2]/div[{x}]/div/div[6]')
        icon2 = driver.find_element(By.XPATH, f'//*[@id="ascension"]/div/div/div[1]/div[2]/div[{x}]/div/div[6]{Constants.IMAGE_WRAPPER}')
        name3 = driver.find_element(By.XPATH, f'//*[@id="ascension"]/div/div/div[1]/div[2]/div[{x}]/div/div[7]')
        icon3 = driver.find_element(By.XPATH, f'//*[@id="ascension"]/div/div/div[1]/div[2]/div[{x}]/div/div[7]{Constants.IMAGE_WRAPPER}')

        upgrades.append({
          'rank': rank.text,
          'level': level.text,
          'cost': cost.text,
          'material_one': {
            'name': name.text,
            'icon': icon.get_attribute("src")
          },
          'material_two': {
            'name': name5.text,
            'icon': icon5.get_attribute("src")
          },
          'material_three': {
            'name': name2.text,
            'icon': icon2.get_attribute("src")
          },
          'material_four': {
            'name': name3.text,
            'icon': icon3.get_attribute("src")
          },
        })
    return self.character['upgrades']