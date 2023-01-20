from playwright.sync_api import Page
from steps.util.data import Data
from time import sleep
from steps.util.element_identifiers import (
    DADOS_DO_CLIENTE_CPF,
    DADOS_DO_CLIENTE_DATA_DE_NASCIMENTO,
    DADOS_DO_CLIENTE_NOME_DO_CLIENTE
)

def simulador_dados_do_cliente(page: Page, data: Data):
    sleep(0.5)
    page.locator(DADOS_DO_CLIENTE_CPF).type(data['dados_do_cliente_cpf'])
    
    sleep(0.5)
    page.locator(DADOS_DO_CLIENTE_DATA_DE_NASCIMENTO).type('')
    
    sleep(5)
    page.locator(DADOS_DO_CLIENTE_DATA_DE_NASCIMENTO).type(data['dados_do_cliente_data_de_nascimento'])
    
    sleep(0.5)
    page.locator(DADOS_DO_CLIENTE_NOME_DO_CLIENTE).type(data['dados_do_cliente_nome_do_cliente'])