import requests
import json


def consulta_cep(cep):

    # Remove caracteres não numéricos do CEP
    cep = ''.join(filter(str.isdigit, str(cep)))

    # Valida se o CEP tem 8 dígitos
    if len(cep) not in [8, 5, 4]:
        return "CEP inválido. Deve conter 8 dígitos."
    elif len(cep) == 5:
        cep += '000'
    elif len(cep) == 4:
        cep = '0' + cep + '000'

    # Monta a URL da API do ViaCEP
    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados_cep = resposta.json()

        return {
            "cep": dados_cep.get("cep"),
            "logradouro": dados_cep.get("logradouro"),
            "complemento": dados_cep.get("complemento"),
            "bairro": dados_cep.get("bairro"),
            "localidade": dados_cep.get("localidade"),
            "uf": dados_cep.get("uf"),
            "ibge": dados_cep.get("ibge"),
            "gia": dados_cep.get("gia"),
            "ddd": dados_cep.get("ddd"),
            "siafi": dados_cep.get("siafi")
        }
    except requests.exceptions.RequestException as e:
        return f"Erro ao consultar o CEP: {e}"
    except Exception as e:
        return f"Ocorreu um erro: {e}"
