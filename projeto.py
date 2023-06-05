# chave coordenador
dicionario_coordenador = {}

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
def cadastro(dicionario, nome):
    flag_dicionario = verifica_nome(nome)
    if flag_dicionario == True:
        if dicionario:
            matricula = max(dicionario.keys()) + 1
        else:
            matricula = 1
        dicionario[matricula] = nome


def editar(matricula, dicionario):
    flag_dicionario = verifica_dicionario(matricula, dicionario)
    if flag_dicionario == True:
        print("Digite o novo nome do aluno: ")
        novo_nome_aluno = input(">>> ").strip().capitalize()
        flag_nome = verifica_nome(novo_nome_aluno)
        if flag_nome == True:
            dicionario_aluno[matricula] = novo_nome_aluno
            print("Aluno editado com sucesso!")
    else:
        return flag_dicionario

def visualizar(dicionario):
    if len(dicionario) == 0:
        print("Não há alunos cadastrados!")
    else:
        print(f"{'Matrícula':<10} | {'Nome do aluno':<25}")
        for matricula_id, aluno in dicionario.items():
            print(f"{matricula_id:<10} | {aluno:<25}")

def excluir(matricula, dicionario):
    flag_dicionario = verifica_dicionario(matricula, dicionario)
    if flag_dicionario == True:
        del dicionario[matricula]
        print("Excluido com sucesso!")


## funções de verificação do aluno
def verifica_dicionario(matricula, dicionario):
    if len(dicionario) == 0:
        print("Não existem pessoas cadastrados.")
    else:
        if matricula in dicionario:
            return True
        else:
            print("A pessoa não está cadastrado!")

def verifica_nome(nome_aluno):
    flag =  True
    if ' ' in nome_aluno:
        lista_aluno = nome_aluno.split(" ")
        for elemento in lista_aluno:
            if elemento.isalpha() == False:
                flag = False
            else:
                print("O nome deve ser composto e não deve conter números.")
        if flag == True:
            return True
    else:
        print("O nome deve ser composto e não deve conter números.")

## funções professor
def visualizar_professor(nome, dicionario):
    flag_verifica = verifica_dicionario(nome, dicionario)
    if flag_verifica == True:
        print(dicionario_professor[nome])

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
            opcao_menu_professor = menu_professor()
            ## cadastrar professor
            if opcao_menu_professor == '1':
                print("Digite o nome do professor que deseja cadastrar: ")
                nome_professor = input(">>> ").strip().capitalize()
                cadastro(dicionario_professor, nome_professor)
            elif opcao_menu_professor == '2':
                print("Digite a matricula do professor que deseja editar: ")
                matricula_editar_professor = int(input(">>> "))
                editar(matricula_editar_professor, dicionario_professor)
            elif opcao_menu_professor == '3':
                print("Digite o nome do professor que gostaria de ver os dados")
                nome_ver_dados_professor = input(">>> ")
                visualizar_professor(nome_ver_dados_professor, dicionario_professor)
            elif opcao_menu_professor == '4':
                print("Digite a matricula do professor que deseja excluir: ")
                matricula_excluir_professor = int(input(">>> "))
                excluir(matricula_excluir_professor, dicionario_professor)
    elif opcao_menu_adm == '3':
        while True:
            opcao_menu_aluno = menu_aluno()
            ## cadastrar aluno
            if opcao_menu_aluno == '1':
                print("Digite o nome do aluno que deseja cadastrar: ")
                nome_aluno = input(">>> ").strip().capitalize()
                cadastro(dicionario_aluno, nome_aluno)
            ## editar aluno
            elif opcao_menu_aluno == '2':
                print("Digite a matricula do aluno que deseja editar: ")
                matricula_editar_aluno = int(input(">>> "))
                editar(matricula_editar_aluno, dicionario_aluno)
            ## visualizar alunos
            elif opcao_menu_aluno == '3':
                visualizar(dicionario_aluno)
            elif opcao_menu_aluno == '4':
                print("Digite a matricula do aluno que deseja excluir: ")
                matricula_excluir_aluno = int(input(">>> "))
                excluir(matricula_excluir_aluno, dicionario_aluno)
            elif opcao_menu_aluno == '0':
                break
    elif opcao_menu_adm == '0':
        break
    else:
        print("Opção inválida! Digite um opção valida")
        print(30 * '=-')
        

