from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import json
import re


list_of_all_characters = [  
  'Albedo', 
  'Aloy', 
  'Amber', 
  'Itto', 
  'Barbara', 
  'Beidou', 
  'Bennett', 
  'Chongyun', 
  'Diluc', 
  'Diona', 
  'Eula', 
  'Fischl', 
  'Ganyu', 
  'Gorou', 
  'HuTao', 
  'Jean', 
  'Kazuha', 
  'Kaeya', 
  'Ayaka', 
  'Ayato', 
  'Keqing', 
  'Klee', 
  'Sara', 
  'Lisa', 
  'Mona', 
  'Ningguang', 
  'Noelle', 
  'Qiqi', 
  'Raiden', 
  'Razor', 
  'Rosaria', 
  'Kokomi', 
  'Sayu', 
  'Shenhe', 
  'Sucrose', 
  'Childe', 
  'Thoma', 
  'Venti', 
  'Xiangling', 
  'Xiao', 
  'Xingqiu', 
  'Xinyan', 
  'YaeMiko', 
  'Yanfei', 
  'Yoimiya', 
  'YunJin', 
  # 'Traveler(Anemo)', 
  # 'Traveler(Geo)', 
  # 'Traveler(Electro)', 
]
def get_skills_and_talents(title: str, list_to_json: list, key: str) -> None:

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

value = 0
for i in range(len(list_of_all_characters)):
  value += 1
  print(f"{value}/{len(list_of_all_characters)}")
  options = Options()
  # options.add_argument('--ignore-certificate-errors-skip-list')
  options.add_argument("--disable-web-security")
  options.add_argument("--disable-site-isolation-trials")
  options.add_argument('--headless')
  options.add_argument('--log-level=1')
  # options.add_argument('--disable-gpu')

  driver = webdriver.Chrome(options=options)
  driver.get(f"https://genshin.gg/characters/{list_of_all_characters[i]}")

  icon = driver.find_element(By.CLASS_NAME, "character-icon").get_attribute("src")
  name = driver.find_element(By.CLASS_NAME, "character-name")
  rarityElement = driver.find_element(By.CLASS_NAME, "character-rarity")
  stars = len(rarityElement.find_elements(By.CLASS_NAME, "rarity"))
  vision = driver.find_elements(By.CLASS_NAME, "character-details-item")

  url_icon = re.split('https://rerollcdn.com', icon)

  skillTalents =  []
  get_skills_and_talents("character", skillTalents, "skillTalents")
  passiveTalents = []
  get_skills_and_talents("passives",passiveTalents, "passiveTalents")
  constellations = []
  get_skills_and_talents("constellations", constellations, "constellations")

  character["characters"].append({
    'id': list_of_all_characters[i].lower(),
    'name': list_of_all_characters[i],
    'description': list_of_all_characters[i],
    'vision': vision[0].text,
    'weapon': vision[1].text,
    'rarity': stars,
    'icon': url_icon[1],
    'skillTalents': skillTalents,
    'passiveTalents': passiveTalents,
    'constellations': constellations
  })

  driver.close()

with open('character.json', 'w') as outfile:
  json.dump(character, outfile, indent=2)

json_data = json.dumps(character)
print(json_data)
