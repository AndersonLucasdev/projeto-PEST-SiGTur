# chave coordenador
dicionario_coordenador = {}

# chave professor
dicionario_professor = {}

# chave aluno
dicionario_aluno = {}

def menu_adm():
    print('''
    [1] - Coordenador
    [2] - Professor
    [3] - Aluno
    [0] - Sair
    ''')
    adm = int(input("Escolha uma opção de admin: "))
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

while True:
    # chama a função menu login ou menu principal
    opcao_menu_adm = menu_adm()
    # verifica se o usuario colocou uma 
    if opcao_menu_adm == 1:
        opcao_menu_coordenador = menu_coordenador()
        if opcao_menu_coordenador == 1:
            pass
        else:
            print("Opção inválida! Digite um opção valida")
    else:
        print("Opção inválida! Digite um opção valida")
        

