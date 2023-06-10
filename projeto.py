import json

def salvar_dicionarios(dicionario, nome_do_arquivo):
    with open(f'{nome_do_arquivo}.json', 'w') as file:
        json.dump(dicionario, file)
        
def descarregar_dicionario(nome_arquivo):
    with open(f'{nome_arquivo}.json', 'r') as file:
        return json.load(file)


# chave coordenador
dicionario_turma = descarregar_dicionario('dicionario_turma')

# chave professor
dicionario_professor = descarregar_dicionario('dicionario_professor')

# chave aluno
dicionario_aluno = descarregar_dicionario('dicionario_aluno')

# funções menu
def menu_adm():
    print("=-=" * 15)
    print(f"{'Menu Principal':^34}")
    print("=-=" * 15)
    print('''
    [1] - Coordenador
    [2] - Professor
    [3] - Aluno
    [0] - Sair
    ''')
    print("Escolha uma opção: ")
    return input(">>> ").strip()

def menu_coordenador():
    print("=-=" * 15)
    print(f"{'Menu Coordenador':^34}")
    print("=-=" * 15)
    print('''
    [1] - Criar turma
    [2] - Editar turma
    [3] - Ver turma
    [4] - Apagar turma
    [0] - Voltar
    ''')
    print("Escolha uma opção: ")
    return input(">>> ").strip()

def menu_coordenador_criar_turma():
    print("=-=" * 15)
    print(f"{'Menu Criar Turma':^34}")
    print("=-=" * 15)
    print('''
    [1] - Ver alunos e professores
    [2] - Adicionar disciplina (professor, aluno)
    [0] - Voltar
    ''')
    print("Escolha uma opção: ")
    return input(">>> ").strip()

def menu_professor():
    print("=-=" * 15)
    print(f"{'Menu Professor':^34}")
    print("=-=" * 15)
    print('''
    [1] - Cadastrar novo professor
    [2] - Editar professor cadastrado
    [3] - Ver dados de um professor cadastrado
    [4] - Excluir um professor cadastrado
    [5] - Visualizar as turmas de um professor específico
    [6] - Visualizar os alunos da turma de um professor específico
    [0] - Voltar
    ''')
    print("Escolha uma opção: ")
    return input(">>> ").strip()

def menu_aluno():
    print("=-=" * 15)
    print(f"{'Menu Aluno':^34}")
    print("=-=" * 15)
    print('''
    [1] - Cadastrar novo aluno
    [2] - Editar aluno cadastrado
    [3] - Visualizar alunos cadastrados cadastrados
    [4] - Apagar aluno cadastrado
    [0] - Voltar
    ''')
    print("Escolha uma opção: ")
    return input(">>> ").strip()



# funções aluno
def cadastro(dicionario, nome, nome_do_arquivo):
    flag_dicionario = verifica_nome(nome)
    if flag_dicionario == True:
        if dicionario:
            for keys in dicionario.keys():
                matricula = keys
            matricula = int(matricula)
            matricula += 1
            matricula = str(matricula)
        else:
            matricula = 1
        dicionario[matricula] = nome
        salvar_dicionarios(dicionario, nome_do_arquivo)
        dicionario = descarregar_dicionario(nome_do_arquivo)
        print("Cadastro feito com sucesso")


