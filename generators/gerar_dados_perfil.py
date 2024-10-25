from random import choice, randint
from generators.gerar_senha_perfil import gerar_senha_perfil
import os

base_path = os.path.abspath(os.curdir)

def gerar_dados_perfil(genero):

    # Configurando o gênero
    genero = genero.lower()

    # Abrindo o arquivo de nomes
    arquivo_nomes = open(f'{base_path}/armazenamento/nomes/{genero}.txt', 'r', encoding="utf8")
    arquivo_sobrenomes = open(f'{base_path}/armazenamento/sobrenomes/{genero}.txt', 'r', encoding="utf8")

    # Declarando a lista de nomes
    nomes = []
    sobrenomes = []

    # Capturando as linhas do arquivo
    for linha in arquivo_nomes:
        
        # Adicionando o nome na lista de nomes
        nomes.append(linha.split('\n')[0])

    # Capturando as linhas do arquivo
    for linha in arquivo_sobrenomes:
        
        # Adicionando o nome na lista de nomes
        sobrenomes.append(linha.split('\n')[0])

    # Definindo os dados do perfil
    padrao = choice(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
    nome = f'{choice(nomes)} {choice(sobrenomes)} {choice(sobrenomes)}'
    
    # Gerando usuário no padrão 1
    if padrao == '1':
        usuario = nome.lower().replace(' ', '_') + str(randint(10, 99)) + str(choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y']))
    elif padrao == '2':
        usuario = nome.lower().replace(' ', '.') + str(randint(10, 99)) + str(choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y']))
    elif padrao == '3':
        usuario = nome.lower().replace(' ', '') + str(randint(10, 99)) + str(choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y']))
    elif padrao == '4':
        usuario = nome.lower().replace(' ', '_') + str(randint(10, 99)) + str(choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y']))
    elif padrao == '5':
        usuario = nome.lower().replace(' ', '.') + str(randint(10, 99)) + str(choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y']))
    elif padrao == '6':
        usuario = nome.lower().replace(' ', '') + str(randint(10, 99)) + str(choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y']))
    elif padrao == '7':
        usuario = nome.lower().replace(' ', '') + '_'
    elif padrao == '8':
        usuario = '_' + nome.lower().replace(' ', '')
    elif padrao == '9':
        usuario = nome.lower().replace(' ', '') + '_' + str(randint(10, 99)) + str(choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y']))
    elif padrao == '10':
        usuario = '_' + nome.lower().replace(' ', '') + str(randint(10, 99)) + str(choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y']))

    senha = gerar_senha_perfil()

    # Retornando o nome, sobrenome e senha
    return nome, usuario, senha