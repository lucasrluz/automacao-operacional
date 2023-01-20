from playwright.sync_api import Playwright, sync_playwright
from dotenv import load_dotenv
from simulador.steps.login import login
from simulador.steps.proposta_simulador import proposta_simulador
from yuppie.steps.yuppie_login import yupie_login
from yuppie.steps.get_values import get_value
from time import sleep
from simulador.steps.util.data import Data

load_dotenv()

data_for_tests: Data = {
    'dados_da_proposta_produto': 'D',
    'dados_da_proposta_tipo_de_operacao': 'NOVO DIGITAL (REPR LEGAL)',
    'dados_da_proposta_orgao_ou_empregador': 'INSS',
    'dados_da_proposta_banco': '',
    'dados_do_cliente_cpf': '111.222.333.44',
    'dados_do_cliente_data_de_nascimento': '19/01/2023',
    'dados_do_cliente_nome_do_cliente': 'Test1...',
    'dados_do_representante_legal_cpf': '555.666.777.88',
    'dados_do_representante_legal_nome': 'Test2...',
    'dados_da_simulacao_informe_o_valor_solicitado': '100.50',
    'dados_da_simulacao_valor_solicitado': 'Contrato',
    'dados_da_simulacao_informe_o_prazo_solicitado': '100'
}
 
def main(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, channel='chromium')
    page = browser.new_page()
    page.goto('https://sistemayuppie.com.br/agilizzapromotora/public/auth/login')

    yupie_login(page)

    get_value(page)

    #page.goto('https://desenv.facta.com.br/sistemaNovo/login.php')
    #login(page)

    #sleep(5)
    #proposta_simulador(page, data_for_tests)
    
    sleep(10000000)

with sync_playwright() as playwright:
    main(playwright)