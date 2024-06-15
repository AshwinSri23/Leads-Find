# --- Imports
import os
import csv
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from elements import *

# --- Global variables
load_dotenv()
TEST_COMPANY = "Google"
TEST_RR_EMAIL = os.getenv("TEST_RR_EMAIL")
TEST_RR_PASSWORD = os.getenv("TEST_RR_PASSWORD")
CSV_FILE_NAME = "data.csv"
MAX_TIMEOUT = 10

# --- Setup
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


# --- Functions
def main():

  driver.get("https://rocketreach.co/login")

  rrLogin()
  rrLookup(TEST_COMPANY)

  people = rrGetPeople(TEST_COMPANY)

  # ! Test
  print("People: ")
  print(people)

  csvWriteUsers(people)


def rrLogin():
  # Input email and password
  elementSendKeys(TEST_RR_EMAIL, elementInputLoginEmail)
  elementSendKeys(TEST_RR_PASSWORD, elementInputLoginPassword)

  # Click login button
  elementClick(elementButtonLoginSubmit)


def rrRegister():
  # ! next: work on registration
  pass


def rrLookup(company: str):
  # Apply filters
  applyFilters(company)


def rrGetPeople(company: str) -> list[list]:
  people = []

  for i in range(10):
    # Find result div
    locator = (elementTemplateDivSearchResult[0], elementTemplateDivSearchResult[1].format(i))
    resultDiv = WebDriverWait(driver, MAX_TIMEOUT).until(expected_conditions.presence_of_element_located(locator))
    view = resultDiv.find_elements(By.TAG_NAME,'button')
    print(view)
    # Create person array with the company name first

    # Name
    # ! error: ptag or name not being found

    ##Finding the element containing the name of the person

    ##      //*[@id="blur-container"]/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/rr-unified-search-results/div/div[3]/div/ul/li[2]/div/svelte-component//div/div/div[1]/div[1]/div[3]/p[1]/a
    ##index = index.format(i + 1)
    ptag = elementFind(elementPTagName, resultDiv)
    ###name = elementFind((By.TAG_NAME, 'a'), ptag).text
    profileCardInfo = ptag.text.split("\n");
    print(profileCardInfo)

    person = [profileCardInfo[2],profileCardInfo[0]]



    ##
    ##/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/rr-unified-search-results/div/div[3]/div/ul/li[1]

    # Emails
    # TODO: get emails, record getting the contact & HTML elements change

    people.append(person)

  return people


def csvWriteUsers(people):
  try:
    with open(CSV_FILE_NAME, mode='w', newline='') as file:
      writer = csv.writer(file)
      writer.writerow(['Company', 'Name', 'Email', 'Status', 'Amount ($)', 'Notes'])

      for person in people:
        writer.writerow(person)

  except OSError:
    print("Could not open file:", CSV_FILE_NAME)
    exit(1)


def applyFilters(company: str):
  # Clear filters, if necessary
  try:
    elementClick(elementButtonClearFilters)
  except TimeoutException:
    pass

  time.sleep(3)

  # Filter 1: Company Name or Domain
  elementClick(elementButtonCompanyNameOrDomain)
  elementSendKeys(company + Keys.ENTER, elementInputCompanyNameOrDomain)


def elementWaitUntilClickable(element: tuple[str, str]) -> WebElement | None:
  return WebDriverWait(driver, MAX_TIMEOUT).until(
    expected_conditions.element_to_be_clickable(element)
  )


def elementClick(element: tuple[str, str]):
  try:
    elementWaitUntilClickable(element).click()
  except NoSuchElementException:
    return None


def elementSendKeys(value: any, element: tuple[str, str]):
  try:
    elementWaitUntilClickable(element).send_keys(value)
  except NoSuchElementException:
    return


def elementFind(element: WebElement | tuple[str, str], inElement: WebElement | None = None) -> WebElement | None:
  ##Checking if the first parameter is a subclass of the 2nd parameter
  try:
    if isinstance(element, WebElement):
      return element
    ##Checking if the element exists with the given parameter.
    else:
      by, value = element
      if inElement is None:
        return driver.find_element(by, value)
      else:
        return inElement.find_element(by, value)
  except NoSuchElementException:
    return None


# --- Main control flow
if __name__ == "__main__":
  main()
