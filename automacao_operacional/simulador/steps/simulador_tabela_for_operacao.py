from playwright.sync_api import Page
from simulador.steps.util.data import Data
from time import sleep
from simulador.steps.util.element_identifiers import (
    ERROR_MESSAGE_ONE,
    ERROR_MESSAGE_TWO,
    PESQUISAR
)

def simulador_tabela_for_operacao(page: Page, data: Data):
    # Pesquisar tabelas
    sleep(0.5)
    page.locator(PESQUISAR).click()

    sleep(2)

    # Tratamento de erro
    errorOne = page.evaluate('(ERROR_MESSAGE_ONE) => document.querySelector(ERROR_MESSAGE_ONE)', ERROR_MESSAGE_ONE)
    if errorOne != None:
        if errorOne.innerHTML == 'Não foram encontradas tabelas para os filtros realizados':
            return print('Error: Não foram encontradas tabelas para os filtros realizados')
    
    # Tratamento de erro
    errorTwo = page.evaluate('(ERROR_MESSAGE_TWO) => document.querySelector(ERROR_MESSAGE_TWO)', ERROR_MESSAGE_TWO)
    if errorTwo != None:
        if errorTwo.innerHTML == 'Valor da parcela é inferior ao mínimo permitido.':
            return print('Valor da parcela é inferior ao mínimo permitido.')

    # Seleciona tabela para operação
    i = 1
    while True:
        TABLE_ID = f'#myTable > tbody > tr:nth-child({i}) > td:nth-child(2)'

        row = page.evaluate('(TABLE_ID) => document.querySelector(TABLE_ID)', TABLE_ID)
        if row == None:
            break

        if data['codigo_especie'] == '32':
            table_name = page.evaluate('(TABELA_ID) => document.querySelector(TABELA_ID).innerHTML', TABLE_ID)

            if table_name == '39985 - SMART Especial Novo PN':
                page.click(TABLE_ID)
                break
        i += 1