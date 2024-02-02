from selenium import webdriver
from time import sleep
import pytest
import subprocess

@pytest.fixture
def driver():
    # Iniciar o Streamlit em background
    process = subprocess.Popen(["streamlit", "run", "src/app.py"])

    # inicair o Webdriver Usando o GeckoDriver
    driver = webdriver.Chrome()
    driver.set_page_load_timeout(5)
    yield driver

    # Fechar o WebDriver e o Streamlit após o teste
    driver.quit()
    process.kill()


def test_app_opens(driver):
    # Verificar se a página abre
    driver.get("http://localhost:8501")
    sleep(5)

# # Precisamos definir qual driver vamos utilizar
# driver = webdriver.Chrome()

# # definir um timeout implicito
# driver.set_page_load_timeout(5) # 5 segundos

# # vamos fazer uma tratativa de try-except de entrar na nossa página
# try:
#     driver.get("http://localhost:8501")
#     sleep(5)
#     print("Acessou a página com sucesso")
# except TimeoutException:
#     print("Tempo de carregamento da página excedeu o limite")
# finally:
#     driver.quit()