def editar_professor(nome, dicionario_professor, dicionario_turmas, nome_do_arquivo):
    # verificando o dicionario
    flag_dicionario = verifica_dicionario(nome, dicionario_professor)
    if flag_dicionario == True:
        # verificando se existem mais de uma pessoa com esse nome
        conta_nomes = verifica_dois_nomes_iguais(nome, dicionario_professor)
        # função para mostrar pessoas com nomes iguais ou parecidas
        mostrar_pessoas_nomes_iguais(nome, dicionario_professor)
        print()
        if conta_nomes == 1:
            print("Confirmação!")
        print(f"Digite a matricula do(a) {nome} que deseja editar: ")
        matricula = input(">>> ")
        flag_verifica_matricula = verifica_matricula(matricula, dicionario_professor)
        if flag_verifica_matricula:
            # verifico se o prof está em alguma disciplina
            flag_verifica_prof_em_disciplina = verficia_prof_em_disciplina(matricula, dicionario_turmas)
            if len(dicionario_turma) > 0 and flag_verifica_prof_em_disciplina:
                print("Digite o novo nome da pessoa: ")
                nome_pessoa = input(">>> ").strip().title()
                flag_verifica_nome = verifica_nome(nome_pessoa)
                if flag_verifica_nome:
                    # percorro as disciplinas
                    for chave_turma in dicionario_turmas.keys():
                        # percorro as matriculas dos prof
                        for chave_prof in dicionario_turmas[chave_turma].keys():
                            if chave_prof == matricula:
                                copia_dicionario = dicionario_turmas[chave_turma][chave_prof][dicionario_professor[chave_prof]].copy()
                                del dicionario_turmas[chave_turma][chave_prof]
                                dicionario_turmas[chave_turma][chave_prof] = {nome_pessoa: copia_dicionario}
                                flag_confirma_alteracao = True
                                break
                    if flag_confirma_alteracao:
                        nome_do_arquivo = 'dicionario_turma'
                        salvar_dicionarios(dicionario_turma, nome_do_arquivo)
                        dicionario_professor[matricula] = nome_pessoa
                        nome_do_arquivo = 'dicionario_professor'
                        salvar_dicionarios(dicionario_professor, nome_do_arquivo)
                        print("Professor editado com sucesso!")
                else:
                    print("O nome deve ser composto e não deve conter números.")
            else:
                print("Digite o novo nome da pessoa: ")
                nome_pessoa = input(">>> ").strip().title()
                flag_verifica_nome = verifica_nome(nome_pessoa)
                if flag_verifica_nome:
                    dicionario_professor[matricula] = nome_pessoa
                    print("Professor editado com sucesso!")
                    salvar_dicionarios(dicionario_professor, nome_do_arquivo)
                else:
                    print("O nome deve ser composto e não deve conter números.")
        else:
            print("Matricula incorreta!")
    else:
        return flag_dicionario

def editar_aluno(nome, dicionario_aluno, dicionario_turmas, nome_do_arquivo):
    # verificando o dicionario
    flag_dicionario = verifica_dicionario(nome, dicionario_aluno)
    if flag_dicionario == True:
        # verificando se existem mais de uma pessoa com esse nome
        conta_nomes = verifica_dois_nomes_iguais(nome, dicionario_aluno)
        # função para mostrar pessoas com nomes iguais ou parecidas
        mostrar_pessoas_nomes_iguais(nome, dicionario_aluno)
        print()
        if conta_nomes == 1:
            print("Confirmação!")
        print(f"Digite a matricula do(a) {nome} que deseja editar: ")
        matricula = input(">>> ")
        flag_verifica_matricula = verifica_matricula(matricula, dicionario_aluno)
        if flag_verifica_matricula:
            flag_verifica_prof_em_disciplina = verficia_prof_em_disciplina(matricula, dicionario_turmas)
            print("Digite o novo nome da pessoa: ")
            nome_pessoa = input(">>> ").strip().title()
            flag_dicionario = verifica_nome(nome_pessoa)
            if flag_dicionario:
                if len(dicionario_turma) > 0 and flag_verifica_prof_em_disciplina:
                    # percorre disciplinas
                    for chave_turma in dicionario_turmas.keys():
                        # percorre matricula
                        for chave_prof, nome_prof in dicionario_turmas[chave_turma].items():
                            # percorre os alunos desse professor
                            for prof in nome_prof.keys():
                                for alunos in dicionario_turmas[chave_turma][chave_prof][prof]:
                                    for chave_aluno in alunos.keys():
                                        if chave_aluno == matricula:
                                            alunos[matricula] = nome_pessoa
                    nome_do_arquivo = 'dicionario_aluno'     
                    dicionario_aluno[matricula] = nome_pessoa
                    salvar_dicionarios(dicionario_aluno, nome_do_arquivo)
                    print("Aluno editado com sucesso!")
                    nome_do_arquivo = 'dicionario_turma'
                    salvar_dicionarios(dicionario_turmas, nome_do_arquivo)
                else:
                    dicionario_aluno[matricula] = nome_pessoa
                    print("Aluno editado com sucesso!")
                    salvar_dicionarios(dicionario_aluno, nome_do_arquivo)
            else:
                print("O nome deve ser composto e não deve conter números.")
        else:
            print("Matricula incorreta!")

