from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import json
import re
from constants import Constants
from webdriver import start_driver

class Character:
  def __init__(self, character, driver):
    self.character = character
    self.driver = driver

    self.get_ascension_upgrades()

  def get_ascension_upgrades(self):
    tableBody = self.driver.find_element(By.CLASS_NAME, Constants.TABLE)
    rows = tableBody.find_elements(By.CLASS_NAME, Constants.ROWS)

    ascensions = []
    for x in range(1, len(rows) + 1):
      for j in range(2, len(rows) + 1):
        ICON_FIRST_LINE_NULL = driver.find_element(By.XPATH, f'{Constants.get_div_table(j, 5)}{Constants.IMAGE_WRAPPER}').get_attribute("src")

      ascensions.append({
        "rank": driver.find_element(By.XPATH, Constants.get_div_table(x, 1)).text,
        "level": driver.find_element(By.XPATH, Constants.get_div_table(x, 2)).text,
        "cost": driver.find_element(By.XPATH, Constants.get_div_table(x, 3)).text,
        "material_one": {
          "name": driver.find_element(By.XPATH, Constants.get_div_table(x, 4)).text,
          "icon": driver.find_element(By.XPATH, f'{Constants.get_div_table(x, 4)}{Constants.IMAGE_WRAPPER}').get_attribute("src")
        },
        "material_two": {
          "name": driver.find_element(By.XPATH, Constants.get_div_table(x, 5)).text,
          "icon": ICON_FIRST_LINE_NULL
        },
        "material_three": {
          "name": driver.find_element(By.XPATH, Constants.get_div_table(x, 6)).text,
          "icon": driver.find_element(By.XPATH, f'{Constants.get_div_table(x, 6)}{Constants.IMAGE_WRAPPER}').get_attribute("src")
        },
        "material_four": {
          "name": driver.find_element(By.XPATH, Constants.get_div_table(x, 7)).text,
          "icon": driver.find_element(By.XPATH, f'{Constants.get_div_table(x, 7)}{Constants.IMAGE_WRAPPER}').get_attribute("src")
        }  
      })

    print(ascensions)
      # rank = driver.find_element(By.XPATH, Constants.get_div_table_rank(x, 1))
      # level = driver.find_element(By.XPATH, f'//*[@id="ascension"]/div/div/div[1]/div[2]/div[{x}]/div/div[2]')
      # cost = driver.find_element(By.XPATH, f'//*[@id="ascension"]/div/div/div[1]/div[2]/div[{x}]/div/div[3]')
      # name = driver.find_element(By.XPATH, f'//*[@id="ascension"]/div/div/div[1]/div[2]/div[{x}]/div/div[4]')
      # icon = driver.find_element(By.XPATH, f'//*[@id="ascension"]/div/div/div[1]/div[2]/div[{x}]/div/div[4]{Constants.IMAGE_WRAPPER}')
      # name5 = driver.find_element(By.XPATH, f'//*[@id="ascension"]/div/div/div[1]/div[2]/div[{x}]/div/div[5]')

      # for j in range(2, len(rows) + 1):
      #   icon5 = driver.find_element(By.XPATH, f'//*[@id="ascension"]/div/div/div[1]/div[2]/div[{j}]/div/div[5]{Constants.IMAGE_WRAPPER}')

      # name2 = driver.find_element(By.XPATH, f'//*[@id="ascension"]/div/div/div[1]/div[2]/div[{x}]/div/div[6]')
      # icon2 = driver.find_element(By.XPATH, f'//*[@id="ascension"]/div/div/div[1]/div[2]/div[{x}]/div/div[6]{Constants.IMAGE_WRAPPER}')
      # name3 = driver.find_element(By.XPATH, f'//*[@id="ascension"]/div/div/div[1]/div[2]/div[{x}]/div/div[7]')
      # icon3 = driver.find_element(By.XPATH, f'//*[@id="ascension"]/div/div/div[1]/div[2]/div[{x}]/div/div[7]{Constants.IMAGE_WRAPPER}')

      # self.character['characters'].append({
      #   "upgrades": {
      #     'rank': rank.text,
      #     'level': level.text,
      #     'cost': cost.text,
      #     'material_one': {
      #       'name': name.text,
      #       'icon': icon.get_attribute("src")
      #     },
      #     'material_two': {
      #       'name': name5.text,
      #       'icon': icon5.get_attribute("src")
      #     },
      #     'material_three': {
      #       'name': name2.text,
      #       'icon': icon2.get_attribute("src")
      #     },
      #     'material_four': {
      #       'name': name3.text,
      #       'icon': icon3.get_attribute("src")
      #     },
      #   }
      # })
    return 'Oi'

if __name__ == "__main__":
  driver = start_driver()
  # driver.get('https://genshin.gg')
  driver.get(f"https://genshin.gg/characters/Ayato")
  character = { "characters": [] }
  character = Character(character, driver)

  driver.close()