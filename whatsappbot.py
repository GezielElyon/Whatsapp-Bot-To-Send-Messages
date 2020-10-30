# Importar as bibliotecas
from selenium import webdriver # Simular o uso do navegador através da automação web
import time
from webdriver_manager.chrome import ChromeDriverManager # Gerenciador do Chrome
from selenium.webdriver.common.keys import Keys # Para poder usar o enter

# Navegar até o whatsapp web
driver = webdriver.Chrome(ChromeDriverManager().install()) # Configurações do WebDriver
driver.get('https://web.whatsapp.com/')
time.sleep(15) # Para dar tempo de escanear o QR Code do whatsapp web

# Definir contatos e grupos e mensagens a ser enviada
contacts = ['Fulano']
message = 'Olá, eu sou um robô!'

# Buscar contatos/grupos
def search_contact(contact):
    search_field = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(3)
    search_field.click()
    search_field.send_keys(contact)
    search_field.send_keys(Keys.ENTER)

# Enviar mensagens para contatos/grupos
def send_message(message):
    send_field = driver.find_elements_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
    send_field[1].click()
    time.sleep(3)
    send_field[1].send_keys(message)
    send_field[1].send_keys(Keys.ENTER)

# Selecionar pessoas e enviar mensagens
for contact in contacts:
    search_contact(contact)
    send_message(message)