def visualizar_alunos_e_professor(dicionario_aluno, dicionario_prof):
    flag_aluno = verifica_dicionario_vazio(dicionario_aluno)
    flag_prof = verifica_dicionario_vazio(dicionario_prof)
    if flag_aluno and flag_prof:
        print(f"{' Alunos ':-^38}")
        print(f"{'Matrícula':<10} | {'Nome':<25}")
        for matricula, pessoas in dicionario_aluno.items():
            print(f"{matricula:<10} | {pessoas:<25}")
        print(f"{' Professores ':-^38}")
        print(f"{'SIAPE':<10} | {'Nome':<25}")
        for matricula, pessoas in dicionario_prof.items():
            print(f"{matricula:<10} | {pessoas:<25}")
        return True
        
def visualizar_aluno(dicionario):
    if len(dicionario_aluno) > 0:
        print(f"{' Alunos ':-^38}")
        print(f"{'Matrícula':<10} | {'Nome':<25}")
        for matricula, pessoas in dicionario.items():
            print(f"{matricula:<10} | {pessoas:<25}")
    else:
        print(f"{' Não há alunos cadastrados! ':*^38}")

def excluir_professor(nome, dicionario_professor, dicionario_turmas, nome_do_arquivo):
    flag_dicionario = verifica_dicionario(nome, dicionario_professor)
    if flag_dicionario == True:
        conta_nomes = verifica_dois_nomes_iguais(nome, dicionario_professor)
        mostrar_pessoas_nomes_iguais(nome, dicionario_professor)
        if conta_nomes == 1:
            print("Confirmação!")
        # percorrendo as pessoas com esse nome
        print(f"Digite a matricula do(a) {nome} que deseja excluir: ")
        matricula = input(">>> ")
        flag_verifica_matricula = verifica_matricula(matricula, dicionario_professor)
        if flag_verifica_matricula:
            # verifica prof em dicionario turmas
            flag_verifica_prof_em_disciplina = verficia_prof_em_disciplina(matricula, dicionario_turmas)
            if len(dicionario_turmas) > 0 and flag_verifica_prof_em_disciplina:
                turmas_a_remover = []
                # percorrendo os nomes das disciplinas
                for chave_turma in dicionario_turmas.keys():
                    flag_verifica_prof_em_disciplina = False
                    # percorrendo o numero da matricula do prof no dicionario turmas
                    for chave_prof in dicionario_turma[chave_turma].keys():
                        # se matricula do prof igual a matricula do prof na disciplina remove
                        if chave_prof == matricula:
                            flag_verifica_prof_em_disciplina = True
                        if flag_verifica_prof_em_disciplina:
                            turmas_a_remover.append(chave_turma)
                for turma in turmas_a_remover:
                    del dicionario_turmas[turma]
                nome_do_arquivo = 'dicionario_turma'
                salvar_dicionarios(dicionario_turmas, nome_do_arquivo)
                del dicionario_professor[matricula]
                print("Exclusão feita com sucesso!")
                nome_do_arquivo = 'dicionario_professor'
                salvar_dicionarios(dicionario_professor, nome_do_arquivo)
            else:
                del dicionario_professor[matricula]
                print("Exclusão feita com sucesso!")
                salvar_dicionarios(dicionario_professor, nome_do_arquivo)
                
        else:
            print("Matricula incorreta!")
    else:
        flag_dicionario

