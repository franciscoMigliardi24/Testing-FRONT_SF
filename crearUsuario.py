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
element.send_keys("francsicoTest")
 
#editar apellido
element = driver.find_element_by_id("apellido")
element.send_keys("MigliardiTest")
 
#editar contrasenia
element = driver.find_element_by_id("contrsena")
element.send_keys("contrasena123")
 
#confirmar contrasenia
element = driver.find_element_by_id("contrsena2")
element.send_keys("contrasena123")
 
#editar ciudad
element = driver.find_element_by_id("nombreUsuario")
element.send_keys("FranTest")  
 
#editar correro
element = driver.find_element_by_id("correo")
element.send_keys("frantest@fran.com")  
 
 
#enviar respuesta de usuario creado
driver.find_element_by_id('submit').click()
 
time.sleep(2)
