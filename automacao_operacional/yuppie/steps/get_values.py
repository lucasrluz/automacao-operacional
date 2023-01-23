from playwright.sync_api import Page
from yuppie.steps.util.proposta_data import PropostaDadosDoTomador, PropostaDadosParaLiberacao, PropostaData
from yuppie.steps.util.element_identifiers import (
    PROPOSTA_DADOS_DO_TOMADOR_CPF, 
    PROPOSTA_DADOS_DO_TOMADOR_NOME, 
    PROPOSTA_DADOS_DO_TOMADOR_IDENTIDADE_RG, 
    PROPOSTA_DADOS_DO_TOMADOR_ORGAO_EMISSOR,
    PROPOSTA_DADOS_DO_TOMADOR_DATA_EXPEDICAO,
    PROPOSTA_DADOS_DO_TOMADOR_UF_EMISSOR,
    PROPOSTA_DADOS_DO_TOMADOR_DATA_NASCIMENTO,
    PROPOSTA_DADOS_DO_TOMADOR_NATURALIDADE,
    PROPOSTA_DADOS_DO_TOMADOR_PAI,
    PROPOSTA_DADOS_DO_TOMADOR_MAE,
    PROPOSTA_DADOS_DO_TOMADOR_CONJUGE, 
    PROPOSTA_DADOS_DO_TOMADOR_CEP,
    PROPOSTA_DADOS_DO_TOMADOR_ENDERECO,
    PROPOSTA_DADOS_DO_TOMADOR_COMPLEMENTO, 
    PROPOSTA_DADOS_DO_TOMADOR_BAIRRO,
    PROPOSTA_DADOS_DO_TOMADOR_CIDADE,
    PROPOSTA_DADOS_DO_TOMADOR_UF,
    PROPOSTA_DADOS_DO_TOMADOR_EMAIL, 
    PROPOSTA_DADOS_DO_TOMADOR_CELULAR, 
    PROPOSTA_DADOS_DO_TOMADOR_FAX,
    PROPOSTA_DADOS_DO_TOMADOR_FONE_RESIDENCIAL, 
    PROPOSTA_DADOS_DO_TOMADOR_FONE_COMERCIAL,
    PROPOSTA_DADOS_DO_TOMADOR_SENHA_CONTRA_CHEQUE, 
    PROPOSTA_DADOS_DO_TOMADOR_POSSUI_REPR_LEGAL,

    PROPOSTA_DADOS_PARA_LIBERACAO_CORRETOR,
    PROPOSTA_DADOS_PARA_LIBERACAO_SUBESTABELECIDO,
    PROPOSTA_DADOS_PARA_LIBERACAO_BANCO,
    PROPOSTA_DADOS_PARA_LIBERACAO_TIPO,
    PROPOSTA_DADOS_PARA_LIBERACAO_CONVENIO,
    PROPOSTA_DADOS_PARA_LIBERACAO_TABELA,
    PROPOSTA_DADOS_PARA_LIBERACAO_DATA_DE_EMISSAO,
    PROPOSTA_DADOS_PARA_LIBERACAO_PRAZO,
    PROPOSTA_DADOS_PARA_LIBERACAO_FORMA_DE_LIBERACAO,
    PROPOSTA_DADOS_PARA_LIBERACAO_PRODUTO,
    PROPOSTA_DADOS_PARA_LIBERACAO_N_CONTRATO,
    PROPOSTA_DADOS_PARA_LIBERACAO_N_ADE,
    PROPOSTA_DADOS_PARA_LIBERACAO_VALOR_BRUTO,
    PROPOSTA_DADOS_PARA_LIBERACAO_VALOR_LIQUIDO,
    PROPOSTA_DADOS_PARA_LIBERACAO_VALOR_PARCELA,
    PROPOSTA_DADOS_PARA_LIBERACAO_SALDO_BANCO,
    PROPOSTA_DADOS_PARA_LIBERACAO_DIGITADOR,
    PROPOSTA_DADOS_PARA_LIBERACAO_NUMERO_BENEFICIO,
    PROPOSTA_DADOS_PARA_LIBERACAO_VALOR_BENEFICIO,
    PROPOSTA_DADOS_PARA_LIBERACAO_CODIGO_ESPECIE,
    PROPOSTA_DADOS_PARA_LIBERACAO_BANCO_DO_BENEFICIADO,
    PROPOSTA_DADOS_PARA_LIBERACAO_AGENCIA_DO_BENEFICIADO,
    PROPOSTA_DADOS_PARA_LIBERACAO_OPERACAO,
    PROPOSTA_DADOS_PARA_LIBERACAO_CONTA_DO_BENEFICIADO,
    PROPOSTA_DADOS_PARA_LIBERACAO_RECEBE_POR_CARTAO,
    PROPOSTA_DADOS_PARA_LIBERACAO_CAPTADOR,
    PROPOSTA_DADOS_PARA_LIBERACAO_MIDIA_DE_ORIGEM,
    PROPOSTA_DADOS_PARA_LIBERACAO_FORMALIZACAO_AGENDADA,
    PROPOSTA_DADOS_PARA_LIBERACAO_HORA_AGENDADA,
    PROPOSTA_DADOS_PARA_LIBERACAO_TIPO_FORMALIZACAO,
    PROPOSTA_DADOS_PARA_LIBERACAO_SITUACAO
)