def excluir_aluno(nome, dicionario_aluno, dicionario_turmas, dicionario_professores, nome_do_arquivo):
    flag_dicionario = verifica_dicionario(nome, dicionario_aluno)
    if flag_dicionario == True:
        conta_nomes = verifica_dois_nomes_iguais(nome, dicionario_aluno)
        mostrar_pessoas_nomes_iguais(nome, dicionario_aluno)
        if conta_nomes == 1:
            print("Confirmação!")
        # percorrendo as pessoas com esse nome
        print(f"Digite a matricula do(a) {nome} que deseja excluir: ")
        matricula = input(">>> ")
        flag_verifica_matricula = verifica_matricula(matricula, dicionario_aluno)
        if flag_verifica_matricula:
            # verifico se existe alguma disciplina
            if len(dicionario_turmas) > 0:
                if len(dicionario_professor) > 0:
                    flag_verifica_aluno_em_disciplina = verifica_aluno_em_disciplina(matricula, dicionario_turmas, dicionario_professores)
                    # verifico se o aluno está em alguma disciplina
                    if flag_verifica_aluno_em_disciplina:
                        #percorro as disciplinas
                        for chave_turma in dicionario_turmas.keys():
                            # percorro a matricula prof e o nome dele
                            for chave_prof, nome_prof in dicionario_turmas[chave_turma].items():
                                # percorre os alunos desse professor
                                for prof in nome_prof.keys():
                                    for alunos in dicionario_turmas[chave_turma][chave_prof][prof]:
                                        for chave_aluno in alunos.keys():
                                            if chave_aluno == matricula:
                                                # dicionario_turmas[chave_turma][chave_prof][prof].remove(dicionario_turmas[chave_turma][chave_prof][prof][alunos])
                                                dicionario_turmas[chave_turma][chave_prof][prof].remove(alunos)

                        nome_do_arquivo = 'dicionario_turma'
                        salvar_dicionarios(dicionario_turmas, nome_do_arquivo)
                        del dicionario_aluno[matricula]
                        print("Exclusão feita com sucesso!")
                        nome_do_arquivo = 'dicionario_aluno'
                        salvar_dicionarios(dicionario_aluno, nome_do_arquivo)
                    # se não, só deletar o aluno do dicionario alunos
                    else:
                        del dicionario_aluno[matricula]
                        print("Exclusão feita com sucesso!")
                        salvar_dicionarios(dicionario_aluno, nome_do_arquivo)

            # se não existir só deleta o aluno no dicionario aluno
            else:
                del dicionario_aluno[matricula]
                print("Exclusão feita com sucesso!")
                salvar_dicionarios(dicionario_aluno, nome_do_arquivo)
        else:
            print("Matricula incorreta!")
    else:
        flag_dicionario

# funções turmas
def criar_turma(dicionario_aluno, dicionario_professor, dicionario_turma, nome_do_arquivo):
    while True:
        opcao_menu_coordenador_criar_turma = menu_coordenador_criar_turma()
        if opcao_menu_coordenador_criar_turma == '1':
            visualizar_alunos_e_professor(dicionario_aluno, dicionario_professor)
        elif opcao_menu_coordenador_criar_turma == '2':
            adicionar_disciplina(dicionario_aluno, dicionario_professor, dicionario_turma, nome_do_arquivo)
        elif opcao_menu_coordenador_criar_turma == '0':
            break
        else:
            print("Opção inválida! Digite um opção valida")

def adicionar_disciplina(dicionario_aluno, dicionario_prof, dicionario_turma, nome_do_arquivo):
    flag_aluno = verifica_dicionario_vazio(dicionario_aluno)
    flag_prof = verifica_dicionario_vazio(dicionario_prof)
    if flag_aluno and flag_prof:
        print("Digite o nome da disciplina: ")
        nome_disciplina = input(">>> ").strip().title()
        print("Digite o nome do professor que deseja adicionar na disciplina: ")
        nome_professor = input(">>> ").strip().title()
        flag_verifica_professor = verifica_dicionario(nome_professor, dicionario_professor)
        if flag_verifica_professor == True:
            conta_nomes = verifica_dois_nomes_iguais(nome_professor, dicionario_professor)
            # função para mostrar pessoas com nomes iguais ou parecidas
            mostrar_pessoas_nomes_iguais(nome_professor, dicionario_professor)
            if conta_nomes == 1:
                print("Confirmação!")
            print(f"Digite a matricula do(a) {nome_professor} que deseja cadastrar em {nome_disciplina}: ")
            matricula_prof = input(">>> ").strip()
            flag_verifica_matricula = verifica_matricula(matricula_prof, dicionario_professor)
            if flag_verifica_matricula:
                if nome_disciplina in dicionario_turma:
                    print("Disciplina já cadastrada")
                else:
                    dicionario_turma[nome_disciplina] = {}
                    lista_alunos = []
                    while True:
                        print("Digite o nome do aluno que deseja adicionar na disciplina ou não para sair: ")
                        nome_aluno = input(">>> ").strip().title()
                        if nome_aluno in 'Não' and len(lista_alunos) != 0:
                            break
                        else:
                            print("É necessário adicionar pelo menos um aluno!")
                        flag_verifica_aluno = False
                        flag_verifica_aluno = verifica_dicionario(nome_aluno, dicionario_aluno)
                        if flag_verifica_aluno:
                            conta_nomes = verifica_dois_nomes_iguais(nome_professor, dicionario_professor)
                            mostrar_pessoas_nomes_iguais(nome_aluno, dicionario_aluno)
                            if conta_nomes == 1:
                                print("Confirmação!")
                            print(f"Digite a matricula do(a) {nome_aluno} que deseja cadastrar em {nome_disciplina}: ")
                            matricula_aluno = input(">>> ").strip()
                            flag_verifica_matricula_aluno = verifica_matricula(matricula_aluno, dicionario_aluno)
                            dicionario_matricula_e_aluno = {matricula_aluno: dicionario_aluno[matricula_aluno]}
                            flag_verifica_cadastro = False
                            if len(lista_alunos) == 0:
                                flag_verifica_cadastro = False
                            else:
                                for cadastro in lista_alunos:
                                    if cadastro == dicionario_matricula_e_aluno:
                                        flag_verifica_cadastro = True
                            if flag_verifica_cadastro:
                                print("Aluno já cadastrado")
                            else:
                                if flag_verifica_matricula_aluno:
                                    lista_alunos.append(dicionario_matricula_e_aluno)
                                else:
                                    print("Matrícula incorreta")
                    dicionario_turma[nome_disciplina] = {matricula_prof: {}}
                    dicionario_turma[nome_disciplina][matricula_prof] = {dicionario_professor[matricula_prof]: lista_alunos}
                    salvar_dicionarios(dicionario_turma, nome_do_arquivo)
            else:
                print("Matricula incorreta!")
        else:
            print("Não existem alunos ou professores cadastrados!")

