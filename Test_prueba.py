from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from webdriver_manager.chrome import ChromeDriverManager
import HtmlTestRunner

class LoginTest(unittest.TestCase):
    driver = webdriver.Chrome(ChromeDriverManager().install())

    @classmethod
    def setup(cls):
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

    def test_cart(self):
        driver = self.driver
        driver.get("https://academybugs.com/find-bugs/")
        ler = driver.find_element(By.XPATH, "/html/body/div[2]/div/a[2]")
        ler.click()
        a = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/main/article/"
                                          "div/section/ul/li[1]/div/div[3]/div[2]/span/a[1]")
        a.click()
        driver.implicitly_wait(10)
        cart = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/"
                                             "main/article/div/section/div[2]/a")
        cart.click()

    def test_button(self):
        driver = self.driver
        driver.get("https://academybugs.com/find-bugs/")
        driver.implicitly_wait(5)
        b = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/main/article/div/"
                                          "section/div[1]/span[1]/a[1]")
        b.click()

    def test_search(self):
        driver = self.driver
        driver.get("https://academybugs.com/find-bugs/")
        mer = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/"
                                            "main/article/div/section/div[1]/select")
        mer.click()
        driver.implicitly_wait(5)
        dar = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/"
                                            "main/article/div/section/div[1]/select/option[2]")
        dar.click()

    def test_filter(self):
        driver = self.driver
        driver.get("https://academybugs.com/find-bugs/")
        c = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/main/article/div/"
                                          "section/ul/li[1]/div/div[1]/a")
        c.click()
        driver.implicitly_wait(10)
        d = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/aside[5]/div/div[1]/a")
        d.click()

    def test_items(self):
        driver = self.driver
        driver.get("https://academybugs.com/find-bugs/")
        e = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/"
                                          "div/main/article/div/section/ul/li[1]/div/div[1]/a")
        e.click()
        driver.implicitly_wait(10)
        new = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/"
                                            "div[2]/aside[4]/div[1]/ul/li[1]/a")
        new.click()

    def test_post(self):
        driver = self.driver
        driver.get("https://academybugs.com/find-bugs/")
        g = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/"
                                          "main/article/div/section/ul/li[1]/div/div[1]/a")
        g.click()
        driver.implicitly_wait(10)
        h = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/"
                                          "div[1]/main/div/div/form/p[2]/textarea")
        h.send_keys("I love it!")
        i = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/"
                                          "div[1]/main/div/div/form/div/p[1]/input")
        i.send_keys("Maria")
        email = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/"
                                              "div[1]/main/div/div/form/div/p[2]/input")
        email.send_keys("maryjane.gc95@gmail.com")
        poster = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[1]/"
                                               "main/div/div/form/p[3]/button")
        poster.click()

    def test_Product(self):
        driver = self.driver
        driver.get("https://academybugs.com/find-bugs/")
        driver.implicitly_wait(5)
        product = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/main/"
                                                "article/div/section/ul/li[1]/div/div[1]/a")
        product.click()
        driver.implicitly_wait(5)
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
        driver.implicitly_wait(10)
        sing = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/aside[7]/form/div[1]/input")
        sing.send_keys("mariaj.gc95@gmail.com")
        anto = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/aside[7]/form/div[3]/input")
        anto.send_keys("holahola")
        driver.implicitly_wait(5)
        sho = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/aside[7]/form/div[6]/button")
        sho.click()
        driver.implicitly_wait(10)
        close = driver.find_element(By.XPATH, "/html/body/div[7]/div/button")
        close.click()
        driver.implicitly_wait(10)
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

    def test_forget(self):
        driver = self.driver
        driver.get("https://academybugs.com/find-bugs/")
        driver.implicitly_wait(5)
        y = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/"
                                          "div/main/article/div/section/ul/li[1]/div/div[1]/a")
        y.click()
        driver.implicitly_wait(10)
        wrong = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/aside[7]/form/div[1]/input")
        wrong.send_keys("mariaj.gc95@gmail.com")
        fail = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/aside[7]/form/div[3]/input")
        fail.send_keys("lettuce")
        pup = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/aside[7]/form/div[6]/button")
        pup.click()
        driver.implicitly_wait(10)
        nonce = driver.find_element(By.XPATH, "/html/body/div[7]/div/button")
        nonce.click()
        driver.implicitly_wait(5)
        forget = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/"
                                               "div[1]/main/article/div/div[2]/form/div[7]/a")
        forget.click()
        driver.implicitly_wait(10)
        rellenar = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[1]/"
                                                 "main/article/div/div/div[1]/form/div[2]/input")
        rellenar.send_keys("mariaj.gc95@gmail.com")
        but = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[1]/main/"
                                            "article/div/div/div[1]/form/div[3]/input")
        but.click()

    @classmethod
    def test_teardown(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/maria/PycharmProjects/Reports"))

print("Que sera")
