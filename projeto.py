# chave coordenador
dicionario_coordenador = {1 : "Alisson"}

# chave professor
dicionario_professor = {}

# chave aluno
dicionario_aluno = {}

# funções menu

def menu_adm():
    print('''
    [1] - Coordenador
    [2] - Professor
    [3] - Aluno
    [0] - Sair
    ''')
    adm = input("Escolha uma opção de admin: ")
    return adm

def menu_coordenador():
    print('''
    [1] - Criar turma
    [2] - Editar turma
    [3] - Ver turma
    [4] - Apagar turma
    ''')
    opcao = int(input("Escolha uma opção de admin: "))
    return opcao




def menu_professor():
    print('''
    [1] - Cadastrar novo professor
    [2] - Editar professor cadastrado
    [3] - Ver dados de um professor cadastrado
    [4] - Excluir um professor cadastrado
    [5] - Visualizar as turmas de um professor específico
    [6] - Visualizar os alunos da turma de um professor específico
    [0] - Voltar
    ''')

def menu_aluno():
    print('''
    [1] - Cadastrar novo aluno
    [2] - Editar aluno cadastrado
    [3] - Visualizar alunos cadastrados cadastrados
    [4] - Apagar aluno cadastrado
    [0] - Voltar
    ''')
    return input("Escolha uma opção: ")

def cadastrar_aluno():
    pass

# funções aluno

def cadastrar_aluno():
    pass

def editar_aluno(editar_aluno):
    # verifica se existem alunos cadastrados
    if len(dicionario_aluno) == 0:
        print("Não existem alunos cadastrados")
    else:
        if editar_aluno not in dicionario_aluno:
            print("O aluno não está cadastrado")
        else:
            novo_nome_aluno = input("Digite o nome do aluno: ")
            if novo_nome_aluno.count(' ') < 1 or novo_nome_aluno: # verifica se o nome tem numeros
                print("O nome deve ser composto e não deve conter números")
            else:
                pass


# def cadastro_aluno():
#     aluno = input("Digite o nome do aluno que deseja cadastrar: ")
#     if aluno not in dicionario_aluno:
#         var = dicionario_aluno.get(1, 0)
#         if var == 1:
#             for num_chave in dicionario_aluno.keys():
#             nova_matricula = num_chave + 1
#         if var == 0:
#             nova_matricula = 1
#     else:
#         print("Este aluno já está cadastrado. ")
#         print(30*"=-")




while True:
    # chama a função menu login ou menu principal
    opcao_menu_adm = menu_adm()
    # verifica se o usuario colocou uma 
    if opcao_menu_adm == '1':
        # chamando a função menu coordenador
        opcao_menu_coordenador = menu_coordenador()
        if opcao_menu_coordenador == 1:
            print(dicionario_coordenador)
            print(dicionario_aluno)
            print(dicionario_professor)
        else:
            print("Opção inválida! Digite um opção valida")
    
    elif opcao_menu_adm == '2':
        pass
    
    elif opcao_menu_adm == '3':
        pass
    elif opcao_menu_adm == '0':
        opcao_menu_aluno = menu_aluno()
        if opcao_menu_aluno == '1':
            pass
        elif opcao_menu_aluno == '2':
            print("Digite o nome do aluno que deseja editar: ")
            nome_editar_aluno = input(">>> ")
            editar_aluno(nome_editar_aluno)

        
    else:
        print("Opção inválida! Digite um opção valida")
        print(30 * '=-')
        

