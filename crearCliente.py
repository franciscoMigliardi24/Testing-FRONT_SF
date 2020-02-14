from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("http://localhost:8080/login")

if "login" in driver.title:
  print("Se pudo entrar a la pagina de login")
else:
  print("No se pudo entrar a la pagina de login")

#iniciar sesion
elem = driver.find_element_by_id("nombreUsuario")
elem.send_keys("FranTest")
elem = driver.find_element_by_id("contrasena")
elem.send_keys("contrasena123")

driver.find_element_by_class_name('buttonhover').click()

time.sleep(2)

#varifica si se pudo inciar sesion
if "logged" in driver.title:
  print("Se pudo iniciar sesion")
else:
  print("No se pudo iniciar sesion")

time.sleep(2)

#ir a crear cliente
driver.find_element_by_class_name('boton-1').click()

#abrir modal para crear cliente
driver.find_element_by_id('agregarCliente').click()

#funcion que busca el campo y lo completa
def completarCamposFunc(idCampo, contenidoCampo):
    try:
        element = driver.find_element_by_name(idCampo)
        element.send_keys(contenidoCampo)
        print("el campo " + idCampo + "fue comletado con " + contenidoCampo)
    except:
        print("el campo " + idCampo + "no fue comletado con " + contenidoCampo)

#ingresar nombre del cliente
completarCamposFunc("nombreCliente", "cliente1")

#ingresar ciudad
completarCamposFunc("ciudad", "Buenos Aires")

#ingresar estado
completarCamposFunc("estado", "Capital Federal")

#ingresar pais
completarCamposFunc("pais", "Argentina")

#ingresar correro
completarCamposFunc("correo", "cliente@cliente.com")

#ingresar direccion
completarCamposFunc("direccion", "calle falsa 123")

#ingresar codigo postal
completarCamposFunc("codigoPostal", "1426") 

#ingresar termino de pago
completarCamposFunc("terminoPago", "12")

#ingresar palabra traduccion
completarCamposFunc("palabraTraduccion", "20")

#ingresar palabra edicion
completarCamposFunc("palabraEdicion", "15")

#ingresar palabra Proofreading
completarCamposFunc("palabraProofreading", "1")

time.sleep(2)

#enviar cliente creado
try:
  driver.find_element_by_id('boton-enviar').click()
  print("cliente creado")
except:
  print("cliente no creado")
