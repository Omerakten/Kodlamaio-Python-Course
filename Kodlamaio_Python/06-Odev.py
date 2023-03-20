# AMAÇ:
#
# Derste gösterilen konuların pekiştirilmesi.
#
# ÖDEV TANIMI:
#
# Aşağıda verilen test caselerin hepsini "https://www.saucedemo.com/" sitesinde gerçekleştirmeniz istenmektedir.
#
# Yazacağınız tüm kodları oluşturduğunuz bir classda fonksiyonlar oluşturarak gerçekleştiriniz. Bu classın fonksiyonlarını çağırarak test ediniz.
#
# Test Caseler;
#
# Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required" gösterilmelidir.
# Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak "Epic sadface: Password is required" gösterilmelidir.
# Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.
# Kullanıcı adı ve şifre alanları boş geçildiğinde bu iki inputun yanında da kırmızı "X" ikonu çıkmalıdır. Daha sonra aşağıda çıkan uyarı mesajının kapatma butonuna tıklandığında bu "X" ikonları kaybolmalıdır. (Tek test casede işleyiniz)
# Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir.
# Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(ChromeDriverManager().install())
class sauce:

    def empty_username_password(self):

        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()

        logbtn = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/input")

        logbtn.click()

        required_message = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        test_result = required_message.text == "Epic sadface: Username is required"
        print(f"Test Sonucu: {test_result}")


    def empty_password(self):

        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()

        userNameInput = driver.find_element(By.ID,"user-name")
        userNameInput.click()
        userNameInput.send_keys("1")
        logbtn = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/input")

        logbtn.click()

        required_message = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        test_result = required_message.text == "Epic sadface: Password is required"
        print(f"Test Sonucu: {test_result}")

    def locked_out_user_secret_sauce(self):

        driver.get("https://www.saucedemo.com/")
        driver.maximize_window() #ekranı tam ekran yapar


        userNameInput = driver.find_element(By.ID, "user-name") #yolu bulma
        userNameInput.click() #tıklama işlemi
        userNameInput.send_keys("locked_out_user") #yazma işlemi

        passwordInput = driver.find_element(By.ID,"password") #yol bulma
        passwordInput.click() #tıkladı
        passwordInput.send_keys("secret_sauce")

        logbtn = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/input") # yol bulucu xpath

        logbtn.click()


        required_message = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")  # yol bulucu full xpath
        test_result = required_message.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"Test Sonucu: {test_result}")

    def empty_login_(self):

        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()  # ekranı tam ekran yapar


        logbtn = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/input")  # yol bulucu xpath
        logbtn.click()

        if driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button"):
            print("X Tespit edildi:")
            logbtn2 = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button")
            logbtn2.click()
            print("X KAPATILDI")
        else:
            print("X Tespit edilemedi:")

    def standard_user_secret_sauce(self):

        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()  # ekranı tam ekran yapar

        userNameInput = driver.find_element(By.ID, "user-name")  # yolu bulma
        userNameInput.click()  # tıklama işlemi
        userNameInput.send_keys("standard_user")  # yazma işlemi

        passwordInput = driver.find_element(By.ID, "password")  # yol bulma
        passwordInput.click()  # tıkladı
        passwordInput.send_keys("secret_sauce")

        logbtn = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/input")  # yol bulucu xpath
        logbtn.click()


        list = driver.find_elements(By.CLASS_NAME, "inventory_item")
        listPrint = len(list)
        print(listPrint)



deneme = sauce()
deneme.empty_username_password()
deneme.empty_password()
deneme.locked_out_user_secret_sauce()
deneme.empty_login_()
deneme.standard_user_secret_sauce()


