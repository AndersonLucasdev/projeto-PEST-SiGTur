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
    adm = input("Escolha uma opção de admin: ").strip()
    return adm

def menu_coordenador():
    print('''
    [1] - Criar turma
    [2] - Editar turma
    [3] - Ver turma
    [4] - Apagar turma
    ''')
    opcao = int(input("Escolha uma opção de admin: ")).strip()
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


# funções aluno


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

def cadastro_aluno(aluno):
    if aluno not in dicionario_aluno:
        if dicionario_aluno:
            nova_matricula = max(dicionario_aluno.keys()) + 1
        else:
            nova_matricula = 1
        dicionario_aluno[nova_matricula] = aluno
    else:
        print("Este aluno já está cadastrado.")
        print(30 * "=-")


def editar_aluno(matricula):
    flag_dicionario = verifica_dicionario_aluno(matricula, dicionario_aluno)
    if flag_dicionario == True:
        print("Digite o novo nome do aluno: ")
        novo_nome_aluno = input(">>> ").strip().lower()
        flag_nome = verifica_nome_aluno(novo_nome_aluno)
        if flag_nome == True:
            dicionario_aluno[matricula] = novo_nome_aluno
            print("Aluno editado com sucesso!")
    else:
        return flag_dicionario

def visualizar_alunos():
    if len(dicionario_aluno) == 0:
        print("Não há alunos cadastrados!")
    else:
        print(dicionario_aluno)

def excluir_aluno(matricula):
    flag_dicionario = verifica_dicionario_aluno(matricula, dicionario_aluno)
    if flag_dicionario == True:
            del dicionario_aluno[matricula]
            print("Aluno excluido com sucesso!")


## funções de verificação do aluno
def verifica_dicionario_aluno(matricula, dicionario):
    if len(dicionario) == 0:
        print("Não existem alunos cadastrados")
    else:
        if matricula in dicionario:
            return True
        else:
            print("O aluno não está cadastrado!")

def verifica_nome_aluno(nome_aluno):
    if nome_aluno.count(' ') < 1 or nome_aluno.isnumeric():
        print("O nome deve ser composto e não deve conter números")
    else:
        return True

## codigo principal

while True:
    # chama a função menu login ou menu principal
    opcao_menu_adm = menu_adm()
    # verifica se o usuario colocou uma 
    if opcao_menu_adm == '1':
        # chamando a função menu coordenador
        opcao_menu_coordenador = menu_coordenador()
        if opcao_menu_coordenador == 1:
            print(dicionario_aluno)
            print(dicionario_professor)
        else:
            print("Opção inválida! Digite um opção valida")
    
    elif opcao_menu_adm == '2':
        while True:
            pass
    
    elif opcao_menu_adm == '3':
        while True:
            opcao_menu_aluno = menu_aluno()
            ## cadastrar aluno
            if opcao_menu_aluno == '1':
                print("Digite o nome do aluno que deseja cadastrar: ")
                nome_aluno = input(">>> ").strip().capitalize()
                cadastro_aluno(nome_aluno)
            ## editar aluno
            elif opcao_menu_aluno == '2':
                print("Digite a matricula do aluno que deseja editar: ")
                matricula_editar_aluno = int(input(">>> "))
                editar_aluno(matricula_editar_aluno)
            ## visualizar alunos
            elif opcao_menu_aluno == '3':
                visualizar_alunos()
            elif opcao_menu_aluno == '4':
                print("Digite a matricula do aluno que deseja excluir: ")
                matricula_excluir_aluno = int(input(">>> "))
                excluir_aluno(matricula_excluir_aluno)
            elif opcao_menu_aluno == '0':
                break
    elif opcao_menu_adm == '0':
        break
    else:
        print("Opção inválida! Digite um opção valida")
        print(30 * '=-')
        

