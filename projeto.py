# chave coordenador
dicionario_turma = {}

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
    return input("Escolha uma opção de admin: ").strip()
    
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
    return input("Escolha uma opção: ")

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
        print("Cadastro feito com sucesso")


def editar(nome, dicionario):
    # verificando o dicionario
    flag_dicionario = verifica_dicionario(nome, dicionario)
    if flag_dicionario == True:
        # verificando se existem mais de uma pessoa com esse nome
        conta_nomes = verifica_dois_nomes_iguais(nome, dicionario)
        if conta_nomes > 1:
            mostrar_pessoas_nomes_iguais(nome, dicionario)
            print(f"Digite a matricula do(a) {nome} que deseja editar: ")
            matricula = input(">>> ")
            matricula = float(matricula)
            print("Digite o novo nome da pessoa: ")
            nome_pessoa = input(">>> ").strip().title()
            dicionario[matricula] = nome_pessoa
            print("Aluno editado com sucesso!")
        else:      
            ## percorro os valores
            for chave in dicionario.keys():
                # verifico a chave do valor
                if dicionario[chave] == nome:
                    matricula = chave
            print("Digite o novo nome do aluno: ")
            novo_nome_aluno = input(">>> ").strip().title()
            flag_nome = verifica_nome(novo_nome_aluno)
            if flag_nome == True:
                # com a chave eu altero no novo nome
                dicionario_aluno[matricula] = novo_nome_aluno
                print("Aluno editado com sucesso!")
    else:
        return flag_dicionario

def visualizar(dicionario):
    if len(dicionario) == 0:
        print("Não há alunos cadastrados!")
    else:
        print(f"{'Matrícula':<10} | {'Nome':<25}")
        for matricula, pessoas in dicionario.items():
            print(f"{matricula:<10} | {pessoas:<25}")

def excluir(nome, dicionario):
    flag_dicionario = verifica_dicionario(nome, dicionario)
    if flag_dicionario == True:
        conta_nomes = verifica_dois_nomes_iguais(nome, dicionario)
        if conta_nomes > 1:
            mostrar_pessoas_nomes_iguais(nome, dicionario)
            # percorrendo as pessoas com esse nome
            print(f"Digite a matricula do(a) {nome} que deseja excluir: ")
            matricula = input(">>> ")
            matricula = float(matricula)
            del dicionario[matricula]
            print("Exclusão feita com sucesso!")
        else:      
            ## percorro os valores
            for chave in dicionario.keys():
                # verifico a chave do valor
                if dicionario[chave] == nome:
                    matricula = chave
            del dicionario_aluno[matricula]
            print("Exclusão feita com sucesso!")

# funções turmas
def criar_turma(nome_disciplina, dicionario_aluno, dicionario_professor, dicionario_turma):
    verificar_dict_aluno = verifica_dicionario_vazio(dicionario_aluno)
    verificar_dict_prof = verifica_dicionario_vazio(dicionario_professor)
    if verificar_dict_aluno and verificar_dict_prof:
        print(dicionario_aluno)
        print(dicionario_professor) ## tobias faz
        print()
        print("Digite o nome do professor que deseja adicionar na disciplina: ")
        nome_professor = input(">>> ").strip().title()
        flag_verifica_professor = verifica_dicionario(nome_professor, dicionario_professor)
        if flag_verifica_professor == True:
            if nome_disciplina in dicionario_turma:
                print("Disciplina já cadastrada")
            else:
                dicionario_turma[nome_disciplina] = {}
                lista_alunos = []
                while True:
                    print("Digite o nome do aluno que deseja adicionar na disciplina ou não para sair: ")
                    nome_aluno = input(">>> ").strip().title()
                    flag_verifica_aluno = False
                    flag_verifica_aluno = verifica_dicionario(nome_aluno, dicionario_aluno)
                    if flag_verifica_aluno:
                        lista_alunos.append(nome_aluno)
                    elif nome_aluno in 'Sair':
                        break
                    else:
                        print("Aluno não está cadastrado")
                dicionario_turma[nome_disciplina] = {nome_professor: [lista_alunos]}
    else:
        print("Não existem alunos ou professores cadastrados!")



