from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def init_webdriver() -> webdriver:
  chrome_args = ['--log-level=3', '--silent', '--disable-extensions', '--disable-popup-blocking',
                  '--disable-blink-features', '--disable-blink-features=AutomationControlled', '--headless']
  options = Options()

  for arg in chrome_args:
    options.add_argument(arg)

  driver = webdriver.Chrome(options=options)

  return driver

def start_driver() -> None:
  try:
    return init_webdriver()
  except Exception as e:
    print(f'[ERROR] to initialize webdriver: {e}')