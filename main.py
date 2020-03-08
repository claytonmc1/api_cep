import requests

print('###################')
print('### Consulta CEP###')
print('###################')
print()

cep_input = input('Digite o CEP para a consulta: ')

if len(cep_input) != 8:
    print('Quantidade de dígitos inválida!')
    exit()

request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))

address_data = request.json()

if 'erro' not in address_data:
    print('==> CEP ENCONTRADO <==')

    print('CEP: {}'.format(address_data['cep']))
    print('Logradouro: {}'.format(address_data['logradouro']))
    print('Complemento: {}'.format(address_data['complemento']))
    print('Bairro: {}'.format(address_data['bairro']))
else:
    print('{}: CEP inválido.'.format(cep_input))
