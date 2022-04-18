# 1 - imports
import pytest
import csv
import  requests

teste_dados_novos_usuarios = [
    ('1', 'juca', 'pirama', 'juca@iterasys.com.br')  # usuario 1
    ('2', 'Agatha', 'agatha@itersys.com.br')  # Usuario 2
]

teste_dados_usuarios_atuais = [
    ('1','George','Bluth','georgebluth@regres.in')  #usuario 1
    ('1', 'janet','Weaver','janet.weaver@regres.in') #ususario2
]







# CRUD / ICAE
# Aplicaçoes       API
# crate            Post   Incluir / Publicar
# Reach /research  Get    Consultar / Pegar
# Update           Put    Atualizar
# Delete           Delete Excluir


@pytest.mark.parametrize('id,nome,sobrenome,email',teste_dados_usuario_atuais)
def testar_dados_usuarios(id,nome,sobrenome,email):  # Funçao que testa algo
    try:
     response =  requests.get(f'https://reqres.in/api/user{id}')



# funçao que faz algo --> Fora do meu computador
# API que vamos fazer o test
# https://reqres.in/api/users/{id}
