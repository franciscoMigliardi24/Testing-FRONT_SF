from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
 
driver = webdriver.Chrome()
driver.get("http://http://localhost:8080/registro")
 
time.sleep(2)

if "logged.html" in driver.title:
  print("Se pudo entras a la pagina de login")
else:
  print("No se pudo entras a la pagina de login")


#funcion que busca el campo y lo completa
def completarCamposFunc(idCampo, contenidoCampo):
    try:
        element = driver.find_element_by_name(idCampo)
        element.send_keys(contenidoCampo)
        print("el campo " + idCampo + "fue comletado con " + contenidoCampo)
    except:
        print("el campo " + idCampo + "no fue comletado con " + contenidoCampo)


#editar nombre usuario
completarCamposFunc("nombre", "francsicoTest")
 
#editar apellido
completarCamposFunc("apellido", "MigliardiTest")
 
#editar contrasenia
completarCamposFunc("contrsena", "contrasena123")
 
#confirmar contrasenia
completarCamposFunc("contrsena2", "contrasena123")
 
#editar ciudad
completarCamposFunc("nombreUsuario", "FranTest")

#editar correro
completarCamposFunc("correo", "frantest@fran.com") 
 
time.sleep(2)

#enviar respuesta de usuario creado
driver.find_element_by_id('submit').click()
ale = driver.switch_to_alert()
ale.text
ale.accept
