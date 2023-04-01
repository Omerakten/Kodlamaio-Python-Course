from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path
from datetime import date


class Test_sauce_Test:

    # her testen once cagirilan methodumuz
    def setup(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)

    # her test sonunda cagirilan methodumuz
    def teardown(self):
        self.driver.quit()

    # sayfada maximum 5 saniye olacak sekilde beklemesini saglayan methodumuz
    def waitForElementVisible(self, locator, timeout=5):
        WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))

    # username ve password alanlarinin bos olmasi durumu
    def test_null_username_and_password(self):
        self.waitForElementVisible((By.ID, "user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        usernameInput.send_keys("")
        self.waitForElementVisible((By.ID, "password"))
        passwordInput = self.driver.find_element(By.ID, "password")
        passwordInput.send_keys("")
        self.waitForElementVisible((By.ID, "login-button"))
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test_null_username_and_password.png")
        assert errorMessage.text == "Epic sadface: Username is required"

    # password alaninin bos olmasi durumu
    def test_null_password(self):
        self.waitForElementVisible((By.ID, "user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        usernameInput.send_keys("rabia")
        self.waitForElementVisible((By.ID, "password"))
        passwordInput = self.driver.find_element(By.ID, "password")
        passwordInput.send_keys("")
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test_null_password.png")
        assert errorMessage.text == "Epic sadface: Password is required"

    # locked_out_user olayi
    def test_locked_out_user(self):
        self.waitForElementVisible((By.ID, "user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        usernameInput.send_keys("locked_out_user")
        self.waitForElementVisible((By.ID, "password"))
        passwordInput = self.driver.find_element(By.ID, "password")
        passwordInput.send_keys("secret_sauce")
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test_locked_out_user.png")
        assert errorMessage.text == "Epic sadface: Sorry, this user has been locked out."

    # error messagedaki carpi isaretine basinci diger iki carpinin kaybolmasi
    def test_close_button(self):
        self.waitForElementVisible((By.ID, "user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        usernameInput.send_keys("")
        self.waitForElementVisible((By.ID, "password"))
        passwordInput = self.driver.find_element(By.ID, "password")
        passwordInput.send_keys("")
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        errorIcon = self.driver.find_element(By.CLASS_NAME, "error-button")
        errorIcon.click()
        self.driver.save_screenshot(f"{self.folderPath}/test_close_x.png")

    # invertory.html sayfasina gidis
    def test_inventory_html(self):
        self.waitForElementVisible((By.ID, "user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        usernameInput.send_keys("standard_user")
        self.waitForElementVisible((By.ID, "password"))
        passwordInput = self.driver.find_element(By.ID, "password")
        passwordInput.send_keys("secret_sauce")
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        self.driver.save_screenshot(f"{self.folderPath}/test-go_to_page-{'standard_user'}-{'secret_sauce'}.png")
        assert self.driver.current_url == "https://www.saucedemo.com/inventory.html"

    # dogru kullanici adi ve sifreyle girdigimizde urunlerin listelenme durumu
    @pytest.mark.smoke
    def test_listing(self):
        self.waitForElementVisible((By.ID, "user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        usernameInput.send_keys("standard_user")
        self.waitForElementVisible((By.ID, "password"))
        passwordInput = self.driver.find_element(By.ID, "password")
        passwordInput.send_keys("secret_sauce")
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        self.waitForElementVisible((By.CLASS_NAME, "inventory_item"))
        products = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(products) > 0
        self.driver.save_screenshot(f"{self.folderPath}/test_listing.png")

    # parametrize dekoratorunu de kullanarak 3 farkli kullanici ile giris yapmak
    @pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce"), ("problem_user", "secret_sauce"),
                                                   ("performance_glitch_user", "secret_sauce")])
    def test_different_users(self, username, password):
        self.waitForElementVisible((By.ID, "user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID, "password"))
        passwordInput = self.driver.find_element(By.ID, "password")
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        assert self.driver.current_url == "https://www.saucedemo.com/inventory.html"

    # parametrize dekoratoru ile urunlerin listelenme seklini dene
    def test_list_style(self):
        self.waitForElementVisible((By.ID, "user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        usernameInput.send_keys("standard_user")
        self.waitForElementVisible((By.ID, "password"))
        passwordInput = self.driver.find_element(By.ID, "password")
        passwordInput.send_keys("secret_sauce")
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        self.waitForElementVisible((By.CLASS_NAME, "inventory_item"))
        liststyle = self.driver.find_element(By.ID, "//*[@id='header_container']/div[2]/div/span/select")

        # parametrize dekoratoru ile urunlerin tum yani 4 farkli siralanma sekline gore dogru bir sekilde siralanma durumu

    @pytest.mark.parametrize("sorting_option", ["az", "za", "lohi", "hilo"])
    def test_product_sorting(self, sorting_option):
        self.waitForElementVisible((By.ID, "user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        usernameInput.send_keys("standard_user")
        self.waitForElementVisible((By.ID, "password"))
        passwordInput = self.driver.find_element(By.ID, "password")
        passwordInput.send_keys("secret_sauce")
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        self.sortingDropdown = self.driver.find_element(By.XPATH, "//select[@class='product_sort_container']")
        self.sortingDropdown.click()
        sortingOptionXpath = f"//option[text()='{sorting_option}']"
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, sortingOptionXpath)))
        sortingOption = self.driver.find_element(By.XPATH, sortingOptionXpath)
        sortingOption.click()
        time.sleep(2)  # waiting for sorting to complete
        products = self.driver.find_elements(By.XPATH, "//div[@class='inventory_item_name']")
        product_names = [p.text for p in products]
        if sorting_option == "az":
            assert product_names == sorted(product_names)
        elif sorting_option == "za":
            assert product_names == sorted(product_names, reverse=True)
        elif sorting_option == "lohi":
            assert product_names == sorted(product_names, key=lambda s: s.lower())
        elif sorting_option == "hilo":
            assert product_names == sorted(product_names, key=lambda s: s.lower(), reverse=True)
