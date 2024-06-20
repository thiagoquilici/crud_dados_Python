# Inicializa as estruturas de dados para armazenar as informações das pessoas
pessoas_lista = []  # Lista para armazenar as pessoas
pessoas_dicionario = {}  # Dicionário para mapear CPFs às informações das pessoas

# Função para cadastrar uma pessoa
def cadastrar_pessoa():
    nome = input('Digite o nome: ')
    cpf = input('Digite o CPF: ')
    telefone = input('Digite o telefone: ')
    email = input('Digite o e-mail: ')
    profissao = input('Digite a profissão: ')
    empresa = input('Digite a empresa: ')

    # Adiciona à lista
    pessoas_lista.append((nome, cpf, telefone, email, profissao, empresa))
    # Mapeia o CPF ao dicionário
    pessoas_dicionario[cpf] = {
        'Nome': nome,
        'Telefone': telefone,
        'E-mail': email,
        'Profissão': profissao,
        'Empresa': empresa
    }
    print('Pessoa cadastrada com sucesso!')

# Função para listar todas as pessoas
def listar_pessoas():
    for pessoa in pessoas_lista:
        print(f'Nome: {pessoa[0]}, CPF: {pessoa[1]}')

# Função para buscar informações de uma pessoa pelo CPF
def buscar_pessoa():
    cpf_busca = input('Digite o CPF da pessoa que deseja buscar: ')
    if cpf_busca in pessoas_dicionario:
        pessoa_info = pessoas_dicionario[cpf_busca]
        print(f'Informações da pessoa com CPF {cpf_busca}:')
        for chave, valor in pessoa_info.items():
            print(f'{chave}: {valor}')
    else:
        print('Pessoa não encontrada.')

# Função para atualizar informações de uma pessoa pelo CPF
def atualizar_pessoa():
    cpf_busca = input('Digite o CPF da pessoa que deseja atualizar: ')
    if cpf_busca in pessoas_dicionario:
        pessoa_info = pessoas_dicionario[cpf_busca]
        print(f'Informações atuais da pessoa com CPF {cpf_busca}:')
        for chave, valor in pessoa_info.items():
            print(f'{chave}: {valor}')
        # Atualiza os dados
        pessoa_info['Nome'] = input('Digite o novo nome: ')
        pessoa_info['Telefone'] = input('Digite o novo telefone: ')
        pessoa_info['E-mail'] = input('Digite o novo e-mail: ')
        pessoa_info['Profissão'] = input('Digite a nova profissão: ')
        pessoa_info['Empresa'] = input('Digite a nova empresa: ')
        print('Informações atualizadas com sucesso!')
    else:
        print('Pessoa não encontrada.')

# Função para deletar uma pessoa pelo CPF
def deletar_pessoa():
    cpf_busca = input('Digite o CPF da pessoa que deseja deletar: ')
    if cpf_busca in pessoas_dicionario:
        del pessoas_dicionario[cpf_busca]
        pessoas_lista = [p for p in pessoas_lista if p[1] != cpf_busca]
        print('Pessoa removida com sucesso!')
    else:
        print('Pessoa não encontrada.')

# Loop principal do programa
while True:
    print('''Escolha uma opção:
    1. Cadastrar pessoa
    2. Listar pessoas cadastradas
    3. Buscar pessoa pelo CPF
    4. Atualizar informações de uma pessoa
    5. Deletar pessoa
    6. Sair do programa''')
    opcao = input('Digite o número da opção desejada: ')
    if opcao == '1':
        cadastrar_pessoa()
    elif opcao == '2':
        listar_pessoas()
    elif opcao == '3':
        buscar_pessoa()
    elif opcao == '4':
        atualizar_pessoa()
    elif opcao == '5':
        deletar_pessoa()
    elif opcao == '6':
        print('Programa encerrado.')
        break
    else:
        print('Opção inválida. Tente novamente.')
