from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("http://localhost:8081/login")


if "login.html" in driver.title:
  print("Funciona")
else:
  print("No funciona")

#iniciar sesion
elem = driver.find_element_by_name("nombreUsuario")
elem.send_keys("FranTest")
elem = driver.find_element_by_name("contraseña")
elem.send_keys("contrasena123")

driver.find_element_by_class_name('boton-enviar').click()


time.sleep(2)

#ir a crear cliente
driver.find_element_by_class_name('boton-1').click()

#abrir modal para crear cliente
driver.find_element_by_class_name('agregarCliente').click()

#ingresar nombre del cliente
element = driver.find_element_by_name("nombreCliente")
element.send_keys("cliente1")

#ingresar ciudad
element = driver.find_element_by_name("ciudad")
element.send_keys("Buenos Aires")

#ingresar estado
element = driver.find_element_by_name("estado")
element.send_keys("Capital Federal")

#ingresar pais
element = driver.find_element_by_name("pais")
element.send_keys("Argentina")

#ingresar correro
element = driver.find_element_by_name("correo")
element.send_keys("cliente@cliente.com")  

#ingresar direccion
element = driver.find_element_by_name("direccion")
element.send_keys("calle falsa 123")

#ingresar codigo postal
element = driver.find_element_by_name("codigoPostal")
element.send_keys("1426")   

#ingresar termino de pago
element = driver.find_element_by_name("terminoPago")
element.send_keys("12") 

#ingresar palabra traduccion
element = driver.find_element_by_name("palabraTraduccion")
element.send_keys("20") 

#ingresar palabra edicion
element = driver.find_element_by_name("palabraEdicion")
element.send_keys("15") 

#ingresar palabra Proofreading
element = driver.find_element_by_name("palabraProofreading")
element.send_keys("1") 


#enviar cliente creado
driver.find_element_by_class_name('boton-enviar').click()

time.sleep(2)