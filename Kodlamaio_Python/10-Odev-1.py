from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait  # Gerekli bekleme kodlarını import eder
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path
from datetime import date
import constants


class Test_OdevClass:
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)

    def teardown_method(self):
        self.driver.quit()

    def test_deneme(self):
        print("1")

    # Constants kullanımı ile yapılmıştır. Aynı zamanda Selenium IDE ile alınan hazır otomasyon kendi kullandığım yönteme çevrilmiştir.
    @pytest.mark.parametrize("username,pw", [("standard_user", "secret_sauce")])
    def test_add_product(self, username, pw):
        self.waitForElementVisible((By.ID, constants.usernameInput))
        self.driver.find_element(By.ID, constants.usernameInput)
        self.waitForElementVisible((By.ID, constants.passwordInput))
        self.driver.find_element(By.ID, constants.passwordInput)

        action = ActionChains(self.driver)
        action.send_keys_to_element(constants.usernameInput, username)
        action.send_keys_to_element(constants.passwordInput, pw)
        action.perform()

        loginBtn = self.driver.find_element(By.ID, constants.loginBtn)
        loginBtn.click()

        self.waitForElementVisible((By.ID, constants.addInput))
        addInput = self.driver.find_element((By.ID, constants.addInput))
        addInput.click()
        self.waitForElementVisible((By.ID, constants.add2Input))
        add2Input = self.driver.find_element(By.ID, constants.add2Input)
        add2Input.click()
        self.driver.save_screenshot(f"{self.folderPath}/test-add-{username}-{pw}.png")

    @pytest.mark.parametrize("username,pw", [("standard_user", "secret_sauce")])
    def test_product_details(self, username, pw):
        self.waitForElementVisible((By.ID, constants.usernameInput))
        usernameInput = self.driver.find_element(By.ID, constants.usernameInput)
        self.waitForElementVisible((By.ID, constants.passwordInput))
        passwordInput = self.driver.find_element(By.ID, constants.passwordInput)

        usernameInput.send_keys(username)
        passwordInput.send_keys(pw)

        loginBtn = self.driver.find_element(By.ID, constants.loginBtn)
        loginBtn.click()

        self.waitForElementVisible((By.XPATH, constants.detailsInput))
        detailsInput = self.driver.find_element(By.XPATH, constants.detailsInput)
        detailsInput.click()

        self.driver.save_screenshot(f"{self.folderPath}/test-product-details-{username}-{pw}.png")
        sleep(2)

    @pytest.mark.parametrize("username,pw", [("standard_user", "secret_sauce")])
    def test_product_details_and_addtocart(self, username, pw):
        self.waitForElementVisible((By.ID, constants.usernameInput))
        usernameInput = self.driver.find_element(By.ID, constants.usernameInput)
        self.waitForElementVisible((By.ID, constants.passwordInput))
        passwordInput = self.driver.find_element(By.ID, constants.passwordInput)

        usernameInput.send_keys(username)
        passwordInput.send_keys(pw)

        loginBtn = self.driver.find_element(By.ID, constants.loginBtn)
        loginBtn.click()

        self.waitForElementVisible((By.XPATH, constants.detailsInput2))
        detailsInput2 = self.driver.find_element(By.XPATH, constants.detailsInput2)
        detailsInput2.click()

        self.waitForElementVisible((By.ID, constants.addInput3))
        addInput3 = self.driver.find_element(By.ID, constants.addInput3)
        addInput3.click()

        self.driver.save_screenshot(f"{self.folderPath}/test-product-details-andadd-{username}-{pw}.png")

        sleep(2)

    @pytest.mark.parametrize("username,pw", [("", "")])
    def test_null_login(self, username, pw):
        self.waitForElementVisible((By.ID, constants.usernameInput))
        self.waitForElementVisible((By.ID, constants.passwordInput))
        loginBtn = self.driver.find_element(By.ID, constants.loginBtn)
        loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-invalid-login-{username}-{pw}.png")
        assert errorMessage.text == "Epic sadface: Username is required"

    @pytest.mark.parametrize("username,pw", [("standard_user", "")])
    def test_null_password(self, username, pw):
        self.waitForElementVisible((By.ID, constants.usernameInput))
        usernameInput = self.driver.find_element(By.ID, constants.usernameInput)
        self.waitForElementVisible((By.ID, constants.passwordInput))
        passwordInput = self.driver.find_element(By.ID, constants.passwordInput)

        usernameInput.send_keys(username)
        passwordInput.send_keys(pw)

        loginBtn = self.driver.find_element(By.ID, constants.loginBtn)
        loginBtn.click()

        errorMessage = self.driver.find_element(By.XPATH, constants.errorMessage)
        self.driver.save_screenshot(f"{self.folderPath}/test-invalid-login-{username}-{pw}.png")
        assert errorMessage.text == "Epic sadface: Password is required"

    @pytest.mark.parametrize("username,pw", [("locked_out_user", "secret_sauce")])
    def test_username_password(self, username, pw):
        self.waitForElementVisible((By.ID, constants.usernameInput))
        usernameInput = self.driver.find_element(By.ID, constants.usernameInput)
        self.waitForElementVisible((By.ID, constants.passwordInput))
        passwordInput = self.driver.find_element(By.ID, constants.passwordInput)

        usernameInput.send_keys(username)
        passwordInput.send_keys(pw)

        loginBtn = self.driver.find_element(By.ID, constants.loginBtn)
        loginBtn.click()

        errorMessage = self.driver.find_element(By.XPATH, constants.errorMessage)
        self.driver.save_screenshot(f"{self.folderPath}/test-invalid-login-{username}-{pw}.png")
        assert errorMessage.text == "Epic sadface: Sorry, this user has been locked out."

    @pytest.mark.parametrize("username,pw", [("", "")])
    def test_icon(self, username, pw):
        self.waitForElementVisible((By.ID, constants.usernameInput))
        self.waitForElementVisible((By.ID, constants.passwordInput))

        loginBtn = self.driver.find_element(By.ID, constants.loginBtn)
        loginBtn.click()

        self.driver.save_screenshot(f"{self.folderPath}/test-invalid-login-{username}-{pw}.png")

        errorIcon = self.driver.find_element(By.XPATH, constants.errorIcon)
        errorIcon.click()

        self.driver.save_screenshot(f"{self.folderPath}/test-invalid-login-{username}-{pw}.png")

    @pytest.mark.parametrize("username,pw", [("standard_user", "secret_sauce")])
    def test_login_standard_user(self, username, pw):
        self.waitForElementVisible((By.ID, constants.usernameInput))
        usernameInput = self.driver.find_element(By.ID, constants.usernameInput)
        self.waitForElementVisible((By.ID, constants.passwordInput))
        passwordInput = self.driver.find_element(By.ID, constants.passwordInput)

        usernameInput.send_keys(username)
        passwordInput.send_keys(pw)

        loginBtn = self.driver.find_element(By.ID, constants.loginBtn)
        loginBtn.click()

        self.driver.save_screenshot(f"{self.folderPath}/test-invalid-login-{username}-{pw}.png")

        self.driver.get(constants.URL2)

        self.driver.save_screenshot(f"{self.folderPath}/test-invalid-login2-{username}-{pw}.png")

        sleep(2)

    @pytest.mark.parametrize("username,pw", [("standard_user", "secret_sauce")])
    def test_show_product_count(self, username, pw):
        self.waitForElementVisible((By.ID, constants.usernameInput))
        usernameInput = self.driver.find_element(By.ID, constants.usernameInput)
        self.waitForElementVisible((By.ID, constants.passwordInput))
        passwordInput = self.driver.find_element(By.ID, constants.passwordInput)

        usernameInput.send_keys(username)
        passwordInput.send_keys(pw)

        loginBtn = self.driver.find_element(By.ID, constants.loginBtn)
        loginBtn.click()

        itemNumber = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        self.driver.save_screenshot(f"{self.folderPath}/test-item-number-{username}-{pw}.png")
        assert len(itemNumber) == 6

    # ürün ekleme
    @pytest.mark.parametrize("username,pw", [("standard_user", "secret_sauce")])
    def test_add(self, username, pw):
        self.waitForElementVisible((By.ID, constants.usernameInput))
        usernameInput = self.driver.find_element(By.ID, constants.usernameInput)
        self.waitForElementVisible((By.ID, constants.passwordInput))
        passwordInput = self.driver.find_element(By.ID, constants.passwordInput)

        usernameInput.send_keys(username)
        passwordInput.send_keys(pw)
        loginBtn = self.driver.find_element(By.ID, constants.loginBtn)
        loginBtn.click()

        self.waitForElementVisible((By.ID, constants.addInput5))
        addInput5 = self.driver.find_element(By.ID, constants.addInput5)
        addInput5.click()
        self.waitForElementVisible((By.ID, constants.addInput4))
        addInput4 = self.driver.find_element(By.ID, constants.addInput4)
        addInput4.click()
        self.driver.save_screenshot(f"{self.folderPath}/test-add-{username}-{pw}.png")

    # ürün detayına ulaşma
    @pytest.mark.parametrize("username,pw", [("standard_user", "secret_sauce")])
    def test_product_detail(self, username, pw):
        self.waitForElementVisible((By.ID, constants.usernameInput))
        usernameInput = self.driver.find_element(By.ID, constants.usernameInput)
        self.waitForElementVisible((By.ID, constants.passwordInput))
        passwordInput = self.driver.find_element(By.ID, constants.passwordInput)

        usernameInput.send_keys(username)
        passwordInput.send_keys(pw)
        loginBtn = self.driver.find_element(By.ID, constants.loginBtn)
        loginBtn.click()

        self.waitForElementVisible((By.XPATH, constants.detailInputs))
        detailInputs = self.driver.find_element(By.XPATH, constants.detailInputs)
        detailInputs.click()
        self.driver.save_screenshot(f"{self.folderPath}/test-product-detail-{username}-{pw}.png")

    # ürün detayına gidip, ürünü ekleme ve sepete gitme
    @pytest.mark.parametrize("username,pw", [("standard_user", "secret_sauce")])
    def test_product_detail_and_add(self, username, pw):
        self.waitForElementVisible((By.ID, constants.usernameInput))
        usernameInput = self.driver.find_element(By.ID, constants.usernameInput)
        self.waitForElementVisible((By.ID, constants.passwordInput))
        passwordInput = self.driver.find_element(By.ID, constants.passwordInput)

        usernameInput.send_keys(username)
        passwordInput.send_keys(pw)
        loginBtn = self.driver.find_element(By.ID, constants.loginBtn)
        loginBtn.click()

        self.waitForElementVisible((By.XPATH, constants.detailsInputx))
        detailInputx = self.driver.find_element(By.XPATH, constants.detailsInputx)
        detailInputx.click()

        self.waitForElementVisible((By.ID, constants.addInputx))
        addInputx = self.driver.find_element(By.ID, constants.addInputx)
        addInputx.click()

        self.waitForElementVisible((By.XPATH, constants.cartInput))
        cartInput = self.driver.find_element(By.XPATH, constants.cartInput)
        cartInput.click()

        self.driver.save_screenshot(f"{self.folderPath}/test-product-detail-and-add-{username}-{pw}.png")

    def waitForElementVisible(self, locator):
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(locator))