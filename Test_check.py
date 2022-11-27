from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from webdriver_manager.chrome import ChromeDriverManager


class LoginTest(unittest.TestCase):
    driver = webdriver.Chrome(ChromeDriverManager().install())

    @classmethod
    def setup(cls):
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

    def test_Product(self):
        driver = self.driver
        driver.get("https://academybugs.com/find-bugs/")
        driver.implicitly_wait(5)
        hell = driver.find_element(By.XPATH, "/html/body/div[2]/div/a[2]")
        hell.click()
        product = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/main/"
                                                "article/div/section/ul/li[1]/div/div[1]/a")
        product.click()
        caja = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/"
                                             "div[2]/aside[2]/div/form/input[1]")
        caja.send_keys("blue")
        search = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/"
                                               "div[2]/aside[2]/div/form/input[2]")
        search.click()

    def test_new(self):
        driver = self.driver
        driver.get("https://academybugs.com/find-bugs/")
        driver.implicitly_wait(3)
        new = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/"
                                            "main/article/div/section/ul/li[1]/div/div[1]/a")
        new.click()
        driver.implicitly_wait(5)
        login = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/aside[7]/form/div[4]/p/a")
        login.click()
        driver.implicitly_wait(5)
        near = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[1]/"
                                             "main/article/div/div/div[1]/form/div[2]/input")
        near.send_keys("Maria")
        log = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[1]/main/"
                                            "article/div/div/div[1]/form/div[3]/input")
        log.send_keys("Guerra")
        pro = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[1]/main/"
                                            "article/div/div/div[1]/form/div[4]/input")
        pro.send_keys("maryjane.gc95@gmail.com")
        he = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[1]/main/"
                                           "article/div/div/div[1]/form/div[5]/input")
        he.send_keys("maryjane.gc95@gmail.com")
        cote = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[1]/main/"
                                             "article/div/div/div[1]/form/div[6]/input")
        cote.send_keys("Antonella")
        rob = driver.find_element(By.XPATH, "/html/body/div[3]/"
                                            "div/div/div[1]/main/article/div/div/div[1]/form/div[7]/input")
        rob.send_keys("Antonella")
        nami = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[1]/main/"
                                             "article/div/div/div[1]/form/div[8]/input[2]")
        nami.click()

    def test_password(self):
        driver = self.driver
        driver.get("https://academybugs.com/find-bugs/")
        lol = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/"
                                            "main/article/div/section/ul/li[1]/div/div[1]/a")
        lol.click()
        sing = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/aside[7]/form/div[1]/input")
        sing.send_keys("mariaj.gc95@gmail.com")
        anto = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/aside[7]/form/div[3]/input")
        anto.send_keys("holahola")
        driver.implicitly_wait(4)
        sho = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/aside[7]/form/div[6]/button")
        sho.click()
        close = driver.find_element(By.XPATH, "/html/body/div[7]/div/button")
        close.click()
        password = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/"
                                                 "div[1]/main/article/div/div/div[3]/div[5]/a")
        password.click()
        current = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[1]/main/article/"
                                                "div/div/div[1]/form/div[1]/input")
        current.send_keys("holahola")
        change = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[1]/main/"
                                               "article/div/div/div[1]/form/div[2]/input")
        change.send_keys("holahola")
        retype = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[1]/main/"
                                               "article/div/div/div[1]/form/div[3]/input")
        retype.send_keys("holahola")
        update = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[1]/main/"
                                               "article/div/div/div[1]/form/div[4]/input")
        update.click()

    @classmethod
    def test_teardown(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")

if __name__ == '__main__':
    unittest.m

print("Que sera")
