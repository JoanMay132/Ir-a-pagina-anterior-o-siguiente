import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class usando_unittest(unittest.TestCase): # Clase que hereda de la clase TestCase   
    def setUp(self): 
        self.driver = webdriver.Chrome(executable_path=r"D:\Descargas\chromedriver_win32\chromedriver.exe") # Inicializamos el driver
    
    def test_pagina_siguiente_o_anterior(self): # Método que contiene las acciones a realizar
        driver = self.driver
        driver.get("https://wwww.facebook.com") # Abrimos la página
        time.sleep(3)
        driver.get("https://www.google.com") # Abrimos la página
        time.sleep(3)
        driver.get("https://www.youtube.com") # Abrimos la página
        time.sleep(3)
        driver.back() #regresar a pagina anterior 
        time.sleep(3)
        driver.back #regresar a pagina anterior
        time.sleep(3)
        driver.forward() #ir a pagina siguiente

if __name__=='__main__': # Método principal
    unittest.main() # Ejecuta el método main de la clase unittest