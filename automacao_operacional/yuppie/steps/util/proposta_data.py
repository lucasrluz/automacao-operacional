from typing import TypedDict

class PropostaDadosDoTomador(TypedDict):
    proposta_dados_do_tomador_cpf: str
    proposta_dados_do_tomador_nome: str 
    proposta_dados_do_tomador_identidade_rg: str 
    proposta_dados_do_tomador_orgao_emissor: str
    proposta_dados_do_tomador_data_expedicao: str
    proposta_dados_do_tomador_uf_emissor: str
    proposta_dados_do_tomador_data_nascimento: str
    proposta_dados_do_tomador_naturalidade: str
    proposta_dados_do_tomador_pai: str
    proposta_dados_do_tomador_mae: str
    proposta_dados_do_tomador_conjuge: str 
    proposta_dados_do_tomador_cep: str
    proposta_dados_do_tomador_endereco: str
    proposta_dados_do_tomador_complemento: str 
    proposta_dados_do_tomador_bairro: str
    proposta_dados_do_tomador_cidade: str
    proposta_dados_do_tomador_uf: str
    proposta_dados_do_tomador_email: str 
    proposta_dados_do_tomador_celular: str 
    proposta_dados_do_tomador_fax: str
    proposta_dados_do_tomador_fone_residencial: str 
    proposta_dados_do_tomador_fone_comercial: str
    proposta_dados_do_tomador_senha_contra_ceque: str 
    proposta_dados_do_tomador_possui_repr_legal: str

class PropostaDadosParaLiberacao(TypedDict):
    proposta_dados_para_liberacao_corretor: str # input
    proposta_dados_para_liberacao_subestabelecido: str # select
    proposta_dados_para_liberacao_banco: str # select
    proposta_dados_para_liberacao_tipo: str # select
    proposta_dados_para_liberacao_convenio: str # select
    proposta_dados_para_liberacao_tabela: str # input
    proposta_dados_para_liberacao_data_de_emissao: str #input
    proposta_dados_para_liberacao_prazo: str # input
    proposta_dados_para_liberacao_forma_de_liberacao: str # select
    proposta_dados_para_liberacao_produto: str # select
    proposta_dados_para_liberacao_n_contrato: str # input
    proposta_dados_para_liberacao_n_ade: str # input
    proposta_dados_para_liberacao_valor_bruto: str # input
    proposta_dados_para_liberacao_valor_liquido: str # input
    proposta_dados_para_liberacao_valor_parcela: str # input
    proposta_dados_para_liberacao_saldo_banco: str # input
    proposta_dados_para_liberacao_digitador: str # input
    proposta_dados_para_liberacao_numero_beneficio: str # input
    proposta_dados_para_liberacao_valor_beneficio: str # input
    proposta_dados_para_liberacao_codigo_especie: str # input
    proposta_dados_para_liberacao_banco_do_beneficiado: str # input
    proposta_dados_para_liberacao_agencia_do_beneficiado: str # input
    proposta_dados_para_liberacao_operacao: str # input
    proposta_dados_para_liberacao_conta_do_beneficiado: str # input
    proposta_dados_para_liberacao_recebe_por_cartao: str # select
    proposta_dados_para_liberacao_captador: str # select
    proposta_dados_para_liberacao_midia_de_origem: str # select
    proposta_dados_para_liberacao_formalizacao_agendada: str
    proposta_dados_para_liberacao_hora_agendada: str# input
    proposta_dados_para_liberacao_tipo_formalizacao: str # select
    proposta_dados_para_liberacao_situacao: str # select


class PropostaData(TypedDict):
    proposta_dados_do_tomador: PropostaDadosDoTomador
    proposta_dados_para_liberacao: PropostaDadosParaLiberacao