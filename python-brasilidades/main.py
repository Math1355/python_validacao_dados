import requests
from acesso_cep import BuscaEndereco

cep = "06286110"
objeto_cep = BuscaEndereco(cep)

#r = requests.get("https://viacep.com.br/ws/01001000/json/")
#print(type(r.text))
#<Response [200]> e positivo

bairro, cidade, uf = objeto_cep.acessa_via_cep()

print(bairro, cidade, uf)