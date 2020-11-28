from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import configRegistro

#llama al archivo config
cfgFile = open('test_front.cfg', 'r').read().split('\n')
cfg = {}
for line in cfgFile:
  if '#' in line:
    line = line[:line.find('#')]
  setting = line.split('=')
  cfg[setting[0].strip()] = setting[1].strip().replace('"', '')

driver = None
if cfg['web_driver'] == 'Firefox':
  driver = webdriver.Firefox()
elif cfg['web_driver'] == 'Chrome':
  driver = webdriver.Chrome()
driver.get(cfg['front_base_url'] + 'registro')
time.sleep(4)

 
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
completarCamposFunc("nombreUsuario", "FranTest1")

#editar correro
completarCamposFunc("correo", "frantest1@fran.com") 
 
time.sleep(2)

#enviar respuesta de usuario creado
try:
  driver.find_element_by_id('submit').click()
  print("usuario creado")
except:
  print("usuario no creado")
