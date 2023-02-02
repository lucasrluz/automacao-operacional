from playwright.sync_api import Page
from simulador.steps.util.element_identifiers import (
    CEP_INFORMACOES_DE_CONTATO,
    BUTTON_PESQUISAR_CEP,
    ERROR_CEP_NOT_FOUND,
    ESTADO_CIVIL,
    NOME_DO_PAI_NAO_CONSTA_NO_DOCUMENTO,
    CLIENTE_ILETRADO_OU_IMPOSSIBILITADO_DE_ASSINAR,
    ENDERECO_RESIDENCIAL,
    NUMERO,
    COMPLEMENTO,
    BAIRRO,
    CIDADE,
    TIPO_RESIDENCIA,
    ESCOLARIDADE,
    BENEFICIO_OU_MATRICULA,
    CELULAR,
    VALOR_BENEFICIO_OU_RENDA,
    NACIONALIDADE,
    NATURALIDADE,
    VALOR_PRATIMONIAL,
    NATURALIDADE_UF
)
from simulador.steps.util.citys import citys
from simulador.steps.util.city_uf import city_uf
from simulador.steps.util.data import Data
from time import sleep

def informacoes_de_contato(page: Page, data: Data):
    sleep(8)

    page.locator(ESTADO_CIVIL).select_option('6') # OUTROS
    page.locator(NOME_DO_PAI_NAO_CONSTA_NO_DOCUMENTO).check() # True
    page.locator(VALOR_PRATIMONIAL).select_option('1') # Tento faz
    page.locator(CLIENTE_ILETRADO_OU_IMPOSSIBILITADO_DE_ASSINAR).select_option('N') # NÃO
    page.locator(ESCOLARIDADE).select_option('7')

    page.locator(NACIONALIDADE).select_option('1')
    page.locator(NATURALIDADE_UF).select_option(data['informacoes_pessoais_naturalidade_uf'])
    page.locator(NATURALIDADE).select_option(city_uf[data['informacoes_pessoais_naturalidade']])
    
    valor_beneficio_ou_renda = data['informacoes_do_beneficio_valor_beneficio_ou_renda']
    page.evaluate(f'(VALOR_BENEFICIO_OU_RENDA) => document.querySelector(VALOR_BENEFICIO_OU_RENDA).value = "{valor_beneficio_ou_renda}"', VALOR_BENEFICIO_OU_RENDA)
    beneficio_ou_matricula = data['informacoes_do_beneficio_beneficio_ou_matricula']
    page.evaluate(f'(BENEFICIO_OU_MATRICULA) => document.querySelector(BENEFICIO_OU_MATRICULA).value = "{beneficio_ou_matricula}"', BENEFICIO_OU_MATRICULA)
    page.locator(CEP_INFORMACOES_DE_CONTATO).fill(data['informacoes_de_contato_cep'])
    page.locator(BUTTON_PESQUISAR_CEP).click()

    page.locator(ENDERECO_RESIDENCIAL).fill(data['informacoes_de_contato_endereco'])
    page.locator(NUMERO).fill(data['informacoes_de_contato_numero'])
    page.locator(COMPLEMENTO).fill(data['informacoes_de_contato_cemplemento'])
    page.locator(BAIRRO).fill(data['informacoes_de_contato_bairro'])
    page.locator(CIDADE).select_option(citys[data['informacoes_de_contato_cidade']])
    page.locator(TIPO_RESIDENCIA).select_option('3') # ALUGADA
    page.locator(CELULAR).fill(data['informacoes_de_contato_celular'])

    return