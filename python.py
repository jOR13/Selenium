# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys


# # Crear una sesión de Firefox
# driver = webdriver.Firefox()
# driver.implicitly_wait(30)
# driver.maximize_window()

# # Acceder a la aplicación web
# # driver.get("http://www.google.es")

# # driver.get ("https://www.facebook.com")
# driver.get ("https://randomtodolistgenerator.herokuapp.com/library")


# # driver.find_element_by_id("email").send_keys("chuypack@hotmail.com")
# # driver.find_element_by_id("pass").send_keys("lol123")
# # driver.find_element_by_id("u_0_b").click()

# # Cerrar la ventana del navegador
# # driver.quit()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

with webdriver.Firefox() as driver:
    wait = WebDriverWait(driver, 10)

    driver.get("https://randomtodolistgenerator.herokuapp.com/library")

    todo = []

    for x in range(6):

        element = driver.find_element_by_xpath(
            '/html/body/div/div/div/div/div[2]/div['+str(x+1)+']/div/div/div[1]')
        # print(element.text)
        todo.append(element.text)

    driver.get("https://todoist.com/users/showlogin")

    driver.find_element_by_id("email").send_keys("cjastw_m35f@cikuh.com")
    driver.find_element_by_id("password").send_keys("test12345678")
    driver.find_element_by_xpath('//*[@id="login_form"]/button').click()

    driver.get("https://todoist.com/app/#/today")

    driver.find_element_by_xpath('//*[@id="agenda_view"]/div/div/div/ul/li[2]/button').click()

    driver.find_element_by_xpath('//*[@id="agenda_view"]/div/div/div/ul/li[2]/form/div[1]/div[1]/div').send_keys(todo[1])


    driver.maximize_window()


    driver.quit()
