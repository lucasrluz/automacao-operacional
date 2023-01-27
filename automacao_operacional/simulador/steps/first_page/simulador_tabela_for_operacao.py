from playwright.sync_api import Page
from simulador.steps.util.data import Data
from time import sleep
from simulador.steps.util.element_identifiers import (
    ERROR,
    PESQUISAR
)

def simulador_tabela_for_operacao(page: Page, data: Data):
    # Pesquisar tabelas
    sleep(0.5)
    page.locator(PESQUISAR).click()

    sleep(3)

    # Tratamento de erro
    error_test: str = page.evaluate('(ERROR) => document.querySelector(ERROR).innerHTML', ERROR)

    if error_test.strip() == '<td colspan="13">Valor da parcela é inferior ao mínimo permitido.</td>':
        print('Valor da parcela é inferior ao mínimo permitido.')
        return
    elif error_test == '<td valign="top" colspan="9" class="dataTables_empty"><font color="red">Não foram encontradas tabelas para os filtros realizados</font></td>':
        print('Não foram encontradas tabelas para os filtros realizados')
        return
    # sleep(100000)

    # Seleciona tabela para operação
    i = 1
    while True:
        TABLE_ID = f'#myTable > tbody > tr:nth-child({i}) > td:nth-child(2)'

        row = page.evaluate('(TABLE_ID) => document.querySelector(TABLE_ID)', TABLE_ID)
        if row == None:
            break

        if data['codigo_especie'] == '32':
            table_name = page.evaluate('(TABELA_ID) => document.querySelector(TABELA_ID).innerHTML', TABLE_ID)

            if table_name == '39195 - INSS Novo Especial RB':
                page.click(TABLE_ID)
                break
        i += 1