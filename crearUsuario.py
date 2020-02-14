from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
 
driver = webdriver.Firefox()
driver.get("http://localhost:8080/registro")
 
time.sleep(2)

#verifica si se puedo entrar a la pagina para crear un usuario
if "registro.html" in driver.title:
  print("Se pudo entras a la pagina de registro de usuario")
else:
  print("No se pudo entras a la pagina de registro de usuario")


#funcion que busca el campo y lo completa
def completarCamposFunc(idCampo, contenidoCampo):
    try:
        element = driver.find_element_by_id(idCampo)
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
try:
  driver.find_element_by_id('submit').click()
  print("usuario creado")
except:
  print("usuario no creado")
