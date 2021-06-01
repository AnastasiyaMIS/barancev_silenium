from selenium import webdriver
from selenium.webdriver.common.by import By

class Application:
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path='../geckodriver-v0.29.1-win64/geckodriver.exe')
        self.vars = {}

    def logout(self):
        # логаут
        self.driver.find_element(By.LINK_TEXT, "Logout").click()

    def return_to_group(self):
        # возвращаемся на страницу групп
        self.driver.find_element(By.LINK_TEXT, "groups").click()
        self.driver.find_element(By.CSS_SELECTOR, "body").click()

    def create_group(self, group):
        # создаем новую группу
        self.driver.find_element(By.NAME, "new").click()
        # заполняем форму
        self.driver.find_element(By.NAME, "group_name").click()
        self.driver.find_element(By.NAME, "group_name").send_keys(group.name)
        self.driver.find_element(By.NAME, "group_header").click()
        self.driver.find_element(By.NAME, "group_header").send_keys(group.header)
        self.driver.find_element(By.NAME, "group_footer").click()
        self.driver.find_element(By.NAME, "group_footer").send_keys(group.footer)
        self.driver.find_element(By.CSS_SELECTOR, "body").click()
        self.driver.find_element(By.NAME, "submit").click()

    def login(self, username, password):
        # выполняем логин
        self.driver.find_element(By.NAME, "user").send_keys(username)
        self.driver.find_element(By.NAME, "pass").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

    def open_home_page(self):
        self.driver.get("http://localhost/addressbook/")
        self.driver.set_window_size(1353, 861)

    def destroy(self):
        self.driver.quit()