from playwright.sync_api import Page
from digitalizar_propostas.facta.steps.util.element_identifiers import (
    CEP_INFORMACOES_DE_CONTATO,
    BUTTON_PESQUISAR_CEP,
    ENDERECO_RESIDENCIAL,
    NUMERO,
    COMPLEMENTO,
    BAIRRO,
    CIDADE,
    TIPO_RESIDENCIA,
    ESCOLARIDADE,
    BENEFICIO_OU_MATRICULA,
    CELULAR,
    VALOR_BENEFICIO_OU_RENDA
)
from digitalizar_propostas.facta.steps.util.citys import citys
from digitalizar_propostas.facta.steps.util.city_uf import city_uf
from digitalizar_propostas.facta.steps.util.data import Data
from time import sleep

def cadastro_dados_pessoais_informacoes_de_contato(page: Page, data: Data):
    page.locator(ESCOLARIDADE).select_option('7')
    
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