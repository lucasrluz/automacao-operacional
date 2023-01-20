from playwright.sync_api import Page
from steps.util.data import Data
from .util.element_identifiers import (
    PROPOSTA_SIMULADOR,
    DADOS_DA_PROPOSTA_PRODUTO,
    DADOS_DA_PROPOSTA_TIPO_DE_OPERACAO,
    DADOS_DA_PROPOSTA_ORGAO_OU_EMPREGADOR,
    DADOS_DA_PROPOSTA_BANCO,
    DADOS_DO_CLIENTE_CPF,
    DADOS_DO_CLIENTE_DATA_DE_NASCIMENTO,
    DADOS_DO_CLIENTE_NOME_DO_CLIENTE,
    DADOS_DO_REPRESENTANTE_LEGAL_CPF,
    DADOS_DO_REPRESENTANTE_LEGAL_NOME,
    DADOS_DA_SIMULACAO_INFORME_O_VALOR_SOLICITADO,
    DADOS_DA_SIMULACAO_VALOR_SOLICITADO,
    DADOS_DA_SIMULACAO_INFORME_O_PRAZO_SOLICITADO,
    PESQUISAR
)

from time import sleep

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

valor_solicitado = {
    'Contrato': '1',
    'Parcela': '2'
}


def proposta_simulador(page: Page, data: Data):
    page.evaluate('(PROPOSTA_SIMULADOR) => document.querySelector(PROPOSTA_SIMULADOR).click()', PROPOSTA_SIMULADOR)

    # Dados da Proposta
    sleep(5)
    page.locator(DADOS_DA_PROPOSTA_PRODUTO).select_option(data['dados_da_proposta_produto'])
    
    sleep(0.5)
    page.locator(DADOS_DA_PROPOSTA_TIPO_DE_OPERACAO).select_option(tipo_de_operacao[data['dados_da_proposta_tipo_de_operacao']])

    sleep(0.5)
    page.locator(DADOS_DA_PROPOSTA_ORGAO_OU_EMPREGADOR).select_option(orgao_ou_empregador[data['dados_da_proposta_orgao_ou_empregador']])

    sleep(0.5)
    page.locator(DADOS_DA_PROPOSTA_BANCO).select_option('3')

    # Dados do Cliente
    sleep(0.5)
    page.locator(DADOS_DO_CLIENTE_CPF).type(data['dados_do_cliente_cpf'])
    
    sleep(0.5)
    page.locator(DADOS_DO_CLIENTE_DATA_DE_NASCIMENTO).type('')
    
    sleep(5)
    page.locator(DADOS_DO_CLIENTE_DATA_DE_NASCIMENTO).type(data['dados_do_cliente_data_de_nascimento'])
    
    sleep(0.5)
    page.locator(DADOS_DO_CLIENTE_NOME_DO_CLIENTE).type(data['dados_do_cliente_nome_do_cliente'])

    # Dados do Representante Legal

    sleep(0.5)
    page.locator(DADOS_DO_REPRESENTANTE_LEGAL_CPF).type(data['dados_do_representante_legal_cpf'])

    sleep(0.5)
    page.locator(DADOS_DO_REPRESENTANTE_LEGAL_NOME).type(data['dados_do_representante_legal_nome'])

    # Dados da Simulação
    sleep(0.5)
    page.locator(DADOS_DA_SIMULACAO_INFORME_O_VALOR_SOLICITADO).type(data['dados_da_simulacao_informe_o_valor_solicitado'])

    sleep(0.5)
    page.locator(DADOS_DA_SIMULACAO_VALOR_SOLICITADO).select_option(valor_solicitado[data['dados_da_simulacao_valor_solicitado']])

    sleep(0.5)
    page.locator(DADOS_DA_SIMULACAO_INFORME_O_PRAZO_SOLICITADO).type(data['dados_da_simulacao_informe_o_prazo_solicitado'])

    sleep(0.5)
    page.locator(PESQUISAR).click()