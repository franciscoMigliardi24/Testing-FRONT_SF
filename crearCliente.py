from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("http://localhost:8081/login")

if "logged.html" in driver.title:
  print("Se pudo entras a la pagina de login")
else:
  print("No se pudo entras a la pagina de login")


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
driver.find_element_by_class_name('boton-enviar').click()
ale = driver.switch_to_alert()
ale.text
ale.accept()
