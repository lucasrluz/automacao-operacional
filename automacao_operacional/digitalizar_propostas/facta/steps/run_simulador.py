from playwright.sync_api import Page
from .simulador.simulador_dados_da_proposta import simulador_dados_da_proposta
from .simulador.simulador_dados_do_cliente import simulador_dados_do_cliente
from .simulador.simulador_dados_da_simulacao import simulador_dados_da_simulacao
from .simulador.simulador_tabela_for_operacao import simulador_tabela_for_operacao
from .util.data import Data

def run_simulador(page: Page, data: Data):
    # Dados da Proposta
    simulador_dados_da_proposta(page, data)
    
    # Dados do Cliente
    simulador_dados_do_cliente(page, data)

    # Dados da Simulação
    simulador_dados_da_simulacao(page, data)

    # Selecionar tabelas
    simulador_tabela_for_operacao(page, data)