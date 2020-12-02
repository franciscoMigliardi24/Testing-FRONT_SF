from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import configLogin

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
driver.get(cfg['front_base_url'] + 'login')
time.sleep(4)

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

#funcion que busca el campo y lo completa
def completarCamposFunc(idCampo, contenidoCampo):
    try:
        element = driver.find_element_by_id(idCampo)
        element.send_keys(contenidoCampo)
        print("el campo " + idCampo + "fue comletado con " + contenidoCampo)
    except:
        print("el campo " + idCampo + "no fue comletado con " + contenidoCampo)


time.sleep(2)

#ir a crear factura
driver.find_element_by_class_name('boton-2').click()

time.sleep(2)

#ir a agregar factura
driver.find_element_by_name('agregar-factura').click()

#ir a agregar cliente
driver.find_element_by_id('selector').click()

time.sleep(1)

# seleccionar cliente
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[2]/div[1]/select/option').click()

# completar numero factura
completarCamposFunc('numeroFactura', '123')

# completar orden de compra
completarCamposFunc('ordenCompra', 'orden factura 1')

# completar fecha factura
completarCamposFunc('fechaFactura', '2019-07-05')

# completar fecha vencimiento
completarCamposFunc('fechaVencimiento', '2019-08-05')

# completar descripcion del Proyecto
completarCamposFunc('descripcionProyecto', 'descripcion del Proyecto')

#seleccionar Tipo de trabajo
driver.find_element_by_id('seleccion').click()

time.sleep(1)

# seleccionar traduccion
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[2]/div[4]/table/tbody/tr[1]/td[2]/select/option[1]').click()

# completar numero de Palabras
completarCamposFunc('numeroPalabras', '1000')

# completar notas
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[2]/div[4]/table/tbody/tr[3]/td/textarea').send_keys('notas')

#enviar factura creada
try:
  driver.find_element_by_id('boton-enviar').click()
  print("factura creada")
except:
  print("factura no creada")


#descargar factura creada
try:
  driver.find_element_by_class_name('icono-i').click()
  print("factura descargada")
except:
  print("factura no descargada")