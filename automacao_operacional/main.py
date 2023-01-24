from playwright.sync_api import Playwright, sync_playwright
from dotenv import load_dotenv
from simulador.steps.login import login
from simulador.steps.proposta_simulador import proposta_simulador
from yuppie.steps.yuppie_login import yupie_login
from yuppie.steps.propostas import propostas
from yuppie.steps.util.proposta_data import PropostaData
from time import sleep
from simulador.steps.util.data import Data

load_dotenv()

def setData(proposta_data: PropostaData):
    tipo_de_operacao = ''

    print(proposta_data['proposta_dados_para_liberacao']['proposta_dados_para_liberacao_tipo'])
    if proposta_data['proposta_dados_para_liberacao']['proposta_dados_para_liberacao_tipo'] == 'NOVO':
        tipo_de_operacao = 'NOVO DIGITAL'

    # remover depois
    tipo_de_operacao = 'NOVO DIGITAL'

    simulador_data: Data = {
        'dados_da_proposta_produto': 'D',
        'dados_da_proposta_tipo_de_operacao': tipo_de_operacao,
        'dados_da_proposta_orgao_ou_empregador': 'INSS',
        'dados_da_proposta_banco': '3',
        'dados_do_cliente_cpf': proposta_data['proposta_dados_do_tomador']['proposta_dados_do_tomador_cpf'],
        'dados_do_cliente_data_de_nascimento': proposta_data['proposta_dados_do_tomador']['proposta_dados_do_tomador_data_nascimento'],
        'dados_do_cliente_nome_do_cliente': proposta_data['proposta_dados_do_tomador']['proposta_dados_do_tomador_nome'],
        'dados_da_simulacao_informe_o_valor_solicitado': proposta_data['proposta_dados_para_liberacao']['proposta_dados_para_liberacao_valor_parcela'],
        'dados_da_simulacao_valor_solicitado': 'Parcela',
        'dados_da_simulacao_informe_o_prazo_solicitado': proposta_data['proposta_dados_para_liberacao']['proposta_dados_para_liberacao_prazo']
    }

    return simulador_data

# data_for_tests: Data = {
#     'dados_da_proposta_produto': 'D',
#     'dados_da_proposta_tipo_de_operacao': 'NOVO DIGITAL',
#     'dados_da_proposta_orgao_ou_empregador': 'INSS',
#     'dados_da_proposta_banco': '',
#     'dados_do_cliente_cpf': '111.222.333.44',
#     'dados_do_cliente_data_de_nascimento': '19/01/2023',
#     'dados_do_cliente_nome_do_cliente': 'Test1...',
#     'dados_do_representante_legal_cpf': '555.666.777.88',
#     'dados_do_representante_legal_nome': 'Test2...',
#     'dados_da_simulacao_informe_o_valor_solicitado': '100.50',
#     'dados_da_simulacao_valor_solicitado': 'Contrato',
#     'dados_da_simulacao_informe_o_prazo_solicitado': '100'
# }
 
def main(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, channel='chromium')
    pageOne = browser.new_page()
    pageOne.goto('https://sistemayuppie.com.br/agilizzapromotora/public/auth/login')

    yupie_login(pageOne)

    proposta_data = propostas(pageOne)
    print(proposta_data)

    pageTwo = browser.new_page()
    pageTwo.goto('https://desenv.facta.com.br/sistemaNovo/login.php')
    login(pageTwo)

    simulador_data = setData(proposta_data)

    sleep(5)
    proposta_simulador(pageTwo, simulador_data)
    
    sleep(10000000)

with sync_playwright() as playwright:
    main(playwright)