# verificações de pessoas com nomes iguais
def verifica_dois_nomes_iguais(nome, dicionario):
    conta_nomes = 0
    for valores in dicionario.values():
        if nome in valores:
            conta_nomes += 1
    return conta_nomes

def mostrar_pessoas_nomes_iguais(nome, dicionario):
    for matricula, pessoa in dicionario.items():
        if nome in pessoa:
            print(f"{matricula:<10} | {pessoa:<25}")

## funções de verificação
def verifica_dicionario_vazio(dicionario):
    if len(dicionario) == 0:
        print("Não existem pessoas cadastradas")
    else:
        return True

def verifica_dicionario(nome, dicionario):
    flag_verifica_dicionario_vazio = verifica_dicionario_vazio(dicionario) 
    if flag_verifica_dicionario_vazio:
        flag = False
        for valor in dicionario.values():
            if nome in valor:
                flag = True
        if flag:
            return True  
        else:
            print("A pessoa não está cadastrado!")

def verifica_nome(nome):
    return True
    # flag =  True
    # if ' ' in nome_aluno:
    #     lista_aluno = nome_aluno.split(" ")
    #     for elemento in lista_aluno:
    #         if elemento.isalpha() == False:
    #             flag = False
    #         else:
    #             print("O nome deve ser composto e não deve conter números.")
    #     if flag == True:
    #         return True
    # else:
    #     print("O nome deve ser composto e não deve conter números.")

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
        if opcao_menu_coordenador == '1':
            print("Digite o nome da disciplina: ")
            nome_disciplina = input(">>> ")
            criar_turma(nome_disciplina, dicionario_aluno, dicionario_professor, dicionario_turma)
        else:
            print("Opção inválida! Digite um opção valida")
    
    elif opcao_menu_adm == '2':
        while True:
            opcao_menu_professor = menu_professor()
            ## cadastrar professor
            if opcao_menu_professor == '1':
                print("Digite o nome do professor que deseja cadastrar: ")
                nome_professor = input(">>> ").strip().title()
                cadastro(dicionario_professor, nome_professor)
            elif opcao_menu_professor == '2':
                print("Digite o nome do professor que deseja editar: ")
                nome_professor = input(">>> ").strip().title()
                editar(nome_professor, dicionario_professor)
            elif opcao_menu_professor == '3':
                print("Digite o nome do professor que gostaria de ver os dados")
                nome_ver_dados_professor = input(">>> ").strip().title()
                visualizar_professor(nome_ver_dados_professor, dicionario_professor)
            elif opcao_menu_professor == '4':
                print("Digite o nome do profesosr que deseja excluir: ")
                nome_professor = input(">>> ").strip().title()
                excluir(nome_professor, dicionario_professor)
            elif opcao_menu_professor == '0':
                break
    elif opcao_menu_adm == '3':
        while True:
            opcao_menu_aluno = menu_aluno()
            ## cadastrar aluno
            if opcao_menu_aluno == '1':
                print("Digite o nome do aluno que deseja cadastrar: ")
                nome_aluno = input(">>> ").strip().title()
                cadastro(dicionario_aluno, nome_aluno)
            ## editar aluno
            elif opcao_menu_aluno == '2':
                print("Digite o nome do aluno que deseja editar: ")
                nome_aluno = input(">>> ").strip().title()
                editar(nome_aluno, dicionario_aluno)
            ## visualizar alunos
            elif opcao_menu_aluno == '3':
                visualizar(dicionario_aluno)
            elif opcao_menu_aluno == '4':
                print("Digite o nome do aluno que deseja excluir: ")
                nome_aluno = input(">>> ").strip().title()
                excluir(nome_aluno, dicionario_aluno)
            elif opcao_menu_aluno == '0':
                break
    elif opcao_menu_adm == '0':
        break
    else:
        print("Opção inválida! Digite um opção valida")
        print(30 * '=-')
        