def ver_turmas(nome_disciplina):
    print(dicionario_turma[nome_disciplina])
    #print(f"Professor: {dicionario_turma["Professor"]}")


# verificações de pessoas com nomes iguais
def verifica_dois_nomes_iguais(nome, dicionario):
    conta_nomes = 0
    for valores in dicionario.values():
        if nome in valores:
            conta_nomes += 1
    return conta_nomes

def mostrar_pessoas_nomes_iguais(nome, dicionario):
    print(f"{'Matrícula':<10} | {'Nome':<25}")
    for matricula, pessoa in dicionario.items():
        if nome in pessoa:
            print(f"{matricula:^10} | {pessoa:<25}")
    
## funções de verificação e tratamento de erros básicos
def verifica_dicionario_vazio(dicionario):
    if len(dicionario) == 0:
        print("Não existem pessoas cadastradas")
    else:
        return True

def verifica_matricula(matricula, dicionario):
    flag = False
    for chaves in dicionario.keys():
        if chaves == matricula:
            flag = True
    return flag

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
    flag = True
    for caractere in nome:
        if caractere in ['0','1','2','3','4','5','6','7','8','9']:
            flag = False
    if flag == False or nome.count(" ") == 0:
        print("O nome deve ser composto e não deve conter números.")
    else:
        return True

## funções professor
def visualizar_professor(nome, dicionario):
    verifica_dicionario_professor = verifica_dicionario(nome, dicionario)
    if verifica_dicionario_professor:
        mostrar_pessoas_nomes_iguais(nome, dicionario)

# verifica pessoas (prof e aluno) em dicionario turmas 

def verficia_prof_em_disciplina(matricula, dicionario):
    flag_verifica_prof_em_disciplina = False
    for chave_turma in dicionario.keys():
        for chave_prof in dicionario[chave_turma].keys():
            if chave_prof == matricula:
                flag_verifica_prof_em_disciplina = True
    if flag_verifica_prof_em_disciplina:
        return True

def verifica_aluno_em_disciplina(matricula, dicionario_turmas, dicionario_professores):
    flag_verifica_aluno_em_disciplina = False
    # percorre as disciplinas
    for chave_turma in dicionario_turmas.keys():
    # percorrer as matrículas dos professores no dicionário turmas
        for chave_prof in dicionario_turmas[chave_turma].keys():
            # percorrer as matrículas dos professores no dicionário de professores
            for matricula_prof, nome_prof in dicionario_professores.items():
                # verificar se a matrícula do professor está presente no dicionário de turmas
                if matricula_prof == chave_prof:
                    # percorre os alunos daquele professor
                    for aluno in dicionario_turmas[chave_turma][chave_prof][nome_prof]:
                        # percorre a matricula daquele aluno
                        for chave_aluno in aluno.keys():
                            # verifica se a matricula do aluno for igual a matricula digitada
                            if chave_aluno == matricula:
                                flag_verifica_aluno_em_disciplina = True
    if flag_verifica_aluno_em_disciplina == True:
        return True
                    
        


