from selenium.webdriver.common.by import By

class Constants:
  TABLE = 'rt-tbody'
  ROWS = 'rt-tr'
  IMAGE_WRAPPER = '//*[@class="table-image-wrapper"]//*[@class="table-image"]'

  def get_div_table(i: int, line: int) -> str:
    return f'//*[@id="ascension"]/div/div/div[1]/div[2]/div[{i}]/div/div[{line}]'

  def ascension(driver, loop, line) -> str:
    return driver.find_element(By.XPATH, Constants.get_div_table(loop, line)).text,
