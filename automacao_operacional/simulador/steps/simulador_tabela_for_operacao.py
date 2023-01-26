from playwright.sync_api import Page
from simulador.steps.util.data import Data

def simulador_tabela_for_operacao(page: Page, data: Data):
    i = 1
    while True:
        TABLE_ID = f'#myTable > tbody > tr:nth-child({i}) > td:nth-child(2)'

        row = page.evaluate('(TABLE_ID) => document.querySelector(TABLE_ID)', TABLE_ID)
        if row == None:
            print('#00')
            break

        if data['codigo_especie'] == '32':
            print('#01')
            table_name = page.evaluate('(TABELA_ID) => document.querySelector(TABELA_ID).innerHTML', TABLE_ID)

            if table_name == '39985 - SMART Especial Novo PN':
                print('#02')
                page.click(TABLE_ID)
                break
        i += 1