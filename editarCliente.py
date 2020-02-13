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
driver.find_element_by_class_name('editar-tabla').click()



#ingresar nombre del cliente
element = driver.find_element_by_name("nombreCliente")
value = element.get_attribute("value")
if value == "cliente1":
	print("el nombre esta bien")
else:
	print("el nombre no esta bien")
	driver.find_element_by_name("nombreCliente").clear()
	driver.find_element_by_name("nombreCliente").send_keys("cliente1")

#ingresar ciudad
element = driver.find_element_by_name("ciudad")
value = element.get_attribute("value")
if value == "Buenos Aires":
	print("la ciudad esta bien")
else:
	print("la ciudad no esta bien")
	driver.find_element_by_name("ciudad").clear()
	driver.find_element_by_name("ciudad").send_keys("Buenos Aires")

#ingresar estado
element = driver.find_element_by_name("estado")
value = element.get_attribute("value")
if value == "Capital Federal":
	print("el estado esta bien")
else:
	print("el estado no esta bien")
	driver.find_element_by_name("estado").clear()
	driver.find_element_by_name("estado").send_keys("Capital Federal")

#ingresar pais
element = driver.find_element_by_name("pais")
value = element.get_attribute("value")
if value == "Argentina":
	print("el pais esta bien")
else:
	print("el pais no esta bien")
	driver.find_element_by_name("pais").clear()
	driver.find_element_by_name("pais").send_keys("Argentina")

#ingresar correro
element = driver.find_element_by_name("correo")
value = element.get_attribute("value")
if value == "cliente@cliente.com":
	print("el correo esta bien")
else:
	print("el correo no esta bien")
	driver.find_element_by_name("correo").clear()
	driver.find_element_by_name("correo").send_keys("cliente@cliente.com")  

#ingresar direccion
element = driver.find_element_by_name("direccion")
value = element.get_attribute("value")
if value == "calle falsa 123":
	print("la direccion esta bien")
else:
	print("la direccion no esta bien")
	driver.find_element_by_name("direccion").clear()
	driver.find_element_by_name("direccion").send_keys("calle falsa 123")



#ingresar codigo postal
element = driver.find_element_by_name("codigoPostal")
value = element.get_attribute("value")
if value == "1426":
	print("el codigoPostal esta bien")
else:
	print("el codigoPostal no esta bien")
	driver.find_element_by_name("codigoPostal").clear()
	driver.find_element_by_name("codigoPostal").send_keys("1426")   

#ingresar termino de pago
element = driver.find_element_by_name("terminoPago")
value = element.get_attribute("value")
if value == "12":
	print("el termino de Pago esta bien")
else:
	print("el termino de Pago no esta bien")
	driver.find_element_by_name("terminoPago").clear()
	driver.find_element_by_name("terminoPago").send_keys("12") 

#ingresar palabra traduccion
element = driver.find_element_by_name("palabraTraduccion")
value = element.get_attribute("value")
if value == "20":
	print("la palabra Traduccion esta bien")
else:
	print("la palabra Traduccion no esta bien")
	driver.find_element_by_name("palabraTraduccion").clear()
	driver.find_element_by_name("palabraTraduccion").send_keys("20") 

#enviar cliente creado
driver.find_element_by_class_name('botonenviar').click()

time.sleep(2)