## codigo principal
while True:
    # chama a função menu login ou menu principal
    opcao_menu_adm = menu_adm()
    # verifica se o usuario colocou uma 
    if opcao_menu_adm == '1':
        while True:
            # chamando a função menu coordenador
            opcao_menu_coordenador = menu_coordenador()
            if opcao_menu_coordenador == '1':
                nome_do_arquivo = 'dicionario_turma'
                criar_turma(dicionario_aluno, dicionario_professor, dicionario_turma, nome_do_arquivo)
            elif opcao_menu_coordenador == '2':
                pass
            elif opcao_menu_coordenador == '3':
                print("Digite o nome da disciplina que deseja ver: ")
                nome_disciplina = input(">>> ").strip().title()
                ver_turmas(nome_disciplina)
            elif opcao_menu_coordenador == '0':
                break
            else:
                print("Opção inválida! Digite um opção valida")
    
    elif opcao_menu_adm == '2':
        while True:
            opcao_menu_professor = menu_professor()
            ## cadastrar professor
            if opcao_menu_professor == '1':
                print("Digite o nome do professor que deseja cadastrar: ")
                nome_professor = input(">>> ").strip().title()
                nome_do_arquivo = 'dicionario_professor'
                cadastro(dicionario_professor, nome_professor, nome_do_arquivo)
            elif opcao_menu_professor == '2':
                print("Digite o nome do professor que deseja editar: ")
                nome_professor = input(">>> ").strip().title()
                nome_do_arquivo = 'dicionario_professor'
                editar_professor(nome_professor, dicionario_professor, dicionario_turma, nome_do_arquivo)
            elif opcao_menu_professor == '3':
                print("Digite o nome do professor que gostaria de ver os dados")
                nome_ver_dados_professor = input(">>> ").strip().title()
                nome_do_arquivo = 'dicionario_professor'
                visualizar_professor(nome_ver_dados_professor, dicionario_professor, dicionario_turma, nome_do_arquivo)
            elif opcao_menu_professor == '4':
                print("Digite o nome do professor que deseja excluir: ")
                nome_professor = input(">>> ").strip().title()
                nome_do_arquivo = 'dicionario_professor'
                excluir_professor(nome_professor, dicionario_professor, dicionario_turma, nome_do_arquivo)
            elif opcao_menu_professor == '5':
                pass
            elif opcao_menu_professor == '0':
                break
            else:
                print("Opção inválida! Digite um opção valida")
    elif opcao_menu_adm == '3':
        while True:
            opcao_menu_aluno = menu_aluno()
            ## cadastrar aluno
            if opcao_menu_aluno == '1':
                print("Digite o nome do aluno que deseja cadastrar: ")
                nome_aluno = input(">>> ").strip().title()
                nome_do_arquivo = 'dicionario_aluno'
                cadastro(dicionario_aluno, nome_aluno, nome_do_arquivo)
            ## editar aluno
            elif opcao_menu_aluno == '2':
                print("Digite o nome do aluno que deseja editar: ")
                nome_aluno = input(">>> ").strip().title()
                nome_do_arquivo = 'dicionario_aluno'
                editar_aluno(nome_aluno, dicionario_aluno, dicionario_turma, nome_do_arquivo)
            ## visualizar alunos
            elif opcao_menu_aluno == '3':
                visualizar_aluno(dicionario_aluno)
            elif opcao_menu_aluno == '4':
                print("Digite o nome do aluno que deseja excluir: ")
                nome_aluno = input(">>> ").strip().title()
                nome_do_arquivo = 'dicionario_aluno'
                excluir_aluno(nome_aluno, dicionario_aluno, dicionario_turma, dicionario_professor, nome_do_arquivo)
            elif opcao_menu_aluno == '0':
                break
            else:
                print("Opção inválida! Digite um opção valida")
    elif opcao_menu_adm == '0':
        break
    else:
        print("Opção inválida! Digite um opção valida")
        print(30 * '=-')
        

