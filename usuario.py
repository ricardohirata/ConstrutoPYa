# funcao que faz algo fora do computador
# API https://reqres.in/api/users/{id}

import pytest
import csv

import requests
from requests import HTTPError

teste_dados_novos_usuarios = [
    (1, 'Juca', 'Pirama', 'juca@iterasys.com.br'),
    (2, 'Agatha', 'Cristie', 'agatha@iterasys.com.br')
]

teste_dados_usuarios_atuais = [
    (1, 'George', 'Bluth', 'george.bluth@reqres.in'),
    (2, 'Janet', 'Weaver', 'janet.weaver@reqres.in')
]

@pytest.mark.parametrize('id, nome, sobrenome, email', teste_dados_usuarios_atuais)
def testar_dados_usuarios(id, nome, sobrenome, email):
    try:
        response = requests.get(f'https://reqres.in/api/users/{id}')
        json_response = response.json()
        id_obtido = json_response['data']['id']
        nome_obtido = json_response['data']['first_name']
        sobrenome_obtido = json_response['data']['last_name']
        email_obtido = json_response['data']['email']

        print(f'id:{id_obtido} - nome: {nome_obtido} - sobrenome: {sobrenome_obtido} - email: {email_obtido}')

        assert id_obtido == id
        assert nome_obtido == nome
        assert sobrenome_obtido == sobrenome
        assert email_obtido == email
    except HTTPError as http_fail:
        print(f'Um erro de http ocorreu: {http_fail}')
    except Exception as fail:
        print(f'Falha inesperada: {fail}')


# Ler csv
def ler_dados_csv():
    teste_dados_csv = []
    try:
        with open('usuarios.csv',newline='') as csv_file:
            dados = csv.reader(csv_file,delimiter=',')
            next(dados)
            for linha in dados:
                teste_dados_csv.append(linha)
        return teste_dados_csv
    except FileNotFoundError:
        print(f'Arquivo nao encontrado: usuarios.csv')
    except Exception as fail:
        print(f'Falha imprevista: {fail}')

@pytest.mark.parametrize('id, nome, sobrenome, email', ler_dados_csv())
def testar_dados_usuarios(id, nome, sobrenome, email):
    try:
        response = requests.get(f'https://reqres.in/api/users/{id}')
        json_response = response.json()
        id_obtido = json_response['data']['id']
        nome_obtido = json_response['data']['first_name']
        sobrenome_obtido = json_response['data']['last_name']
        email_obtido = json_response['data']['email']

        print(f'id:{id_obtido} - nome: {nome_obtido} - sobrenome: {sobrenome_obtido} - email: {email_obtido}')

        assert id_obtido == id
        assert nome_obtido == nome
        assert sobrenome_obtido == sobrenome
        assert email_obtido == email
    except HTTPError as http_fail:
        print(f'Um erro de http ocorreu: {http_fail}')
    except Exception as fail:
        print(f'Falha inesperada: {fail}')