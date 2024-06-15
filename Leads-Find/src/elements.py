from selenium.webdriver.common.by import By

elementInputLoginEmail = (By.ID, "id_email")
elementInputLoginPassword = (By.ID, "id_password")
elementButtonLoginSubmit = (By.CLASS_NAME, "btn-primary")
elementButtonClearFilters = (By.XPATH,
                             '//*[@id="blur-container"]/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[2]/button')
elementButtonCompanyNameOrDomain = (By.XPATH,
                                    '//*[@id="blur-container"]/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[3]/div[1]/div[5]/div[2]/div[1]')
elementInputCompanyNameOrDomain = (By.XPATH,
                                   '//*[@id="blur-container"]/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[3]/div[1]/div[5]/div[2]/div[1]/rr-search-facet-input/div/div[2]/div[1]/div/input')
elementTemplateDivSearchResult = (By.CLASS_NAME, 'search-results-list-item--{}')
elementPTagName = (By.CLASS_NAME, 'ng-scope')
elementViewButton = (By.XPATH, '//button[normalize-space("Get Contact Info")]')


