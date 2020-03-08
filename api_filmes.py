import requests
import json

req = None

def requisicao(titulo):
    try:
        req = requests.get(
            'http://www.omdbapi.com/?i=tt3896198&apikey=90a40071&t={}'.format(titulo))
        dicionario = json.loads(req.text)
        return dicionario
    except:
        print('Erro na conexão')
        return None

def printar_detalhes(filme):
    print('Título: {}'.format(filme['Title']))
    print('Ano: {}'.format(filme['Year']))
    print('Diretor: {}'.format(filme['Director']))
    print('Atores: {}'.format(filme['Actors']))
    print('Nota: {}'.format(filme['imdbRating']))

sair = False
while not sair:
    op = input('Escreva o nome de um filme ou SAIR para fechar: ')

    if op == 'SAIR':
        sair = True
        print('Saindo...')
    else:
        filme = requisicao(op)
        if filme['Response'] == 'False':
            print('Filme não encontrado')
        else:
            printar_detalhes(filme)