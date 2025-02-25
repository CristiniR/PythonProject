# 1 - Importação de pacotes
import json
import pytest

# 2 - Classes

# 3 - Definições (Funções e Métodos)

dados = {}

dados['cliente'] = []
dados['cliente'].append({
    'nome':'Cris',
    'telefone':'47000000000',
    'email':'cris@hotmail.com'
})
dados['cliente'].append({
    'nome':'Di',
    'telefone':'48000000000',
    'email':'di@hotmail.com'
})

def criar_json():
    with open('clientes.json','w') as outfile:
        json.dump(dados,outfile,indent=4)

def ler_json():
    with open('clientes2.json') as outfile:
        dados = json.load(outfile)
        for registro in dados['cliente']:
            print('nome: ' + registro['nome'])
            print('telefone: ' + registro['telefone'])
            print('email: ' + registro['email'])
            print('')

def ler_e_adicionar_json():
    with open('clientes2.json') as outfile:
        dados2 = json.load(outfile)

        temp = []
        for registro in dados['cliente']:
            print('nome: ' + registro['nome'])
            print('telefone: ' + registro['telefone'])
            print('email: ' + registro['email'])
            print('')
            temp.append(
                '\'nome \'' + ':' + '\'' + registro['nome'] + '\',' \
                + '\'telefone \'' + ':' + '\'' + registro['telefone'] + '\',' \
                + '\'email \'' + ':' + '\'' + registro['email'] + '\','
            )

    dados['cliente'].extend(temp)
    print('Lista atualizada')
    print(dados['cliente'])


def testar_criar_json():
    criar_json()
    print(dados['cliente'])

def testar_ler_json():
    print('leitura do json por linha / campo')
    ler_json()
    print(dados['cliente'])

def testar_ler_e_adicionar_json():
    print('Lista atualizada')
    print(dados['cliente'])

