from playwright.sync_api import Page
from digitalizar_propostas.facta.steps.util.data import Data
from time import sleep
from digitalizar_propostas.facta.steps.util.element_identifiers import (
    DADOS_DA_PROPOSTA_PRODUTO,
    DADOS_DA_PROPOSTA_TIPO_DE_OPERACAO,
    DADOS_DA_PROPOSTA_ORGAO_OU_EMPREGADOR,
    DADOS_DA_PROPOSTA_BANCO
)

tipo_de_operacao = {
    'AVERBAÇÃO ANTECIPADA DIGITAL':             '31',
    'CARTÃO CONSIGNADO BENEFÍCIO':              '33',
    'CARTÃO CONSIGNADO BENEFÍCIO (REPR LEGAL)': '36',
    'CARTÃO DIGITAL RMC':                       '11',
    'CARTÃO DIGITAL RMC (REPR LEGAL)':          '38',
    'NOVO DIGITAL':                             '13',
    'NOVO DIGITAL (REPR LEGAL)':                '35',
    'PORTABILIDADE DIGITAL':                    '17',
    'PORTABILIDADE MANUAL DIGITAL':             '28',
    'REFIN CARTÃO DIGITAL':                     '29',
    'REFIN DA PORTABILIDADE DIGITAL':           '18',
    'REFIN DIGITAL':                            '14',
    'REFIN DIGITAL + MARGEM LIVRE':             '32',
    'REFIN RETENCAO DIGITAL':                   '15',
    'PORTABILIDADE + REFIN DA PORTABILIDADE':   '003500'
}

orgao_ou_empregador = {
    'GOVERNO DO ESTADO RS':             '1',
    'INSS':                             '3',
    'SIAPE':                            '15',
    'FACTA FÁCIL - DÉBITO EM CONTA ':   '390',
    'FGTS':                             '20095',
    'IPE - INST PREV DO ESTADO - RS':   '30',
    'MARINHA':                          '23',
    'PREFEITURA DE PORTO ALEGRE - RS':  '10226',
    'DÉBITO EM CONTA - RENEGOCIAÇÃO':   '710',
    'FACTA FÁCIL - DÉBITO EM CONTA':    '390',
    'PODER JUDICIARIO - RS':            '100'
}

def simulador_dados_da_proposta(page: Page, data: Data):
    sleep(5)
    page.locator(DADOS_DA_PROPOSTA_PRODUTO).select_option(data['dados_da_proposta_produto'])
    
    sleep(0.5)
    page.locator(DADOS_DA_PROPOSTA_TIPO_DE_OPERACAO).select_option(tipo_de_operacao[data['dados_da_proposta_tipo_de_operacao']])

    sleep(0.5)
    page.locator(DADOS_DA_PROPOSTA_ORGAO_OU_EMPREGADOR).select_option(orgao_ou_empregador[data['dados_da_proposta_orgao_ou_empregador']])

    sleep(0.5)
    page.locator(DADOS_DA_PROPOSTA_BANCO).select_option('3')
