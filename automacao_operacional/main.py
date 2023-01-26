from playwright.sync_api import Playwright, sync_playwright, Page
from dotenv import load_dotenv
from simulador.steps.login import login
from simulador.steps.proposta_simulador import proposta_simulador
from yuppie.steps.yuppie_login import yupie_login
from yuppie.steps.propostas import propostas
from yuppie.steps.util.proposta_data import PropostaData
from time import sleep
from simulador.steps.util.data import Data

load_dotenv()

def set_data(proposta_data: PropostaData, page: Page):
    tipo_de_operacao = ''
    valor_solicitado = ''

    print(proposta_data['proposta_dados_para_liberacao']['proposta_dados_para_liberacao_tipo'])
    # if proposta_data['proposta_dados_para_liberacao']['proposta_dados_para_liberacao_tipo'] == 'NOVO':
    #     tipo_de_operacao = 'NOVO DIGITAL'

    # remover depois
    tipo_de_operacao = 'NOVO DIGITAL'

    if proposta_data['proposta_dados_para_liberacao']['proposta_dados_para_liberacao_valor_parcela'] != None:
        valor_solicitado = 'Parcela'
    else:
        valor_solicitado = 'Contrato'
    

    simulador_data: Data = {
        'dados_da_proposta_produto': 'D', # Venda Digital
        'dados_da_proposta_tipo_de_operacao': tipo_de_operacao,
        'dados_da_proposta_orgao_ou_empregador': 'INSS',
        'dados_da_proposta_banco': '3', # Facta
        'dados_do_cliente_cpf': proposta_data['proposta_dados_do_tomador']['proposta_dados_do_tomador_cpf'],
        'dados_do_cliente_data_de_nascimento': proposta_data['proposta_dados_do_tomador']['proposta_dados_do_tomador_data_nascimento'],
        'dados_do_cliente_nome_do_cliente': proposta_data['proposta_dados_do_tomador']['proposta_dados_do_tomador_nome'],
        'dados_da_simulacao_informe_o_valor_solicitado': proposta_data['proposta_dados_para_liberacao']['proposta_dados_para_liberacao_valor_parcela'],
        'dados_da_simulacao_valor_solicitado': valor_solicitado,
        'dados_da_simulacao_informe_o_prazo_solicitado': proposta_data['proposta_dados_para_liberacao']['proposta_dados_para_liberacao_prazo'],
        'codigo_especie': proposta_data['proposta_dados_para_liberacao']['proposta_dados_para_liberacao_codigo_especie']
    }

    return simulador_data

def print_dict(value: dict):
    a = value['proposta_dados_do_tomador']
    b = value['proposta_dados_para_liberacao']

    print('Proposta dados do tomador')
    for x, y in a.items():
        print(f'{x}: {y}')

    print(' ')
    print('Proposta dados para liberação')
    for k, v in b.items():
        print(f'{k}: {v}')
 
def main(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, channel='chromium')
    pageOne = browser.new_page()
    pageOne.goto('https://sistemayuppie.com.br/agilizzapromotora/public/auth/login')

    yupie_login(pageOne)

    proposta_data = propostas(pageOne)
    print_dict(proposta_data)

    pageTwo = browser.new_page()
    pageTwo.goto('https://desenv.facta.com.br/sistemaNovo/login.php')
    login(pageTwo)

    simulador_data = set_data(proposta_data, pageTwo)

    sleep(5)
    proposta_simulador(pageTwo, simulador_data)
    
    sleep(10000000)

with sync_playwright() as playwright:
    main(playwright)