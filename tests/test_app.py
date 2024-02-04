from selenium import webdriver
from time import sleep
import pytest
import subprocess
from selenium.webdriver.common.by import By
import os


@pytest.fixture
def driver():
    # Iniciar o Streamlit em background
    process = subprocess.Popen(["streamlit", "run", "src/app.py"])

    # inicair o Webdriver Usando o GeckoDriver
    driver = webdriver.Chrome(0)
    driver.set_page_load_timeout(5)
    yield driver

    # Fechar o WebDriver e o Streamlit após o teste
    driver.quit()
    process.kill()


def test_app_opens(driver):
    # Verificar se a página abre
    driver.get("http://localhost:8501")
    sleep(5)


def test_check_title_is(driver):
    # Verificar se a página abre
    driver.get("http://localhost:8501")
    sleep(5)
    # vrifica se o titulo da página é
    # capturar o titulo da página
    page_title = driver.title

    #verificar se o titulo da página é o esperado
    expected_title = "Validador de schema excel" # Substitua com o título real esperado
    assert page_title == expected_title


def test_check_streamlit_h1(driver):
    # Acessar a página do Streamlite
    driver.get("http://localhost:8501")
    # Aguardar para garantir que página foi carregada
    sleep(5)

    # Capiturar o o primeiro elemento <h1> da página
    h1_element = driver.find_element(By.TAG_NAME, "h1")

    # Verificar se o texto do elemento <h1> da página
    expect_text = "Insira o seu excel para validação"
    assert h1_element.text == expect_text


def test_check_usuario_pode_inserir_um_excel_e_receber_uma_mensagem(driver):
    # Acessar a página do Streamlite
    driver.get("http://localhost:8501")
    # Aguardar para garantir que página foi carregada
    sleep(5)

    # Realizar o upload do arquivo de sucesso
    sucess_file_path = os.path.abspath("data/arquivo_excel.xlsx")
    driver.find_element(By.CSS_SELECTOR, 'input[type="file"]').send_keys(sucess_file_path)

    # Aguagardar a mensagem de sucesso
    sleep(5)
    assert "O schema do arquivo está correto!! " in driver.page_source



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







