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
    ESCOLARIDADE
)
from simulador.steps.util.data import Data
from time import sleep

def informacoes_de_contato(page: Page, data: Data):
    sleep(8)

    page.locator(ESTADO_CIVIL).select_option('6') # OUTROS
    page.locator(NOME_DO_PAI_NAO_CONSTA_NO_DOCUMENTO).check() # True
    page.locator(CLIENTE_ILETRADO_OU_IMPOSSIBILITADO_DE_ASSINAR).select_option('N') # NÃO
    page.locator(ESCOLARIDADE).select_option('7')

    page.locator(CEP_INFORMACOES_DE_CONTATO).fill(data['informacoes_de_contato_cep'])

    page.locator(BUTTON_PESQUISAR_CEP).click()

    sleep(2)
    error_cep_not_found: str = page.evaluate('(ERROR_CEP_NOT_FOUND) => document.querySelector(ERROR_CEP_NOT_FOUND)', ERROR_CEP_NOT_FOUND)
    if error_cep_not_found != None:
        print('CEP não encontrado')
        page.locator(ENDERECO_RESIDENCIAL).fill(data['informacoes_de_contato_endereco'])
        page.locator(NUMERO).fill(data['informacoes_de_contato_numero'])
        page.locator(COMPLEMENTO).fill(data['informacoes_de_contato_cemplemento'])
        page.locator(BAIRRO).fill(data['informacoes_de_contato_bairro'])
        # page.locator(CIDADE).fill(data['informacoes_de_contato_cidade'])
        # page.locator(TIPO_RESIDENCIA).fill('3') # ALUGADA
        # return
    
    # Get City, remove after
    i = 1
    with open('b.txt', 'w') as f:
        while True:
            print(i)
            id = f'#cidade > option:nth-child({i})'
            if page.evaluate('(id) => document.querySelector(id)', id) == None:
                break
            id = f'#cidade > option:nth-child({i})'

            city = page.evaluate('(id) => document.querySelector(id).innerHTML', id)
            value = page.evaluate('(id) => document.querySelector(id).value', id)

            f.write(f"'{city}': '{value}'")
            f.write('\n')

            i += 1