proposta_data: PropostaData = {}
proposta_dados_do_tomador: PropostaDadosDoTomador = {}
proposta_dados_para_liberacao: PropostaDadosParaLiberacao = {}

def get_values(page: Page):
    proposta_dados_do_tomador['proposta_dados_do_tomador_cpf'] = page.input_value(PROPOSTA_DADOS_DO_TOMADOR_CPF)
    proposta_dados_do_tomador['proposta_dados_do_tomador_nome'] = page.input_value(PROPOSTA_DADOS_DO_TOMADOR_NOME)
    proposta_dados_do_tomador['proposta_dados_do_tomador_identidade_rg'] = page.input_value(PROPOSTA_DADOS_DO_TOMADOR_IDENTIDADE_RG)
    proposta_dados_do_tomador['proposta_dados_do_tomador_orgao_emissor'] = page.input_value(PROPOSTA_DADOS_DO_TOMADOR_ORGAO_EMISSOR)
    proposta_dados_do_tomador['proposta_dados_do_tomador_data_expedicao'] = page.input_value(PROPOSTA_DADOS_DO_TOMADOR_DATA_EXPEDICAO)
    proposta_dados_do_tomador['proposta_dados_do_tomador_uf_emissor'] = page.input_value(PROPOSTA_DADOS_DO_TOMADOR_UF_EMISSOR)
    proposta_dados_do_tomador['proposta_dados_do_tomador_data_nascimento'] = page.input_value(PROPOSTA_DADOS_DO_TOMADOR_DATA_NASCIMENTO)
    proposta_dados_do_tomador['proposta_dados_do_tomador_naturalidade'] = page.input_value(PROPOSTA_DADOS_DO_TOMADOR_NATURALIDADE)
    proposta_dados_do_tomador['proposta_dados_do_tomador_pai'] = page.input_value(PROPOSTA_DADOS_DO_TOMADOR_PAI)
    proposta_dados_do_tomador['proposta_dados_do_tomador_mae'] = page.input_value(PROPOSTA_DADOS_DO_TOMADOR_MAE)
    proposta_dados_do_tomador['proposta_dados_do_tomador_conjuge'] = page.input_value(PROPOSTA_DADOS_DO_TOMADOR_CONJUGE)
    proposta_dados_do_tomador['proposta_dados_do_tomador_cep'] = page.input_value(PROPOSTA_DADOS_DO_TOMADOR_CEP)
    proposta_dados_do_tomador['proposta_dados_do_tomador_endereco'] = page.input_value(PROPOSTA_DADOS_DO_TOMADOR_ENDERECO)
    proposta_dados_do_tomador['proposta_dados_do_tomador_complemento'] = page.input_value(PROPOSTA_DADOS_DO_TOMADOR_COMPLEMENTO)
    proposta_dados_do_tomador['proposta_dados_do_tomador_bairro'] = page.input_value(PROPOSTA_DADOS_DO_TOMADOR_BAIRRO)
    proposta_dados_do_tomador['proposta_dados_do_tomador_cidade'] = page.input_value(PROPOSTA_DADOS_DO_TOMADOR_CIDADE)
    proposta_dados_do_tomador['proposta_dados_do_tomador_uf'] = page.input_value(PROPOSTA_DADOS_DO_TOMADOR_UF)
    proposta_dados_do_tomador['proposta_dados_do_tomador_email'] = page.input_value(PROPOSTA_DADOS_DO_TOMADOR_EMAIL)
    proposta_dados_do_tomador['proposta_dados_do_tomador_celular'] = page.input_value(PROPOSTA_DADOS_DO_TOMADOR_CELULAR)
    proposta_dados_do_tomador['proposta_dados_do_tomador_fax'] = page.input_value(PROPOSTA_DADOS_DO_TOMADOR_FAX)
    proposta_dados_do_tomador['proposta_dados_do_tomador_fone_residencial'] = page.input_value(PROPOSTA_DADOS_DO_TOMADOR_FONE_RESIDENCIAL)
    proposta_dados_do_tomador['proposta_dados_do_tomador_fone_comercial'] = page.input_value(PROPOSTA_DADOS_DO_TOMADOR_FONE_COMERCIAL)
    proposta_dados_do_tomador['proposta_dados_do_tomador_senha_contra_ceque'] = page.input_value(PROPOSTA_DADOS_DO_TOMADOR_SENHA_CONTRA_CHEQUE)
    proposta_dados_do_tomador['proposta_dados_do_tomador_possui_repr_legal'] = page.is_checked(PROPOSTA_DADOS_DO_TOMADOR_POSSUI_REPR_LEGAL)

    proposta_dados_para_liberacao['proposta_dados_para_liberacao_corretor'] = page.input_value(PROPOSTA_DADOS_PARA_LIBERACAO_CORRETOR)
    proposta_dados_para_liberacao['proposta_dados_para_liberacao_subestabelecido'] = page.input_value(PROPOSTA_DADOS_PARA_LIBERACAO_SUBESTABELECIDO)
    proposta_dados_para_liberacao['proposta_dados_para_liberacao_banco'] = page.input_value(PROPOSTA_DADOS_PARA_LIBERACAO_BANCO)
    proposta_dados_para_liberacao['proposta_dados_para_liberacao_tipo'] = page.input_value(PROPOSTA_DADOS_PARA_LIBERACAO_TIPO)
    proposta_dados_para_liberacao['proposta_dados_para_liberacao_convenio'] = page.input_value(PROPOSTA_DADOS_PARA_LIBERACAO_CONVENIO)
    proposta_dados_para_liberacao['proposta_dados_para_liberacao_tabela'] = page.input_value(PROPOSTA_DADOS_PARA_LIBERACAO_TABELA)
    proposta_dados_para_liberacao['proposta_dados_para_liberacao_data_de_emissao'] = page.input_value(PROPOSTA_DADOS_PARA_LIBERACAO_DATA_DE_EMISSAO)
    proposta_dados_para_liberacao['proposta_dados_para_liberacao_prazo'] = page.input_value(PROPOSTA_DADOS_PARA_LIBERACAO_PRAZO)
    proposta_dados_para_liberacao['proposta_dados_para_liberacao_forma_de_liberacao'] = page.input_value(PROPOSTA_DADOS_PARA_LIBERACAO_FORMA_DE_LIBERACAO)
    proposta_dados_para_liberacao['proposta_dados_para_liberacao_produto'] = page.input_value(PROPOSTA_DADOS_PARA_LIBERACAO_PRODUTO)
    proposta_dados_para_liberacao['proposta_dados_para_liberacao_n_contrato'] = page.input_value(PROPOSTA_DADOS_PARA_LIBERACAO_N_CONTRATO)
    proposta_dados_para_liberacao['proposta_dados_para_liberacao_n_ade'] = page.input_value(PROPOSTA_DADOS_PARA_LIBERACAO_N_ADE)
    proposta_dados_para_liberacao['proposta_dados_para_liberacao_valor_bruto'] = page.input_value(PROPOSTA_DADOS_PARA_LIBERACAO_VALOR_BRUTO)
    proposta_dados_para_liberacao['proposta_dados_para_liberacao_valor_liquido'] = page.input_value(PROPOSTA_DADOS_PARA_LIBERACAO_VALOR_LIQUIDO)
    proposta_dados_para_liberacao['proposta_dados_para_liberacao_valor_parcela'] = page.input_value(PROPOSTA_DADOS_PARA_LIBERACAO_VALOR_PARCELA)
    proposta_dados_para_liberacao['proposta_dados_para_liberacao_saldo_banco'] = page.input_value(PROPOSTA_DADOS_PARA_LIBERACAO_SALDO_BANCO)
    proposta_dados_para_liberacao['proposta_dados_para_liberacao_digitador'] = page.input_value(PROPOSTA_DADOS_PARA_LIBERACAO_DIGITADOR)
    proposta_dados_para_liberacao['proposta_dados_para_liberacao_numero_beneficio'] = page.input_value(PROPOSTA_DADOS_PARA_LIBERACAO_NUMERO_BENEFICIO)
    proposta_dados_para_liberacao['proposta_dados_para_liberacao_valor_beneficio'] = page.input_value(PROPOSTA_DADOS_PARA_LIBERACAO_VALOR_BENEFICIO)
    proposta_dados_para_liberacao['proposta_dados_para_liberacao_codigo_especie'] = page.input_value(PROPOSTA_DADOS_PARA_LIBERACAO_CODIGO_ESPECIE)
    proposta_dados_para_liberacao['proposta_dados_para_liberacao_banco_do_beneficiado'] = page.input_value(PROPOSTA_DADOS_PARA_LIBERACAO_BANCO_DO_BENEFICIADO)
    proposta_dados_para_liberacao['proposta_dados_para_liberacao_agencia_do_beneficiado'] = page.input_value(PROPOSTA_DADOS_PARA_LIBERACAO_AGENCIA_DO_BENEFICIADO)
    proposta_dados_para_liberacao['proposta_dados_para_liberacao_operacao'] = page.input_value(PROPOSTA_DADOS_PARA_LIBERACAO_OPERACAO)
    proposta_dados_para_liberacao['proposta_dados_para_liberacao_conta_do_beneficiado'] = page.input_value(PROPOSTA_DADOS_PARA_LIBERACAO_CONTA_DO_BENEFICIADO)
    proposta_dados_para_liberacao['proposta_dados_para_liberacao_recebe_por_cartao'] = page.input_value(PROPOSTA_DADOS_PARA_LIBERACAO_RECEBE_POR_CARTAO)
    proposta_dados_para_liberacao['proposta_dados_para_liberacao_captador'] = page.input_value(PROPOSTA_DADOS_PARA_LIBERACAO_CAPTADOR)
    proposta_dados_para_liberacao['proposta_dados_para_liberacao_midia_de_origem'] = page.input_value(PROPOSTA_DADOS_PARA_LIBERACAO_MIDIA_DE_ORIGEM)
    proposta_dados_para_liberacao['proposta_dados_para_liberacao_formalizacao_agendada'] = page.input_value(PROPOSTA_DADOS_PARA_LIBERACAO_FORMALIZACAO_AGENDADA)
    proposta_dados_para_liberacao['proposta_dados_para_liberacao_hora_agendada'] = page.input_value(PROPOSTA_DADOS_PARA_LIBERACAO_HORA_AGENDADA)
    proposta_dados_para_liberacao['proposta_dados_para_liberacao_tipo_formalizacao'] = page.input_value(PROPOSTA_DADOS_PARA_LIBERACAO_TIPO_FORMALIZACAO)
    proposta_dados_para_liberacao['proposta_dados_para_liberacao_situacao'] = page.input_value(PROPOSTA_DADOS_PARA_LIBERACAO_SITUACAO)

    proposta_data['proposta_dados_do_tomador'] = proposta_dados_do_tomador
    proposta_data['proposta_dados_para_liberacao'] = proposta_dados_para_liberacao
    
    return proposta_data