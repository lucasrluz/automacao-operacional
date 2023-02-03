from playwright.sync_api import Playwright, sync_playwright, Page
from dotenv import load_dotenv
from digitalizar_propostas.facta.run_facta import run_facta
from yuppie.steps.yuppie_login import yupie_login
from yuppie.steps.propostas import propostas
from yuppie.steps.util.proposta_data import PropostaData
from time import sleep
from digitalizar_propostas.facta.steps.util.data import Data

load_dotenv()

data: Data = {
    'dados_da_proposta_produto': 'D',
    'dados_da_proposta_tipo_de_operacao': 'NOVO DIGITAL', 
    'dados_da_proposta_orgao_ou_empregador': 'INSS',
    'dados_da_proposta_banco': '3',
    'dados_do_cliente_cpf': '926.507.167-20',
    'dados_do_cliente_data_de_nascimento': '',
    'dados_do_cliente_nome_do_cliente': '',
    'dados_da_simulacao_informe_o_valor_solicitado': '100.00', # 200000 or 2000 
    'dados_da_simulacao_valor_solicitado': 'Parcela',
    'dados_da_simulacao_informe_o_prazo_solicitado': '84', 
    'codigo_especie': '32',
    'informacoes_de_contato_cep': '21931120',
    'informacoes_de_contato_endereco': 'RUA MARAPET',
    'informacoes_de_contato_numero': '2542',
    'informacoes_de_contato_cemplemento': '8675',
    'informacoes_de_contato_bairro': 'JARDIM GUANABARA',
    'informacoes_de_contato_cidade': 'RIO DE JANEIRO',
    'informacoes_de_contato_celular': '(21) 99887-3388',
    'informacoes_do_beneficio_valor_beneficio_ou_renda': '4.503,49',
    'informacoes_do_beneficio_beneficio_ou_matricula': '0464124',
    'informacoes_pessoais_naturalidade_uf': 'SC',
    'informacoes_pessoais_naturalidade': 'FLORIANOPOLIS'
}

def set_data(proposta_data: PropostaData, page: Page):
    tipo_de_operacao = ''
    valor_solicitado = ''
    informe_o_valor_solicitado = ''

    print(proposta_data['proposta_dados_para_liberacao']['proposta_dados_para_liberacao_tipo'])
    # if proposta_data['proposta_dados_para_liberacao']['proposta_dados_para_liberacao_tipo'] == 'NOVO':
    #     tipo_de_operacao = 'NOVO DIGITAL'

    # remover depois
    tipo_de_operacao = 'NOVO DIGITAL'

    if proposta_data['proposta_dados_para_liberacao']['proposta_dados_para_liberacao_valor_parcela'] != '0,00':
        valor_solicitado = 'Parcela'
        informe_o_valor_solicitado = proposta_data['proposta_dados_para_liberacao']['proposta_dados_para_liberacao_valor_parcela']
    else:
        valor_solicitado = 'Contrato'
        informe_o_valor_solicitado = proposta_data['proposta_dados_para_liberacao']['proposta_dados_para_liberacao_valor_bruto']
    

    simulador_data: Data = {
        'dados_da_proposta_produto': 'D', # Venda Digital
        'dados_da_proposta_tipo_de_operacao': tipo_de_operacao,
        'dados_da_proposta_orgao_ou_empregador': 'INSS',
        'dados_da_proposta_banco': '3', # Facta
        'dados_do_cliente_cpf': proposta_data['proposta_dados_do_tomador']['proposta_dados_do_tomador_cpf'],
        'dados_do_cliente_data_de_nascimento': proposta_data['proposta_dados_do_tomador']['proposta_dados_do_tomador_data_nascimento'],
        'dados_do_cliente_nome_do_cliente': proposta_data['proposta_dados_do_tomador']['proposta_dados_do_tomador_nome'],
        'dados_da_simulacao_informe_o_valor_solicitado': informe_o_valor_solicitado,
        'dados_da_simulacao_valor_solicitado': valor_solicitado,
        'dados_da_simulacao_informe_o_prazo_solicitado': proposta_data['proposta_dados_para_liberacao']['proposta_dados_para_liberacao_prazo'],
        'codigo_especie': proposta_data['proposta_dados_para_liberacao']['proposta_dados_para_liberacao_codigo_especie'],
        'informacoes_de_contato_cep': proposta_data['proposta_dados_do_tomador']['proposta_dados_do_tomador_cep']
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
    # pageOne = browser.new_page()
    # pageOne.goto('https://sistemayuppie.com.br/agilizzapromotora/public/auth/login')

    # yupie_login(pageOne)

    # proposta_data = propostas(pageOne)
    # print_dict(proposta_data)

    # simulador_data = set_data(proposta_data, pageTwo)
    
    facta_page = browser.new_page()
    
    run_facta(facta_page, data)
    
    sleep(10000000)

with sync_playwright() as playwright:
    main(playwright)