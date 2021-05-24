# Con unittest nos podemos traer todas nuestras pruebas
import unittest
# Ayuda a orquestar cada una de las pruebas que estaremos
# ejecutando junto con los reportes
from pyunitreport import HTMLTestRunner
# Para comunicarnos con el navegador usamos webdriver
from selenium import webdriver

class HelloWorld(unittest.TestCase):
	# Realiza todo lo necesario antes de empezar la prueba
    @classmethod # Decorador para que las distintas paginas corran en una sola pestaña
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path = "./chromedriver")
        driver = cls.driver
		# esperamos 10 seg antes de realizar la siguiente accion
        driver.implicitly_wait(10)

	# Caso de prueba donde realizaremos una serie de acciones para que el navegador las automatice
    def test_hello_world(self):
        driver = self.driver
        driver.get('https://www.montacargasrentaldelvalle.com')

    def visit_wikipedia(self):
        self.driver.get('https://www.wikipedia.com')
        
		
	# Cerramos el navegador una vez terminadas las pruebas
    @classmethod
    def tearDown(cls):
        cls.driver.quit()

if __name__ == "__main__":
	unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'hello-world-report'))