from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from time import sleep


# Precisamos definir qual driver vamos utilizar
driver = webdriver.Chrome()

# definir um timeout implicito
driver.set_page_load_timeout(5) # 5 segundos

# vamos fazer uma tratativa de try-except de entrar na nossa página
try:
    driver.get("http://localhost:8501")
    sleep(5)
    print("Acessou a página com sucesso")
except TimeoutException:
    print("Tempo de carregamento da página excedeu o limite")
finally:
    driver.quit()







