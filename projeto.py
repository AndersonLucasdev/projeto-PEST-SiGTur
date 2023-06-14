import json

# funções para json
def salvar_dicionarios(dicionario, nome_do_arquivo):
    with open(f'{nome_do_arquivo}.json', 'w') as file:
        json.dump(dicionario, file)
        
def descarregar_dicionario(nome_arquivo):
    with open(f'{nome_arquivo}.json', 'r') as file:
        return json.load(file)

# dicionario coordenador, professor e aluno
dicionario_turma = descarregar_dicionario('dicionario_turma')
dicionario_professor = descarregar_dicionario('dicionario_professor')
dicionario_aluno = descarregar_dicionario('dicionario_aluno')

# funções para menu
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
    [4] - Ver todas as turmas
    [5] - Apagar turma
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

def menu_coordenador_editar_turma():
    print("=-=" * 15)
    print(f"{'Menu Editar Turma':^34}")
    print("=-=" * 15)
    print('''
    [1] - Mudar professor
    [2] - Adicionar aluno
    [3] - Remover Aluno
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
            # transformo para numero somo e transformo para str de novo
            matricula = int(matricula)
            matricula += 1
            matricula = str(matricula)
        else:
            matricula = '1'
        dicionario[matricula] = nome
        salvar_dicionarios(dicionario, nome_do_arquivo)
        dicionario = descarregar_dicionario(nome_do_arquivo)
        print("Cadastro feito com sucesso")



def visualizar_aluno(dicionario):
    flag_dicionario_vazio = verifica_dicionario_vazio(dicionario)
    if flag_dicionario_vazio:
        print(f"{' Alunos ':-^38}")
        print(f"{'Matrícula':<10} | {'Nome':<25}")
        for matricula, pessoas in dicionario.items():
            print(f"{matricula:<10} | {pessoas:<25}")
    else:
        print(f"{' Não há alunos cadastrados! ':*^38}")



# excluir aluno
def excluir_aluno(nome, dicionario_aluno, dicionario_turmas, dicionario_professores, nome_do_arquivo):
    flag_verificacoes_primarias_excluir_aluno, matricula = verificacoes_primarias_aluno(nome, dicionario_aluno)
    if flag_verificacoes_primarias_excluir_aluno:
        flag_verificacoes_dicionario_excluir_aluno = verificacoes_dicionario_excluir_aluno(matricula, dicionario_turmas, dicionario_professores)
        if flag_verificacoes_dicionario_excluir_aluno:
            excluir_aluno_funcao(matricula, dicionario_turmas)
            # salvos as alterações no dicionario e json turma e aluno
            nome_do_arquivo = 'dicionario_turma'
            salvar_dicionarios(dicionario_turmas, nome_do_arquivo)
            del dicionario_aluno[matricula]
            print("Exclusão feita com sucesso!")
            nome_do_arquivo = 'dicionario_aluno'
            salvar_dicionarios(dicionario_aluno, nome_do_arquivo)
        else:
            del dicionario_aluno[matricula]
            print("Exclusão feita com sucesso!")
            salvar_dicionarios(dicionario_aluno, nome_do_arquivo)
# funções aux no excluir aluno
def verificacoes_primarias_aluno(nome, dicionario_aluno):
    # verificações no dicionario
    flag_dicionario = verifica_dicionario(nome, dicionario_aluno)
    if flag_dicionario == True:
        conta_nomes = verifica_dois_nomes_iguais(nome, dicionario_aluno)
        mostrar_pessoas_nomes_iguais(nome, dicionario_aluno)
        if conta_nomes == 1:
            print("Confirmação!")
        # percorrendo as pessoas com esse nome
        print(f"Digite a matricula do(a) {nome} que deseja excluir: ")
        matricula = input(">>> ").strip()
        # verificações na matricula
        flag_verifica_matricula = verifica_matricula(matricula, dicionario_aluno)
        if flag_verifica_matricula:
            return True, matricula
        else:
            print("Matricula incorreta!")

def verificacoes_dicionario_excluir_aluno(matricula, dicionario_turmas, dicionario_professores):
    flag_verifica_dicionario_vazio_turmas = verifica_dicionario_vazio(dicionario_turmas)
    if flag_verifica_dicionario_vazio_turmas:
        flag_verifica_dicionario_vazio_prof = verifica_dicionario_vazio(dicionario_professor)
        if flag_verifica_dicionario_vazio_prof:
            # verifica se o aluno está matriculado em alguma disciplina
            flag_verifica_aluno_em_disciplina = verifica_aluno_em_disciplina(matricula, dicionario_turmas, dicionario_professores)
            if flag_verifica_aluno_em_disciplina:
                return True

def excluir_aluno_funcao(matricula, dicionario_turmas):
    #percorro as disciplinas
    for chave_turma in dicionario_turmas.keys():
        # percorro a matricula prof e o nome dele
        for chave_prof, nome_prof in dicionario_turmas[chave_turma].items():
            # percorre os alunos desse professor
            for prof in nome_prof.keys():
                for alunos in dicionario_turmas[chave_turma][chave_prof][prof]:
                    for chave_aluno in alunos.keys():
                        # se matricula no turmas igual matricula do aluno no dict alunos
                        if chave_aluno == matricula:
                            # removo o aluno do dicionario turmas
                            dicionario_turmas[chave_turma][chave_prof][prof].remove(alunos)
    return dicionario_turmas




# editar aluno
def editar_aluno(nome, dicionario_aluno, dicionario_turmas, nome_do_arquivo):
    flag_verificacoes_primarias_aluno, matricula = verificacoes_primarias_aluno(nome, dicionario_aluno)
    # verifica se a matricula está cadastrada
    if flag_verificacoes_primarias_aluno:
        flag_verifica_prof_e_pede_novo_nome, nome_pessoa = verifica_prof_e_pede_novo_nome(matricula, dicionario_turmas)
        if flag_verifica_prof_e_pede_novo_nome:
            editar_aluno_funcao(matricula, nome_pessoa, dicionario_turmas)
            # muda nos dicionarios e json no aluno e turma
            nome_do_arquivo = 'dicionario_aluno'     
            dicionario_aluno[matricula] = nome_pessoa
            salvar_dicionarios(dicionario_aluno, nome_do_arquivo)
            print("Aluno editado com sucesso!")
            nome_do_arquivo = 'dicionario_turma'
            salvar_dicionarios(dicionario_turmas, nome_do_arquivo)
# funções aux no editar aluno
def verifica_prof_e_pede_novo_nome(matricula, dicionario_turmas):
    # verifica se o prof está em alguma disciplina
    flag_verifica_prof_em_disciplina = verficia_prof_em_disciplina(matricula, dicionario_turmas)
    print("Digite o novo nome da pessoa: ")
    nome_pessoa = input(">>> ").strip().title()
    flag_dicionario = verifica_nome(nome_pessoa)
    if flag_dicionario:
        if len(dicionario_turma) > 0 and flag_verifica_prof_em_disciplina:
            return True, nome_pessoa
        else:
            # muda apenas no json e dicionario aluno
            dicionario_aluno[matricula] = nome_pessoa
            print("Aluno editado com sucesso!")
            salvar_dicionarios(dicionario_aluno, nome_do_arquivo)
    else:
        print("O nome deve ser composto e não deve conter números.")

def editar_aluno_funcao(matricula, nome_pessoa, dicionario_turmas):
# percorre disciplinas
    for chave_turma in dicionario_turmas.keys():
        # percorre matricula
        for chave_prof, nome_prof in dicionario_turmas[chave_turma].items():
            # percorre os alunos desse professor
            for prof in nome_prof.keys():
                for alunos in dicionario_turmas[chave_turma][chave_prof][prof]:
                    for chave_aluno in alunos.keys():
                        # se a matricula e a matricula do aluno na disciplina for igual
                        if chave_aluno == matricula:
                            # muda com o novo nome
                            alunos[matricula] = nome_pessoa
    return dicionario_turmas




# funçoes professor
# editar professor
def editar_professor(nome, dicionario_professor, dicionario_turmas, nome_do_arquivo):
    flag_verificacoes_iniciais_editar_professor, matricula = verificacoes_iniciais_editar_professor(nome, dicionario_professor, dicionario_turmas)
    if len(dicionario_turma) > 0 and flag_verificacoes_iniciais_editar_professor:
        flag_subtituindo_prof_em_disciplinas = subtituindo_prof_em_disciplinas(dicionario_turmas, matricula, dicionario_professor)
        if flag_subtituindo_prof_em_disciplinas:
            # salvo no json turma e professor
            nome_do_arquivo = 'dicionario_turma'
            salvar_dicionarios(dicionario_turma, nome_do_arquivo)
            dicionario_professor[matricula] = nome_pessoa
            nome_do_arquivo = 'dicionario_professor'
            salvar_dicionarios(dicionario_professor, nome_do_arquivo)
            print("Professor editado com sucesso!")
    else:
        # só mudo no dicionario e json professor
        print("Digite o novo nome da pessoa: ")
        nome_pessoa = input(">>> ").strip().title()
        flag_verifica_nome = verifica_nome(nome_pessoa)
        if flag_verifica_nome:
            dicionario_professor[matricula] = nome_pessoa
            print("Professor editado com sucesso!")
            salvar_dicionarios(dicionario_professor, nome_do_arquivo)
        else:
            print("O nome deve ser composto e não deve conter números.")

# funções aux editar_professor
def verificacoes_iniciais_editar_professor(nome, dicionario_professor, dicionario_turmas):
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
                return True, matricula
            
def subtituindo_prof_em_disciplinas(dicionario_turmas, matricula, dicionario_professor):
    print("Digite o novo nome da pessoa: ")
    nome_pessoa = input(">>> ").strip().title()
    flag_verifica_nome = verifica_nome(nome_pessoa)
    # verifica se o nome está no padrão
    if flag_verifica_nome:
        # percorro as disciplinas
        for chave_turma in dicionario_turmas.keys():
            # percorro as matriculas dos prof
            for chave_prof in dicionario_turmas[chave_turma].keys():
                if chave_prof == matricula:
                    # guardo os valores, excluo o professor antigo
                    copia_dicionario = dicionario_turmas[chave_turma][chave_prof][dicionario_professor[chave_prof]].copy()
                    del dicionario_turmas[chave_turma][chave_prof]
                    # coloco o novo professor com a copia dos valores
                    dicionario_turmas[chave_turma][chave_prof] = {nome_pessoa: copia_dicionario}
        return True
    else:
        print("O nome deve ser composto e não deve conter números.")
                    


# excluir professor
def excluir_professor(nome, dicionario_professor, dicionario_turmas, nome_do_arquivo):
    flag_verifica_tudo_excluir_professor, matricula = verifica_tudo_excluir_professor(nome, dicionario_professor, dicionario_turmas)
    if len(dicionario_turmas) > 0 and flag_verifica_tudo_excluir_professor:
        percorro_disciplinas_para_excluir(matricula, dicionario_turmas)
        # salvo no json e dicionario turma e professor
        nome_do_arquivo = 'dicionario_turma'
        salvar_dicionarios(dicionario_turmas, nome_do_arquivo)
        del dicionario_professor[matricula]
        print("Exclusão feita com sucesso!")
        nome_do_arquivo = 'dicionario_professor'
        salvar_dicionarios(dicionario_professor, nome_do_arquivo)
    else:
        # salvo no json e dicionario apenas do professor
        del dicionario_professor[matricula]
        print("Exclusão feita com sucesso!")
        salvar_dicionarios(dicionario_professor, nome_do_arquivo)    

# funções aux excluir professor
def verifica_tudo_excluir_professor(nome, dicionario_professor, dicionario_turmas):
    # verificações no dicionario
    flag_dicionario = verifica_dicionario(nome, dicionario_professor)
    if flag_dicionario == True:
        conta_nomes = verifica_dois_nomes_iguais(nome, dicionario_professor)
        mostrar_pessoas_nomes_iguais(nome, dicionario_professor)
        if conta_nomes == 1:
            print("Confirmação!")
        # percorrendo as pessoas com esse nome
        print(f"Digite a matricula do(a) {nome} que deseja excluir: ")
        matricula = input(">>> ").strip()
        # verificações na matricula
        flag_verifica_matricula = verifica_matricula(matricula, dicionario_professor)
        if flag_verifica_matricula:
            # verifica prof em dicionario turmas
            flag_verifica_prof_em_disciplina = verficia_prof_em_disciplina(matricula, dicionario_turmas)
            if len(dicionario_turmas) > 0 and flag_verifica_prof_em_disciplina:
                return True, matricula
        else:
            print("Matricula incorreta!")

def percorro_disciplinas_para_excluir(matricula, dicionario_turmas):
    turmas_a_remover = []
    # percorrendo os nomes das disciplinas
    for chave_turma in dicionario_turmas.keys():
        flag_verifica_prof_em_disciplina = False
        # percorrendo o numero da matricula do prof no dicionario turmas
        for chave_prof in dicionario_turma[chave_turma].keys():
            # se matricula do prof igual a matricula do prof na disciplina remove
            if int(chave_prof) == int(matricula):
                flag_verifica_prof_em_disciplina = True
            if flag_verifica_prof_em_disciplina:
                # adiciona a disciplina na lista de disciplinas
                turmas_a_remover.append(chave_turma)
    for turma in turmas_a_remover:
        # percorro a lista de disciplinas deletando-a
        del dicionario_turmas[turma]
    return dicionario_turmas




# visualizar turmas prof especifico
def visualizar_turmas_professor_especifico(nome_professor, dicionario_professor, dicionario_turma):
    flag_verifica_visualizar_turmas_professor_especifico = verifica_visualizar_turmas_professor_especifico(dicionario_professor, dicionario_turma)
    if flag_verifica_visualizar_turmas_professor_especifico:
        flag_pesquisa_visualizar_turmas_professor_especifico, matricula = pesquisa_visualizar_turmas_professor_especifico(nome_professor, dicionario_professor)
        if flag_pesquisa_visualizar_turmas_professor_especifico:
            flag_verifica_prof_em_disciplina = verficia_prof_em_disciplina(matricula, dicionario_turma)
            if flag_verifica_prof_em_disciplina:
                visualizar_turmas_professor_especifico_funcao(matricula, dicionario_turma)
            else:
                print("Professor não tem disciplinas cadastradas!")

def verifica_visualizar_turmas_professor_especifico(dicionario_professor, dicionario_turma):
    flag_verifica_dicionario_vazio_professor = verifica_dicionario_vazio(dicionario_professor)
    if flag_verifica_dicionario_vazio_professor:
        flag_verifica_dicionario_vazio_turma = verifica_dicionario_vazio(dicionario_turma)
        if flag_verifica_dicionario_vazio_turma:
            return True
        else:
            print("Não existem turmas cadastradas!")
    else:
        print("Não existem professores cadastrados!")

def pesquisa_visualizar_turmas_professor_especifico(nome_professor, dicionario_professor):
    conta_nomes = verifica_dois_nomes_iguais(nome_professor, dicionario_professor)
    mostrar_pessoas_nomes_iguais(nome_professor, dicionario_professor)
    if conta_nomes == 1:
        print("Confirmação!")
    # percorrendo as pessoas com esse nome
    print(f"Digite a matricula do(a) {nome_professor} que deseja visualizar: ")
    matricula = input(">>> ").strip()
    # verificações na matricula
    flag_verifica_matricula = verifica_matricula(matricula, dicionario_professor)
    # verifica se o prof digitado existe em dict prof
    if flag_verifica_matricula:
        return True, matricula

def visualizar_turmas_professor_especifico_funcao(matricula, dicionario_turmas):
    print("Disciplinas: ")
    for nome_disciplina in dicionario_turmas.keys():
        for matricula_prof in dicionario_turmas[nome_disciplina].keys():
            if int(matricula_prof) == int(matricula):
                print(f"{nome_disciplina.upper()}")




# visualizar alunos prof especifico
def visualizar_alunos_professor_especifico(nome_professor, dicionario_professor, dicionario_turma):
    flag_verifica_tudo_visualizar_alunos_professor_especifico, matricula = verifica_tudo_visualizar_alunos_professor_especifico(nome_professor, dicionario_professor, dicionario_turma)
    if flag_verifica_tudo_visualizar_alunos_professor_especifico:
            lista_alunos_em_professor = adiciona_aluno_em_lista_para_ser_percorrida(matricula, dicionario_turma, dicionario_aluno)
            percorre_lista_alunos_professor_especifico(lista_alunos_em_professor)

# funções para auxiliar o visualizar_alunos_professor_especifico
def verifica_tudo_visualizar_alunos_professor_especifico(nome_professor, dicionario_professor, dicionario_turma):
    flag_verifica_visualizar_turmas_professor_especifico = verifica_visualizar_turmas_professor_especifico(dicionario_professor, dicionario_turma)
    if flag_verifica_visualizar_turmas_professor_especifico:
        flag_pesquisa_visualizar_turmas_professor_especifico, matricula = pesquisa_visualizar_turmas_professor_especifico(nome_professor, dicionario_professor)
        if flag_pesquisa_visualizar_turmas_professor_especifico:
            flag_verifica_prof_em_disciplina = verficia_prof_em_disciplina(matricula, dicionario_turma)
            if flag_verifica_prof_em_disciplina:
                return True, matricula

def adiciona_aluno_em_lista_para_ser_percorrida(matricula, dicionario_turma, dicionario_aluno):
    lista_alunos_em_professor = []
    # adicionar a lista apenas os alunos do prof
    for chave_turma in dicionario_turma.keys():
        # percorro a matricula prof e o nome dele
        for chave_prof, nome_prof in dicionario_turma[chave_turma].items():
            # percorre os alunos desse professor
            for prof in nome_prof.keys():
                for alunos in dicionario_turma[chave_turma][chave_prof][prof]:
                    for chave_aluno in alunos.keys():
                        # se matricula no turmas igual matricula do aluno no dict alunos
                        if int(chave_aluno) == int(matricula):
                            dicionario_aluno = {matricula: dicionario_aluno[matricula]}
                            # verifica se o aluno já foi cadastrado
                            if dicionario_aluno not in lista_alunos_em_professor:   
                                lista_alunos_em_professor.append(dicionario_aluno)    
    return lista_alunos_em_professor

def percorre_lista_alunos_professor_especifico(lista_alunos_em_professor):
    print(f"{'Matrícula:':<12} Aluno:")
    for aluno in lista_alunos_em_professor:
        for matricula_alunos, nome_aluno in aluno.items():
            print(f"{matricula_alunos:<12}",nome_aluno)




# funções turmas
# menu criar turmas
def criar_turma(dicionario_aluno, dicionario_professor, dicionario_turma, nome_do_arquivo):
    # verifico o menu criar turmas
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

# visualizar prof e aluno
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


# adicionar disciplina
def adicionar_disciplina(dicionario_aluno, dicionario_prof, dicionario_turma, nome_do_arquivo):
    flag_verifica_prof_adicionar_disciplina, nome_disciplina, matricula_prof = verifica_prof_adicionar_disciplina(nome_professor, dicionario_prof)
    if flag_verifica_prof_adicionar_disciplina:
        if nome_disciplina in dicionario_turma:
            print("Disciplina já cadastrada")
        else:
            dicionario_turma[nome_disciplina] = {}
            # crio uma lista de alunos
            lista_alunos = []
            while True:
                print("Digite o nome do aluno que deseja adicionar na disciplina ou não para sair: ")
                nome_aluno = input(">>> ").strip().title()
                if nome_aluno in 'Não':
                    break
                flag_verifica_aluno = False
                # verifico se o aluno está cadastrado
                flag_verifica_aluno = verifica_dicionario(nome_aluno, dicionario_aluno)
                if flag_verifica_aluno:
                    conta_nomes = verifica_dois_nomes_iguais(nome_professor, dicionario_professor)
                    mostrar_pessoas_nomes_iguais(nome_aluno, dicionario_aluno)
                    if conta_nomes == 1:
                        print("Confirmação!")
                    print(f"Digite a matricula do(a) {nome_aluno} que deseja cadastrar em {nome_disciplina}: ")
                    matricula_aluno = input(">>> ").strip()
                    # verifica se a matricula do aluno existe
                    flag_verifica_matricula_aluno = verifica_matricula(matricula_aluno, dicionario_aluno)
                    # um dicionario apenas com a matricula do aluno e o nome dele
                    dicionario_matricula_e_aluno = {matricula_aluno: dicionario_aluno[matricula_aluno]}
                    flag_verifica_cadastro = False
                    if len(lista_alunos) == 0:
                        flag_verifica_cadastro = False
                    else:
                        for cadastro in lista_alunos:
                            # se a matricula do aluno for igual a matricula do aluno na disciplina ele já foi cadastrado
                            if cadastro == dicionario_matricula_e_aluno:
                                flag_verifica_cadastro = True
                    if flag_verifica_cadastro:
                        print("Aluno já cadastrado")
                    else:
                        if flag_verifica_matricula_aluno:
                            # adiciono o dicionario com a matricula do aluno e o seu nome na lista de alunos
                            lista_alunos.append(dicionario_matricula_e_aluno)
                        else:
                            print("Matrícula incorreta")
            # modifico no dicionario e no json turma, adicionando no diconario a lista de alunos (matricula e nome)
            dicionario_turma[nome_disciplina] = {matricula_prof: {}}
            dicionario_turma[nome_disciplina][matricula_prof] = {dicionario_professor[matricula_prof]: lista_alunos}
            salvar_dicionarios(dicionario_turma, nome_do_arquivo)
    else:
        print("Matricula incorreta!")


def verifica_prof_adicionar_disciplina(nome_professor, dicionario_prof):
    # faço verificações nos dicionarios
    flag_aluno = verifica_dicionario_vazio(dicionario_aluno)
    flag_prof = verifica_dicionario_vazio(dicionario_prof)
    if flag_aluno and flag_prof:
        print("Digite o nome da disciplina: ")
        nome_disciplina = input(">>> ").strip().title()
        print("Digite o nome do professor que deseja adicionar na disciplina: ")
        nome_professor = input(">>> ").strip().title()
        # verifico se o prof está cadastrado
        flag_verifica_professor = verifica_dicionario(nome_professor, dicionario_professor)
        if flag_verifica_professor == True:
            conta_nomes = verifica_dois_nomes_iguais(nome_professor, dicionario_professor)
            # função para mostrar pessoas com nomes iguais ou parecidas
            mostrar_pessoas_nomes_iguais(nome_professor, dicionario_professor)
            if conta_nomes == 1:
                print("Confirmação!")
            print(f"Digite a matricula do(a) {nome_professor} que deseja cadastrar em {nome_disciplina}: ")
            matricula_prof = input(">>> ").strip()
            # verifico se a matricula existe
            flag_verifica_matricula = verifica_matricula(matricula_prof, dicionario_professor)
            # verifico se a disciplina já foi cadastrada
            if flag_verifica_matricula:
                return True, nome_disciplina, matricula_prof
    else:
        print("Matricula incorreta!")


def verifica_aluno_adicionar_disciplina():
    dicionario_turma[nome_disciplina] = {}
    # crio uma lista de alunos
    lista_alunos = []
    while True:
        print("Digite o nome do aluno que deseja adicionar na disciplina ou não para sair: ")
        nome_aluno = input(">>> ").strip().title()
        if nome_aluno in 'Não':
            break
        flag_verifica_aluno = False
        # verifico se o aluno está cadastrado
        flag_verifica_aluno = verifica_dicionario(nome_aluno, dicionario_aluno)
        if flag_verifica_aluno:
            conta_nomes = verifica_dois_nomes_iguais(nome_professor, dicionario_professor)
            mostrar_pessoas_nomes_iguais(nome_aluno, dicionario_aluno)
            if conta_nomes == 1:
                print("Confirmação!")
            print(f"Digite a matricula do(a) {nome_aluno} que deseja cadastrar em {nome_disciplina}: ")
            matricula_aluno = input(">>> ").strip()
            # verifica se a matricula do aluno existe
            flag_verifica_matricula_aluno = verifica_matricula(matricula_aluno, dicionario_aluno)
            # um dicionario apenas com a matricula do aluno e o nome dele
            dicionario_matricula_e_aluno = {matricula_aluno: dicionario_aluno[matricula_aluno]}
            flag_verifica_cadastro = False
            if len(lista_alunos) == 0:
                flag_verifica_cadastro = False
            else:
                for cadastro in lista_alunos:
                    # se a matricula do aluno for igual a matricula do aluno na disciplina ele já foi cadastrado
                    if cadastro == dicionario_matricula_e_aluno:
                        flag_verifica_cadastro = True
            if flag_verifica_cadastro:
                print("Aluno já cadastrado")
            else:
                if flag_verifica_matricula_aluno:
                    # adiciono o dicionario com a matricula do aluno e o seu nome na lista de alunos
                    lista_alunos.append(dicionario_matricula_e_aluno)
                else:
                    print("Matrícula incorreta")

# def verificacoes_aluno_cadastrar():
#     print("Digite o nome do aluno que deseja adicionar na disciplina ou não para sair: ")
#     nome_aluno = input(">>> ").strip().title()
#     if nome_aluno in 'Não':
#         break
#     flag_verifica_aluno = False
#     # verifico se o aluno está cadastrado
#     flag_verifica_aluno = verifica_dicionario(nome_aluno, dicionario_aluno)
#     if flag_verifica_aluno:
#         conta_nomes = verifica_dois_nomes_iguais(nome_professor, dicionario_professor)
#         mostrar_pessoas_nomes_iguais(nome_aluno, dicionario_aluno)
#         if conta_nomes == 1:
#             print("Confirmação!")
#         print(f"Digite a matricula do(a) {nome_aluno} que deseja cadastrar em {nome_disciplina}: ")
#         matricula_aluno = input(">>> ").strip()
#         # verifica se a matricula do aluno existe
#         flag_verifica_matricula_aluno = verifica_matricula(matricula_aluno, dicionario_aluno)
#         return 



def editar_turma(dicionario_turma, dicionario_professor, nome_arquivo):
    while True:
        opcao_menu_coordenador_editar_turma = menu_coordenador_editar_turma()
        if opcao_menu_coordenador_editar_turma == '1':
            print("Digite o nome da disciplina que deseja modificar o prof: ")
            nome_disciplina_mudar = input(">>> ").strip().title()
            mudar_prof_uma_disciplina(nome_disciplina_mudar, dicionario_turma, dicionario_professor)
        elif opcao_menu_coordenador_editar_turma == '2':
            print("Digite o nome da disciplina que deseja adicionar aluno: ")
            nome_disciplina = input(">>> ").strip().title()
            adicionar_aluno_em_disciplina(nome_disciplina, dicionario_aluno, dicionario_turma)
        elif opcao_menu_coordenador_editar_turma == '3':
            print("Digite o nome da disciplina que deseja remover aluno: ")
            nome_disciplina = input(">>> ").strip().title()
            remover_aluno_em_disciplina(nome_disciplina, dicionario_aluno, dicionario_turma)
        elif opcao_menu_coordenador_editar_turma == '0':
            break
        else:
            print("Opção inválida! Digite um opção valida")



def mudar_prof_uma_disciplina(nome_disciplina, dicionario_turma, dicionario_professor):
    # verifica dict turma
    flag_verifica_dicionario_vazio_turma = verifica_dicionario_vazio(dicionario_turma)
    if flag_verifica_dicionario_vazio_turma:
        # verifica dict prof
        flag_verifica_dicionario_vazio_prof = verifica_dicionario_vazio(dicionario_professor)
        if flag_verifica_dicionario_vazio_prof:
            # verifica se a disciplina existe
            flag_verifica_disciplina = False
            for nome_turma in dicionario_turma.keys():
                # verifica se o nome digitado existe em dicionario turmas
                if nome_turma == nome_disciplina:
                    flag_verifica_disciplina = True
            if flag_verifica_disciplina:
                print("Digite o nome do prof que deseja para substituir o professor: ")
                nome_professor = input(">>> ").strip().title()
                conta_nomes = verifica_dois_nomes_iguais(nome_professor, dicionario_professor)
                mostrar_pessoas_nomes_iguais(nome_professor, dicionario_professor)
                if conta_nomes == 1:
                    print("Confirmação!")
                # percorrendo as pessoas com esse nome
                print(f"Digite a matricula do(a) {nome_professor} que deseja substituir: ")
                matricula = input(">>> ").strip()
                # verificações na matricula
                flag_verifica_matricula = verifica_matricula(matricula, dicionario_professor)
                # verifica se o prof digitado existe em dict prof
                if flag_verifica_matricula:
                    for chave_prof in dicionario_turma[nome_disciplina].keys():
                        # guardo os valores, excluo o professor antigo
                        copia_dicionario = dicionario_turma[nome_disciplina][chave_prof][dicionario_professor[chave_prof]].copy()
                        del dicionario_turma[nome_disciplina][chave_prof]
                        dicionario_turma[nome_disciplina] = {}
                        dicionario_turma[nome_disciplina] = {matricula: {}}
                        dicionario_turma[nome_disciplina][matricula] = {dicionario_professor[matricula]: copia_dicionario}
                        
                        break
                    # salvo no json turma e professor
                    nome_do_arquivo = 'dicionario_turma'
                    salvar_dicionarios(dicionario_turma, nome_do_arquivo)
                    print("Professor editado com sucesso!")
            else:
                print("A disciplina não existe")

def adicionar_aluno_em_disciplina(disciplina, dicionario_aluno, dicionario_turma):
    # verificações nos dicts
    flag_verificacoes_dicionario_aluno_em_disciplina = verificacoes_dicionario_aluno_em_disciplina(disciplina, dicionario_aluno, dicionario_turma)
    if flag_verificacoes_dicionario_aluno_em_disciplina:

        # verifica a disciplina e mostra os alunos cadastrados para a pesquisa
        flag_mostra_alunos_disciplina_e_verifica, nome_aluno_adicionar, matricula = mostra_alunos_disciplina_e_verifica(disciplina, dicionario_turma, dicionario_aluno)
        if flag_mostra_alunos_disciplina_e_verifica:

            flag_verifica_aluno_ja_cadastrado_e_cadastra = verifica_aluno_ja_cadastrado_e_cadastra(disciplina, nome_aluno_adicionar, matricula, dicionario_turma, dicionario_aluno)
            if flag_verifica_aluno_ja_cadastrado_e_cadastra:

                nome_do_arquivo = 'dicionario_turma'
                salvar_dicionarios(dicionario_turma, nome_do_arquivo)

# funções para auxiliar adicionar_aluno_em_disciplina                   
def verificacoes_dicionario_aluno_em_disciplina(disciplina, dicionario_aluno, dicionario_turma):
    flag_verifica_dicionario_vazio_aluno = verifica_dicionario_vazio(dicionario_aluno)
    if flag_verifica_dicionario_vazio_aluno:
        flag_verifica_dicionario_vazio_turma = verifica_dicionario_vazio(dicionario_turma)
        if flag_verifica_dicionario_vazio_turma:
            flag_verifica_disciplina_existe = False
            for nome_disciplina in dicionario_turma.keys():
                # verifica se a disciplina existe mesmo
                if nome_disciplina == disciplina:
                    flag_verifica_disciplina_existe = True
            if flag_verifica_disciplina_existe == True:
                return flag_verifica_disciplina_existe
            else:
                print("Disciplina não cadastrada!")
        else:
            print("Não existem turmas cadastradas!")
    else:
        print("Não existem aluno cadastrados!")

def mostra_alunos_disciplina_e_verifica(disciplina, dicionario_turma, dicionario_aluno):
    # printa os alunos na disciplina
    print(F"{'Alunos na disciplina':-^35}")
    for siape, prof_aluno in dicionario_turma[disciplina].items():
        for professor, alunos_lista in prof_aluno.items():
            print(f"{'Matrícula:':<12} Aluno:")
            for aluno in alunos_lista:
                for matricula, nome_aluno in aluno.items():
                    print(f"{matricula:<12}",nome_aluno)

    print("Digite o nome do aluno que deseja adicionar na disciplina: ")
    nome_aluno_adicionar = input(">>> ").strip().title()
    conta_nomes = verifica_dois_nomes_iguais(nome_aluno_adicionar, dicionario_aluno)
    mostrar_pessoas_nomes_iguais(nome_aluno_adicionar, dicionario_aluno)
    if conta_nomes == 1:
        print("Confirmação!")
    # percorrendo as pessoas com esse nome
    print(f"Digite a matricula do(a) {nome_aluno_adicionar} que deseja adicionar: ")
    matricula = input(">>> ").strip()
    # verificações na matricula
    flag_verifica_matricula = verifica_matricula(matricula, dicionario_aluno)
    # verifica se o prof digitado existe em dict prof
    if flag_verifica_matricula:
        return True, nome_aluno_adicionar, matricula

def verifica_aluno_ja_cadastrado_e_cadastra(disciplina, nome_aluno_adicionar, matricula, dicionario_turma, dicionario_aluno):
    flag_verifica_aluno_ja_cadastrado = False
    for chave_prof, nome_prof in dicionario_turma[disciplina].items():
        # percorre os alunos desse professor
        for prof, lista_alunos in nome_prof.items():
            for alunos in dicionario_turma[disciplina][chave_prof][prof]:
                for chave_aluno in alunos.keys():
                    # se a matricula e a matricula do aluno na disciplina for igual
                    if chave_aluno == matricula:
                        flag_verifica_aluno_ja_cadastrado = True
    if flag_verifica_aluno_ja_cadastrado:
        print("O aluno já existe na disciplina!")
    else:
        dicionario_novo_aluno = {matricula: dicionario_aluno[matricula]}
        lista_alunos.append(dicionario_novo_aluno)
        return dicionario_turma


def remover_aluno_em_disciplina(disciplina, dicionario_aluno, dicionario_turma):
    flag_verificacoes_dicionario_aluno_em_disciplina = verificacoes_dicionario_aluno_em_disciplina(disciplina, dicionario_aluno, dicionario_turma)
    if flag_verificacoes_dicionario_aluno_em_disciplina:
        flag_mostra_alunos_e_verifica_remover_aluno, matricula = mostra_alunos_e_verifica_remover_aluno(disciplina, dicionario_turma)
        if flag_mostra_alunos_e_verifica_remover_aluno:
            remove_aluno_aluno_em_disciplina_funcao(disciplina, matricula, dicionario_turma)
            nome_do_arquivo = 'dicionario_turma'
            salvar_dicionarios(dicionario_turma, nome_do_arquivo)
# funções para auxiliar o remover_aluno_em_disciplina
def mostra_alunos_e_verifica_remover_aluno(disciplina, dicionario_turma):
    # printa os alunos da disciplina
    print(F"{'Alunos na disciplina':-^35}")
    for siape, prof_aluno in dicionario_turma[disciplina].items():
        for professor, alunos_lista in prof_aluno.items():
            print(f"{'Matrícula:':<12} Aluno:")
            for aluno in alunos_lista:
                for matricula_alunos, nome_aluno in aluno.items():
                    print(f"{matricula_alunos:<12}",nome_aluno)

    print("Digite a matricula do aluno que deseja remover da disciplina: ")
    matricula = input(">>> ").strip()
    # verificações na matricula
    flag_verifica_matricula = False
    for matricula_alunos, nome_alunos in aluno.items():
        if matricula_alunos == matricula:
            flag_verifica_matricula = True
    # verifica se o prof digitado existe em dict turma
    if flag_verifica_matricula:
        return True, matricula
    else:
        print("Matricula incorreta!")

def remove_aluno_aluno_em_disciplina_funcao(disciplina, matricula, dicionario_turmas):
    for siape, prof_aluno in dicionario_turma[disciplina].items():
        for professor, alunos_lista in prof_aluno.items():
            for aluno in alunos_lista:
                for matricula_alunos, nome_aluno in aluno.items():
                    if int(matricula_alunos) == int(matricula):
                        alunos_lista.remove(aluno)
    return dicionario_turmas


def ver_turmas(nome_disciplina, dicionario_turma):
    print(35*'-')
    flag_verifica_turma_vazio = verifica_dicionario_vazio(dicionario_turma)
    if flag_verifica_turma_vazio:
        flag_verifica_disciplina = False
        for nome_turma in dicionario_turma.keys():
            # verifica se o nome digitado existe em dicionario turmas
            if nome_turma == nome_disciplina:
                flag_verifica_disciplina = True
        if flag_verifica_disciplina:
            for disciplina, dados_turma in dicionario_turma.items():
                print(f"Disciplina: {disciplina.upper()}")
                print()
                for siape, prof_aluno in dados_turma.items():
                    print(f"{'SIAPE:':<8}Professor:")
                    print(f"{siape:<8}", end = "")
                    for professor, alunos_lista in prof_aluno.items():
                        print(professor)
                        print()
                        print(f"{'Matrícula:':<12} Aluno:")
                        for aluno in alunos_lista:
                            for matricula, nome_aluno in aluno.items():
                                print(f"{matricula:<12}",nome_aluno)
        else:
            print("A disciplina não está cadastrada!")
    else:
        print("Não existem turmas cadastradas!")
    print(35*'-')

def ver_todas_as_turmas(dicionario_turmas):
    print(35*'-')
    print("Disciplinas:")
    for nome_disciplina in dicionario_turmas.keys():
        print(f"{nome_disciplina.upper()}")


# verificações de pessoas com nomes iguais
def verifica_dois_nomes_iguais(nome, dicionario):
    conta_nomes = 0
    # verifico se existem mais de uma pessoa com o mesmo nome
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
    # verifico se a matricula existe no dicionario
    for chaves in dicionario.keys():
        if str(chaves) == matricula:
            flag = True
    return flag

def verifica_dicionario(nome, dicionario):
    # verifico se o dicionario é vazio e se a pessoa existe no dicionario
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
    # verifica se o nome antiga a norma padrão (composto e sem números)
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
    # verifico se o prof está cadastrado em alguma disciplina
    for chave_turma in dicionario.keys():
        for chave_prof in dicionario[chave_turma].keys():
            if int(chave_prof) == int(matricula):
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
                nome_do_arquivo = 'dicionario_turma'
                editar_turma(dicionario_turma, dicionario_professor, nome_do_arquivo)
            elif opcao_menu_coordenador == '3':
                print("Digite o nome da disciplina que deseja ver: ")
                nome_disciplina = input(">>> ").strip().title()
                ver_turmas(nome_disciplina, dicionario_turma, )
            elif opcao_menu_coordenador == '4':
                ver_todas_as_turmas(dicionario_turma)
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
                print("Digite o nome do professor que deseja visualizar as turmas: ")
                nome_professor = input(">>> ").strip().title()
                visualizar_turmas_professor_especifico(nome_professor, dicionario_professor, dicionario_turma)

            elif opcao_menu_professor == '6':
                print("Digite o nome do professor que deseja visualizar as turmas: ")
                nome_professor = input(">>> ").strip().title()
                visualizar_alunos_professor_especifico(nome_professor, dicionario_professor, dicionario_turma)
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
        

