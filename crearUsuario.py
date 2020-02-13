from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
 
driver = webdriver.Chrome()
driver.get("http://http://localhost:8080/registro")
 
 
if "registro.html" in driver.title:
  print("Funciona")
else:
  print("No funciona")
 
time.sleep(2)
 
 
#editar nombre usuario
element = driver.find_element_by_id("nombre")
value = element.get_attribute("value")
if value == "francsicoTest":
    print("el nombre esta bien")
else:
    print("el nombre no esta bien")
    driver.find_element_by_id("nombre").clear()
    driver.find_element_by_id("nombre").send_keys("francsicoTest")
 
#editar apellido
element = driver.find_element_by_id("apellido")
value = element.get_attribute("value")
if value == "MigliardiTest":
    print("el apellido esta bien")
else:
    print("el apellido no esta bien")
    driver.find_element_by_id("apellido").clear()
    driver.find_element_by_id("apellido").send_keys("MigliardiTest")
 
#editar contrasenia
element = driver.find_element_by_id("contrsena")
value = element.get_attribute("value")
if value == "contrasena123":
    print("la contrasena esta bien")
else:
    print("la contrasena no esta bien")
    driver.find_element_by_id("contrsena").clear()
    driver.find_element_by_id("contrsena").send_keys("contrasena123")
 
#confirmar contrasenia
element = driver.find_element_by_id("contrsena2")
value = element.get_attribute("value")
if value == "contrasena123":
    print("la contrasena esta bien")
else:
    print("la contrasena no esta bien")
    driver.find_element_by_id("contrsena2").clear()
    driver.find_element_by_id("contrsena2").send_keys("contrasena123")
 
#editar ciudad
element = driver.find_element_by_id("nombreUsuario")
value = element.get_attribute("value")
if value == "FranTest":
    print("el nombre de Usuario esta bien")
else:
    print("el nombre de Usuario no esta bien")
    driver.find_element_by_id("nombreUsuario").clear()
    driver.find_element_by_id("nombreUsuario").send_keys("Capital Federal")  
 
#editar correro
element = driver.find_element_by_id("correo")
value = element.get_attribute("value")
if value == "frantest@fran.com":
    print("el correo esta bien")
else:
    print("el correo no esta bien")
    driver.find_element_by_id("correo").clear()
    driver.find_element_by_id("correo").send_keys("frantest@fran.com")  
 
 
#enviar respuesta de usuario creado
driver.find_element_by_id('submit').click()
 
time.sleep(2)
