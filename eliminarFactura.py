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

time.sleep(2)

#ir a crear factura
driver.find_element_by_class_name('boton-2').click()

time.sleep(2)

try:
    driver.find_element_by_css_selector('tr.seleccionar-f:nth-child(5) > td:nth-child(1) > input:nth-child(1)').click()
    print('factura seleccionada')
    try:
        driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/div[2]/button').click()
        print('factura borrada')
    except:
        print('no se pudo borrar')
except:
    print('no se pudo seleccionar la factura')
