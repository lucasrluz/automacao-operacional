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
    VALOR_BENEFICIO_OU_RENDA
)
from simulador.steps.util.citys import citys
from simulador.steps.util.data import Data
from time import sleep

def informacoes_de_contato(page: Page, data: Data):
    sleep(8)

    page.locator(ESTADO_CIVIL).select_option('6') # OUTROS
    page.locator(NOME_DO_PAI_NAO_CONSTA_NO_DOCUMENTO).check() # True
    page.locator(CLIENTE_ILETRADO_OU_IMPOSSIBILITADO_DE_ASSINAR).select_option('N') # NÃO
    page.locator(ESCOLARIDADE).select_option('7')

    # page.locator(BENEFICIO_OU_MATRICULA).fill(data['informacoes_do_beneficio_beneficio_ou_matricula'])
    valor_beneficio_ou_renda = data['informacoes_do_beneficio_valor_beneficio_ou_renda']
    page.evaluate(f'(VALOR_BENEFICIO_OU_RENDA) => document.querySelector(VALOR_BENEFICIO_OU_RENDA).value = {valor_beneficio_ou_renda}', VALOR_BENEFICIO_OU_RENDA)

    page.locator(CEP_INFORMACOES_DE_CONTATO).fill(data['informacoes_de_contato_cep'])
    page.locator(BUTTON_PESQUISAR_CEP).click()

    sleep(1)
    error_cep_not_found: str = page.evaluate('(ERROR_CEP_NOT_FOUND) => document.querySelector(ERROR_CEP_NOT_FOUND)', ERROR_CEP_NOT_FOUND)

    if error_cep_not_found != None:
        print('CEP não encontrado')
        page.locator(ENDERECO_RESIDENCIAL).fill(data['informacoes_de_contato_endereco'])
        page.locator(NUMERO).fill(data['informacoes_de_contato_numero'])
        page.locator(COMPLEMENTO).fill(data['informacoes_de_contato_cemplemento'])
        page.locator(BAIRRO).fill(data['informacoes_de_contato_bairro'])
        page.locator(CIDADE).select_option(citys[data['informacoes_de_contato_cidade']])
        page.locator(TIPO_RESIDENCIA).select_option('3') # ALUGADA
        page.locator(CELULAR).fill(data['informacoes_de_contato_celular'])
        sleep(3)
        return
    
    # Get City, remove after
    # i = 1
    # with open('b.txt', 'w') as f:
    #     while True:
    #         print(i)
    #         id = f'#cidade > option:nth-child({i})'
    #         if page.evaluate('(id) => document.querySelector(id)', id) == None:
    #             break
    #         id = f'#cidade > option:nth-child({i})'

    #         city = page.evaluate('(id) => document.querySelector(id).innerHTML', id)
    #         value = page.evaluate('(id) => document.querySelector(id).value', id)

    #         f.write(f"'{city}': '{value}',")
    #         f.write('\n')

    #         i += 1

