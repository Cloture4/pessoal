from datetime import datetime,timedelta
def main():   

    ##############################################################################################################################
    #Função Principal: Cérebro do programa, responsável pelo armazenamento,manipulação,gravação e leitura de dados em ultimo nível
    ##############################################################################################################################
    disciplinas = LerArquivo('disciplinascadastradas.txt')
    unitario = LerArquivo('unitarioscadastrados.txt')
    semanal = LerArquivo('semanaiscadastrados.txt')
    #####################################################################################################################################
    #Os dados são gravados e armazenados em 3 listas: Uma lista das disciplinas cadastradas, uma lista para compromissos que se repetem
    #e uma lista para compromisso que não se repetem. Aqui os dados acabaram de ser recuperados do arquivo txt
    ######################################################################################################################################
    print('\n'*5) #Limpa tela :)
    MontarCalendario(unitario,semanal,'1') #Chama a função que imprime o calendário da semana atual assim que o programa é aberto!
    while True:
        opc = menu()
        if opc == '1':
            #Função responsável por criar,editar e excluir as diciplinas
            disciplinas,semanal = TratamentoDasDisciplinas(disciplinas,semanal)
        elif opc == '2':
                        #Função responsável por criar,editar e excluir todos os tipos de compromisso
            unitario,semanal = TratamentoDeCompromissos(unitario,semanal,disciplinas)
        elif opc == '3':
            MontarCalendario(unitario,semanal,0)
        elif opc == '4':
            #Ao encerar o programa, salva as informações em arquivos de texto separados, uma para cada lista de dados!
            EditarArquivo(disciplinas,'d')
            EditarArquivo(unitario,'u')
            EditarArquivo(semanal,'s')
            break
            

def LerArquivo(nomarquivo):
    #######################################################################################
    #Função responsável por recuperar as informações dos arquivos e retransformar em listas
    #######################################################################################
    infosevento = []
    allarquivo = []
    #################################################################################################################
    # abre o arquivo com as variaveis se ele existir e retorna uma tupla com essas informações, em caso negativo cria.
    # Itera o arquivo e identifica pela formatação do arquivo se os dados devem ser retransformador como strings ou listas
    #################################################################################################################
    try:
        infocadastrada = (open(nomarquivo,'r'))
        stringues = True
        for line in infocadastrada:
            info = line.split(',')
            if info[0] == '\n':
                allarquivo += [infosevento] 
                infosevento = []
                stringues = True
                continue
            if stringues == True:
                infosevento += info[:len(info)-1]
                stringues = False
            else:
                infosevento += [info[:len(info)-1]]                
    except FileNotFoundError:
        #Se o arquivo não existir ele é criado
        infocadastrada = (open(nomarquivo,'w'))

    infocadastrada.close()
    return allarquivo

def menu():
    while True:
        #Menu, apenas repassa as informações para função principal e guia o usuario!
        print('\n'*5)
        print('Bom dia! O que deseja fazer agora?')
        print('1 - Adicionar, Editar ou Excluir disciplinas ao banco de dados.')
        print('2 - Adicionar, Editar ou Excluir compromissos ao seu calendario')
        print('3 - Acessar sua programação')
        print('4 - Sair')
        while True:
            opc = input()
            if opc == '1':
                return '1'
            elif opc == '2':
                return '2'
            elif opc == '3':
                return '3'
            elif opc == '4':
                return '4'
            else:
                print('Digite uma opção válida! (1, 2, 3 ou 4)')
            
def TratamentoDasDisciplinas(disciplinas,semanal):
    #################################################################################################################################################
    #Função responsável por gerenciar as disciplinas e os compromissos semanais oriundos delas.
    #########################################################################################################

    print('\n'*10)
    print('1 - Inserir uma disciplina nova')
    print('2 - Editar informações de uma disciplina')
    print('3 - Excluir uma disciplina')
    print('4 - Voltar')

    while True:
        opc = input()
        if opc == '1':
            while True:
                #Coleta as informações pro cadastro de disciplinas
                #Isto é: Código,Nome(Importante para exibição),Turma,Dias da Semana de Aula(Importante para exibição),
                #Horário das aulas(Importante para exibição) e Periodo(Importante para exibição)
                #Enfase para a função ValidacaoInput(), que verifica o tipo de dado da entrada e se é compativel com o que
                #está sendo pedido.

                print('\n'*10)
                nomedisciplinascadastradas = []
                coddisciplinascadastradas = []
                print('Disciplinas já cadastradas:\n')
                for disciplina in disciplinas:
                    print(disciplina[1])
                    nomedisciplinascadastradas += [disciplina[1].lower()]
                    coddisciplinascadastradas += [disciplina[0].lower()]
                print('\nDigite as informações de cadastro.\n')
                while True:
                    cod = input('Digite o código da disciplina: ')
                    check = ValidacaoInput(cod) 
                    if check == -1: break
                    elif check == -2: return disciplinas,semanal
                if cod.lower() in coddisciplinascadastradas:
                    print('Código ja vinculado a uma disciplina! Códigos e nomes devem ser únicos!')
                    return disciplinas,semanal
                while True:
                    nome = input('Digite o nome da disciplina: ')
                    check = ValidacaoInput(nome) 
                    if check == -1: break
                    elif check == -2: return disciplinas,semanal
                if nome.lower() in nomedisciplinascadastradas:
                    print('Nome ja vinculado a uma disciplina! Códigos e nomes devem ser únicos!')
                    return disciplinas,semanal
                while True:
                    turma = input('Digita o nome da turma: ')
                    check = ValidacaoInput(turma) 
                    if check == -1: break
                    elif check == -2: return disciplinas,semanal
                while True:
                    dias = input('Digite os dias da semana separados em espaço (Ex: Terça Quinta): ').split()
                    check = ValidacaoInput(dias,'dia') 
                    if check == -1: break
                    elif check == -2: return disciplinas,semanal
                while True:
                    horario = input('Digite o horário da aula e a duração em horas nessa ordem(Só aceitam valores inteiros - Ex: 16 1): ').split()
                    check = ValidacaoInput(horario,'horario') 
                    if check == -1: break
                    elif check == -2: return disciplinas,semanal
                while True:
                    periodo = input('Digite previsao de começo e término da disciplina (Ex: 23/04/22 22/07/22): ').split()
                    check = ValidacaoInput(periodo,'periodo') 
                    if check == -1: break
                    elif check == -2: return disciplinas,semanal
                geral = [cod,nome,turma,dias,horario,periodo]
                disciplinas += [geral]
                
                ###################################################
                #Permite que usuario cadastre outra disciplina sem que necessariamente volte ao menu de escolhas
                again = ''
                while again.lower() != 's' and again.lower() != 'n':
                    again = input('Deseja adicionar outra disciplina?(s/n) ')
                    if again == 'n': 
                        return disciplinas,semanal
                    elif again == 's':
                        break
                    else:
                        print('Digite "s" ou "n" ')

        elif opc == '2':
            #Codigo responsável por alterar informaçoes de disciplinas ja cadastradas e armazenadas na respectiva lista
            while True:
                print('Informe de qual disciplina você quer alterar os dados: ')
                disciplina = OpcaoExistente(disciplinas,1)
                if disciplina != -1:
                    print('O que você deseja alterar?: \n')
                    for info in disciplinas[disciplina]:
                        print(info)
                    print()
                    print('1 - Código da disciplina \n2 - Nome da disciplina \n3 - Nome da turma \n4 - Dias da semana \n5 - Horarios \n6 - Periodo')
                    opc = input('\n')
                    if opc != '1' and opc != '2' and opc != '3' and opc != '4' and opc != '5' and opc != '6':
                        again = ''
                        while again.lower() != 's' and again.lower() != 'n':
                            again = input('Atributo inválido ou ausente. Ainda deseja alterar algum dado? ')
                            if again == 'n': return disciplinas,semanal
                            elif again == 's': continue
                            else: print('Digite "s" ou "n"')
                    else:
                        ####################################################################################
                        #Exibe o atributo a ser alterado e verifica/altera aonde a alteração deve ser feita nas listas
                        print('Você vai editar: ',disciplinas[disciplina][int(opc)-1])
                        if opc == '1':
                            while True:
                                cod = input('Digite o código da disciplina: ')
                                check = ValidacaoInput(cod)
                                if check == -1: break
                                elif check == -2: return disciplinas,semanal
                            disciplinas[disciplina][int(opc)-1] = cod
                        elif opc == '2':
                            while True:
                                nome = input('Digite o nome da disciplina: ')
                                check = ValidacaoInput(nome) 
                                if check == -1: break
                                elif check == -2: return disciplinas,semanal
                            disciplinas[disciplina][int(opc)-1] = nome
                        elif opc == '3':
                            while True:
                                turma = input('Digita o nome da turma: ')
                                check = ValidacaoInput(turma) 
                                if check == -1: break
                                elif check == -2: return disciplinas,semanal
                            disciplinas[disciplina][int(opc)-1] = turma
                        elif opc == '4':
                            while True:
                                dias = input('Digite os dias da semana separados em espaço (Ex: Terça Quinta): ').split()
                                check = ValidacaoInput(dias,'dia') 
                                if check == -1: break
                                elif check == -2: return disciplinas,semanal
                            disciplinas[disciplina][int(opc)-1] = dias
                        elif opc == '5':
                            while True:
                                horario = input('Digite o horário da aula e a duração em horas nessa ordem (Só aceitam valores inteiros - Ex: 16 1): ').split()
                                check = ValidacaoInput(horario,'horario') 
                                if check == -1: break
                                elif check == -2: return disciplinas,semanal
                            disciplinas[disciplina][int(opc)-1] = horario
                        elif opc == '6':
                            while True:
                                periodo = input('Digite previsao de começo e término da disciplina (Ex: 23/04/22 22/07/22): ').split()
                                check = ValidacaoInput(periodo,'periodo') 
                                if check == -1: break
                                elif check == -2: return disciplinas,semanal
                            disciplinas[disciplina][int(opc)-1] = periodo
                        nomedossemanais = []

                        #Se uma disciplina que está cadastrada nos compromissos semanais tem um atributo alterado,
                        #essa parte do código garante que ele seja alterado na lista de compromissos semanais
                        for compromisso in semanal:
                            nomedossemanais += [compromisso[0].lower()]
                        if disciplinas[disciplina][1].lower() in nomedossemanais:
                            alterar = nomedossemanais.index(disciplinas[disciplina][1].lower())
                            if opc == '2':
                                semanal[alterar][0] = disciplinas[disciplina][1]
                            elif opc == '4':
                                semanal[alterar][1] = disciplinas[disciplina][3]
                            elif opc == '5': 
                                semanal[alterar][3] = disciplinas[disciplina][4]
                            elif opc == '6':
                                semanal[alterar][2] = disciplinas[disciplina][5]
                        print('Dados atualizados!')
                        return disciplinas,semanal

        elif opc == '3':
            #Responsável pela exclusão de disciplinas que o usuario desejar.
            #Enfase para a função OpcaoExistente ja utilizada antes, ela permite que o usuario escolha apenas disciplinas
            #que ja foram cadastradas as mostrando quando necessário.
            while True:
                print('Informe de qual disciplina você quer excluir: ')
                disciplina = OpcaoExistente(disciplinas,0)
                if disciplina != -1:
                    ctz = input('Você tem certeza que deseja excluir essa disciplina da sua base de dados? Digite exatamente "SIM" se deseja prosseguir (OS DADOS SERÃO REMOVIDOS PERMANENTEMENTE\n E NÃO SERA CAPAZ RESTAURA-LOS NEM QUE JESUS VOLTE!) ')
                    if ctz == 'SIM':
                        del disciplinas[disciplina]
                        print('Apagado :)')
                        break
                return disciplinas,semanal
        elif opc == '4':
            #Volta ao menu principal
            return disciplinas,semanal
        else: print('Digite uma opção válida! (1, 2, 3 ou 4)') 


def TratamentoDeCompromissos(unitario,semanal,disciplinas):
    ############################################################################################################################
    #Função responsável pelo cadastro,edição e exclusão das informações que realmente vao ser exibidas quando o usuario solicitar, vindo elas
    #do banco de disciplinas criado na função que lida com elas ou não
    ############################################################################################################################
    compromissos = unitario + semanal
    ############################################################################################################################    #Estrutura de armazenamento de informações baseado na frequência do compromisso a ser adicionado, se um compromisso
    #tem frequencia semanal ele é adicionado numa lista junto a semelhantes, caso contrario o mesmo para compromissos
    #sem frêquencia semanal.
    ###########################################################################################################################
    print('O que deseja fazer: ')
    print('1 - Adicionar compromissos')
    print('2 - Editar Compromissos')
    print('3 - Excluir Compromissos')
    print('4 - Voltar')
    while True: 
        opc = input()
        if opc == '1':
            print('\n'*5)
            print('1 - Adicionar novo compromisso')
            print('2 - Adicionar disciplina do banco de dados aos compromisso')
            print('3 - Voltar')
            opc = input()
            while True: 
                ###########################################################################################################################################
                #Coleta as informações necessarias para o cadastro e exibição no caléndario: Nome,Lembretes(Exclusivo de compromissos sem frequencia)
                #Datas e Horário.
                ###########################################################################################################################################
                if opc == '1':
                    nomcompromissoscadastrados = []
                    for compromisso in compromissos:
                        nomcompromissoscadastrados += [compromisso[0].lower()]

                    while True:
                        nome = input('Digite o nome do compromisso: ')
                        check = ValidacaoInput(nome) 
                        if check == -1: break
                        elif check == -2: return unitario,semanal
                    if nome.lower() in nomcompromissoscadastrados:
                        print('Compromisso já cadastrado! So é possível cadastrar compromissos com nomes diferentes')
                        return unitario,semanal

                    while True:
                        horario = input('Hora de começo e duração separado por espaço (Somente numeros inteiros. Ex: 16 1) ').split()
                        check = ValidacaoInput(horario,'horario') 
                        if check == -1: break
                        elif check == -2: return unitario,semanal

                    while True:
                        recorrencia = input('O compromisso tem recorrência semanal?(Se não quiser que ela seja removido passados a data digite "s"(s/n)) ')
                        check = ValidacaoInput(recorrencia,'sn') 
                        if check == -1: break
                        elif check == -2: return unitario,semanal

                    ##################################################################################################################
                    #Enfase para a função SobrescreverCompromisso(), ela é capaz de verificar sobreposição de eventos durante o cadastro
                    # ou atualização de informações e impedir ou não o usuario de sobrescrever um compromisso
                    ####################################################################################################################
                    if recorrencia == 'n':
                        while True:
                            dia = input('Data do compromisso (Ex: "25/07/24"): ')
                            check = ValidacaoInput(dia,'diamesano') 
                            if check == -1: break
                            elif check == -2: return unitario,semanal
                            if ValidacaoInput(dia,'diamesano') == -2: return unitario,semanal
                        while True:
                            lembrete = input('Deseja adicionar um lembrete? (s/n) ')
                            check = ValidacaoInput(lembrete,'sn') 
                            if check == -1: break
                            elif check == -2: return unitario,semanal
                        compromissounitario = [nome,lembrete,dia,horario]
                        check = SobrescreverCompromisso(compromissounitario,compromissos)
                        if check == -1:
                            print()
                        elif check == -2:
                            return unitario,semanal
                        else:
                            if check[1] == 's':
                                limparhorario = check[0][3]
                                unitario += [['-------','n',dia,limparhorario]]
                            elif check[1] == 'u':
                                unitario.remove(check[0])
                            print('O compromisso:-',check[0][0],'- foi sobrescristo no horário em questão!')
                        unitario += [compromissounitario]
                        print('Adicionado')
                        return unitario,semanal
                    else:
                        while True:
                            dia = input('Dia(s) da semana separados por espaço sem acentos e caracteres especiais: ').split()
                            check = ValidacaoInput(dia,'dia') 
                            if check == -1: break
                            elif check == -2: return unitario,semanal

                        hoje = str(datetime.strftime(datetime.today(),'%d/%m/%y'))
                        compromissosemanal = [nome,dia,[hoje,'31/12/30'],horario]
                        semanal += [compromissosemanal]
                        print('Adicionado')
                        return unitario,semanal
                elif opc == '2':
                    #########################################################################################################
                    #Parte do código responsavel por adicionar enfim, disciplinas cadastradas anteriormente a um compromisso
                    #que vai ser exibido quando o usuario solicitar
                    #########################################################################################################
                    if len(disciplinas) == 0:
                        print('Nenhuma disciplina cadastrada')
                        return unitario,semanal
                    print('Qual disciplina você quer adicionar? ')
                    disciplina = OpcaoExistente(disciplinas,0)
                    if disciplina != -1:
                        for compromisso in compromissos:
                            if disciplinas[disciplina][1].lower() == compromisso[0].lower():
                                print('Disciplina já cadastrada!')
                                return unitario,semanal
                        compromissosemanal = [disciplinas[disciplina][1],disciplinas[disciplina][3],disciplinas[disciplina][5],disciplinas[disciplina][4]]
                        semanal += [compromissosemanal]
                        print('Adicionado!')
                    return unitario,semanal
                elif opc == '3':
                    #Volta ao menu principal
                    return unitario,semanal
                else:
                    print('Digite uma opção válida! (1, 2 ou 3)')
                    continue
                
        elif opc == '2':
            ###############################################################################################################
            #Parte do código responsável por identificar,localizar e alterar informações de compromissos ja cadastrados
            ############################################################################################################

            print('Qual compromisso você deseja editar? ')
            compromisso = OpcaoExistente(compromissos,0)
            if compromisso != -1:
                while True:
                    print('O que você deseja alterar?\n ')
                    for info in compromissos[compromisso]:
                        print(info)
                    print()
                    print('1 - Nome')
                    print('2 - Adicionar lembrete ou não')
                    print('3 - Dia')
                    print('4 - Horário')
                    print('5 - Voltar')
                    opc = input()
                    if opc == '1':
                        while True:
                            nome = input('Digite o nome do compromisso: ')
                            check = ValidacaoInput(nome) 
                            if check == -1: break
                            elif check == -2: return unitario,semanal
                        compromissos[compromisso][0] = nome
                    elif opc == '2':
                        while True:
                            lembrete = input('Deseja adicionar lembrete? (s/n) ')
                            check = ValidacaoInput(lembrete,'sn')
                            if check == -1: break
                            elif check == -2: return unitario,semanal
                        compromisso[compromisso][1] = lembrete
                    elif opc == '3':
                        if type(compromissos[compromisso][1]) == str:
                            while True:
                                dia = input('Data do compromiso (Ex: "25/07/22"): ')
                                check = ValidacaoInput(dia,'diamesano')
                                if check == -1: break
                                elif check == -2: return unitario,semanal
                            reverser = compromissos[compromisso][len(compromissos[compromisso])-2]
                            compromissos[compromisso][len(compromissos[compromisso])-2] = dia
                            check = SobrescreverCompromisso(compromissos[compromisso],compromissos)
                            if check == -1:
                                print()
                            elif check == -2:
                                print('Operação Cancelada!')
                                compromissos[compromisso][len(compromissos[compromisso])-2] = reverser
                                return unitario,semanal
                            else:
                                if check[1] == 's':
                                    limparhorario = check[0][3]
                                    unitario += [['-------','n',dia,limparhorario]]
                                if check[1] == 'u':
                                    unitario.remove(check[0])
                                print('O compromisso:-',check[0][0],'- foi sobrescristo no horário em questão!')                      
                                unitario += [compromissos[compromisso]]
                                unitario.remove(compromissos[compromisso])
                                return unitario,semanal
                        else:
                            while True:
                                dia = input('Dia(s) da semana separados em espaço sem acentos nem caracteres especiais: ').split()
                                check = ValidacaoInput(dia,'dia') 
                                if check == -1: break
                                elif check == -2: return unitario,semanal
                            compromissos[compromisso][len(compromissos[compromisso])-3] = dia

                    elif opc == '4':
                        while True:
                            horario = input('Hora de começo e duração separado por espaço (Somente numeros inteiros. Ex: 16 1) ').split()
                            check = ValidacaoInput(horario,'horario') 
                            if check == -1: break
                            elif check == -2: return unitario,semanal
                        if type(compromissos[compromisso][1]) == str:
                            reverser = compromissos[compromisso][len(compromissos[compromisso])-1]
                            compromissos[compromisso][len(compromissos[compromisso])-1] = horario
                            check = SobrescreverCompromisso(compromissos[compromisso],compromissos)
                            if check == -1:
                                print()
                            elif check == -2:
                                print('Operação Cancelada!')
                                compromissos[compromisso][len(compromissos[compromisso])-1] = reverser
                                return unitario,semanal
                            else:
                                if check[1] == 's':
                                    limparhorario = check[0][3]
                                    unitario += [['-------','n',compromissos[compromisso][2],limparhorario]]
                                if check[1] == 'u':
                                    unitario.remove(check[0])
                                print('O compromisso:-',check[0][0],'- foi sobrescristo no horário em questão!')
                                unitario += [compromissos[compromisso]]
                                unitario.remove(compromissos[compromisso])
                                return unitario,semanal
                        else:
                            compromissos[compromisso][len(compromissos[compromisso])-1] = horario

                    elif opc == '5':
                        break
                    else:
                        print('Opção Inexistente! ')
                        continue
                    print('Atualizado!')
                    break
        elif opc == '3':
            ####################################################################################################
            #Exclui compromissos que o usuario desejar
            #################################################################################################
            print('Digite qual compromisso você deseja excluir: \n')
            compromisso = OpcaoExistente(compromissos,0)
            if compromisso != -1:
                print('O compromisso:-',compromissos[compromisso][0],'- foi excluido!')
                if compromissos[compromisso-1][0] == '-------':
                    compromissos.pop(compromisso)
                    compromisso -= 1
                compromissos.pop(compromisso)
        elif opc == '4':
            return unitario,semanal
        else:
            print('Digite uma opção valida!(1,2,3 ou 4!)')
            continue

        ######################################################################################################
        #Em alguns momentos da função os compromissos semanais e unitarios são agregados a fim de realizar qualquer
        #necessidade do código, aqui eles são novamente separados e retornados se não fora feito antes
        ###################################################################################################


        unitario = []
        semanal = []
        for compromisso in compromissos:
            if type(compromisso[1]) == str:
                unitario += [compromisso]
            else:
                semanal += [compromisso]
        return unitario,semanal



def ValidacaoInput(entrada,tipo='nomes'):

    ##########################################################################################################################################
    #Função responsável por validar as entradas do usuario. Ela recebe a entrada e o tipo da entrada(caso não seja fornecido o tipo
    #é analisada como nomes) e valida se as informações fazem sentido e estão de acordo com a formatação exigida do programa.
    #Ela é capaz de analisar e identificar: Espaços Vazios, o caracter "b" que cancela qualquer operação em andamento, Datas, Horas Existentes,
    #Respostas de Sim ou Não
    ###########################################################################################################################################

    if type(entrada) == list:
        if entrada[0] == 'b':
            print('Operação Cancelada!')
            return -2
    else:
        if entrada == 'b':
            print('Operação Cancelada!')
            return -2
    if entrada == '' or entrada == '\n' or entrada == []:
        print('Entrada obrigatória, não é possivel deixar em branco. Digite novamente ou digite "b" para sair')
        return 0
    elif tipo == 'nomes':
        if len(entrada) > 13:
            print('Por motivos de formatação, só são aceitos nomes com até 13 caracteres! :)')
            return 1
        return -1
    elif tipo == 'dia':
        for dia in entrada:
            existe = 'n'
            diasdasemana = ['domingo','segunda','terca','quarta','quinta','sexta','sabado']
            for diadasemana in diasdasemana:
                if dia.lower() == diadasemana:
                    existe = 's'
                    break
            if existe == 'n':
                print('Dia da semana inexistente! Digite novamente ou digite "b" para sair')
                return 1 
        return -1
    elif tipo == 'diamesano':
        try:
            testedata = datetime.strptime(entrada,'%d/%m/%y')
        except ValueError:
            print('Data inexistente. Digite novamente ou digite "b" para sair')
            return 1
        return -1
    elif tipo == 'horario':
        if len(entrada) != 2:
            print('Quantidade de dados incompatível. Digite novamente ou digite "b" para sair')
            return 10
        for hora in entrada:
            try:
                hora = int(hora)
            except ValueError:
                print('Dados invalidos! Digite novamente ou digite "b" para sair')
                return 20
        if not 24>= hora >= 0:
            print('Duração Irregular. Digite novamente ou digite "b" para sair')
            return 200
        try:
            ehhora = datetime.strptime(entrada[0],'%H')
            return -1
        except ValueError:
            print('Horário Inexistente ou Formato inadequado. Digite novamente ou digite "b" para sair')
            return 2            
    elif tipo == 'periodo':
        if len(entrada) != 2:
            print('Quantidade de dados incompatível. Digite novamente ou digite "b" para sair')
            return 10
        datas = []
        for data in entrada:
            try:
                datas += [datetime.strptime(data,'%d/%m/%y')]
            except ValueError:
                print('Data inexistentes ou em formato inadequado. Digite novamente ou digite "b" para sair')
                return 3
        if datas[0] > datas[1]:
            print(datas[0],datas[1])
            print('A primeira data tem que ser necessariamente anterior à ou igual a segunda data!. Digite novamente ou digite "b" para sair')
            return 3
        return -1
    elif tipo == 'sn':
        if len(entrada) != 1:
            print('Digite "s" ou "n" ! ')
            return 4
        elif entrada.lower() != 's' and entrada.lower() != 'n':
            print('Digite "s" ou "n" ! ')
            return 4
        else:
            return -1

    else: 
        return -1


def OpcaoExistente(iteravel,posnome):
    ########################################################################################################################
    #Função responsável por verificar as opções existentes para uma operação qualquer, ou seja, quais disciplinas/compromissos
    #existem para que possam ser alterados/excluidos/não repetidos
    ##########################################################################################################################
    #Enfase na váriavel skip necessaria para situações onde compromissos foram sobrescritos e o compromisso '---------' foi 
    #Adicionado para limpar o caléndario!

    skip = 0
    opcoesvalidas = []
    for item in iteravel:
        if item[posnome] == '-------':
            skip += 1
            continue
        opcoesvalidas += [item[posnome].lower()]
        print(item[posnome])
    print()
    opc = input()
    if opc.lower() not in opcoesvalidas:
        print('Opção Invalida')
        return -1
    else:
        for item in range(len(opcoesvalidas)):
            if opc.lower() == opcoesvalidas[item]:
                return item+skip

        
def EditarArquivo(eventos,identificador):
    ##########################################################################################################################
    #Função responsavel por gravar as informações de disciplinas,compromissos unitarios e compromissos semanais em arquivos txt
    #Para que possam ser carregadas ao iniciar o programa!
    #Distingue como os elementos vão ser gravados pelo seu tipo e formata o arquivo de texto de acordo
    ############################################################################################################################

    try:
        if identificador == 'd':
            eventoscadastrados = open('disciplinascadastradas.txt','w')
        elif identificador == 's':
            eventoscadastrados = open('semanaiscadastrados.txt','w')
        elif identificador == 'u':
            eventoscadastrados = open('unitarioscadastrados.txt','w')
    except IndexError:
        return 
    for evento in eventos:
        
        for item in evento:

            if type(item) == str:
                eventoscadastrados.write(item)
                eventoscadastrados.write(',')
        
            if type(item) == list:
                eventoscadastrados.write('\n')

                for elemento in item:
                    eventoscadastrados.write(elemento)
                    eventoscadastrados.write(',')
        eventoscadastrados.write('\n\n')
    
    eventoscadastrados.close()

def SobrescreverCompromisso(novocompromisso,compromissos):
    ################################################################################################################
    #Função responsável por identificar possivel sobreposições de compromissos em dia e horário, confirma com o usuario
    #o interesse de querer sobrescrever de fato ou não, retorna o compromisso a ser sobrescrito mas também consegue 
    #cancelar operações.
    #OBS: A sobrescrição de compromissos semanais por outros compromissos semanais não é cobrida
    #OBS: Compromissos semanais sobrescritos por compromissos unitários podem ser voltados a ser mostrados no horário
    #em questão se os respectivos unitários forem EXCLUIDOS. Alterações não tão previstas nessa condição 
    ##################################################################################################################
    diacompromisso = datetime.strptime(novocompromisso[2], '%d/%m/%y')
    for compromisso in compromissos:
        if type(compromisso[1]) == str:
            if novocompromisso[2] == compromisso[2] and novocompromisso[0] != compromisso[0] and (int(compromisso[3][0]) <= int(novocompromisso[3][0]) < int(compromisso[3][0]) + int(compromisso[3][1]) \
                    or int(novocompromisso[3][0]) + int(novocompromisso[3][1]) > int(compromisso[3][0])):
                while True:
                    print('Existe um compromisso no mesmo horário. Deseja sobrescrever? (O compromisso em questão será apagado!:',compromisso[0],compromisso[2],'(s/n) ')
                    sn = input()
                    check = ValidacaoInput(sn,'sn')
                    if check == -1: break
                    elif check == -2: 
                        return -2
                if sn.lower() == 's':
                    return compromisso,'u'
                else: 
                    return -2
        else:
            fimperiodo = datetime.strptime(compromisso[2][1],'%d/%m/%y')
            inicioperiodo = datetime.strptime(compromisso[2][0],'%d/%m/%y')
            if fimperiodo >= diacompromisso and inicioperiodo <= diacompromisso:
                semana = ['segunda','terca','quarta','quinta','sexta','sabado','domingo']
                for diasemana in compromisso[1]:
                    if diasemana.lower() == semana[diacompromisso.weekday()] and novocompromisso[0] != compromisso[0] and (int(compromisso[3][0]) <= int(novocompromisso[3][0]) < int(compromisso[3][0]) + int(compromisso[3][1]) \
                    or int(novocompromisso[3][0]) + int(novocompromisso[3][1]) > int(compromisso[3][0]) > int(novocompromisso[3][0])):
                        while True:
                            print('Existe um compromisso no mesmo horário. Deseja sobrescrever?\n (O compromisso em questão vai ser substituido na respectiva data):\n',compromisso[0],novocompromisso[2],novocompromisso[3][0],int(novocompromisso[3][0])+int(novocompromisso[3][1]),'-(s/n) ',sep='-')
                            sn = input()
                            check = ValidacaoInput(sn,'sn')
                            if check == -1: break
                            elif check == -2: return -2
                        if sn.lower() == 's':
                            return compromisso,'s'
                        else:
                            return -2
    return -1

def MontarCalendario(unitario,semanal,opc):
    #####################################################################################################################
    #Função responsavel pela montagem e formatação do calendário da semana
    #Variavél semanaasermostrada se igual a 0, orienta o programa a mostrar o compromisso da semana atual cronologicamente
    #Monta primeiramente um calendário de dicicionares preenchendo todos os dias e horários com '-------', depois vem
    #Adicionando os compromissos semanais e por fim os compromissos unitários
    #######################################################################################################################
    semana = ['segunda','terca','quarta','quinta','sexta','sabado','domingo']
    semanaasermostrada = 1

    if opc != '1':
        print('1 - Exibir compromissos da semana atual')
        print('2 - Buscar compromissos de uma semana qualquer')
        print('3 - Lembretes')
        print('4 - Voltar')
        opc = input()


    if opc == '1':
        semanaasermostrada = 0
    elif opc == '2':
        while True:
            print('Digite um dia do mês do qual deseja ver os compromisso da respectiva semana (Ex: 25/06/23): ')
            dia = input()
            check = ValidacaoInput(dia,'diamesano')
            if check == -1: break
            elif check == -2: return
        semanaasermostrada = 1
        dia = datetime.strptime(dia,'%d/%m/%y')
        iniciodasemana = dia-timedelta(days=dia.weekday())
        fimdasemana = dia+timedelta(days=6-dia.weekday())
    elif opc == '3':
        hoje = datetime.today()
        fimdasemana = hoje+timedelta(days=6)
        for compromisso in unitario:
            data = datetime.strptime(compromisso[2],'%d/%m/%y')
            if fimdasemana >= data >= hoje:
                if compromisso[1] == 's':
                    print('O compromisso: ',compromisso[0],'está marcado para a próxima',semana[data.weekday()].upper())
        return
    elif opc == '4':
        return               

    calendario = {'SEGUNDA':{},'TERCA':{},'QUARTA':{},'QUINTA':{},'SEXTA':{},'SABADO':{},'DOMINGO':{}}
    for dia in calendario:
        for hora in range(24):
            calendario[dia][hora] = '-------'

    if semanaasermostrada == 0:
        hoje = datetime.today().weekday()
        iniciodasemana = datetime.today()-timedelta(days=hoje)
        fimdasemana = datetime.today()+timedelta(days=6-hoje)

    for compromisso in semanal:
        inicioperiodo = datetime.strptime(compromisso[2][0],'%d/%m/%y')
        fimperiodo = datetime.strptime(compromisso[2][1],'%d/%m/%y')
        for dia in compromisso[1]:
            diasemana = semana.index(dia.lower())
            if inicioperiodo <= iniciodasemana + timedelta(days=diasemana) <= fimperiodo:
                horarioatual = int(compromisso[3][0])
                duration = int(compromisso[3][1])
                while duration > 0:
                    if horarioatual > 23:
                        print('A duração do compromisso',compromisso[0],'excedeu as horas do dia!')
                        break
                    calendario[dia.upper()][horarioatual] = compromisso[0]
                    horarioatual += 1
                    duration -= 1

    for compromisso in unitario:
        datacompromisso = datetime.strptime(compromisso[2],'%d/%m/%y')
        if iniciodasemana <= datacompromisso <= fimdasemana:
            datacompromisso = semana[datacompromisso.weekday()].upper()
            horarioatual = int(compromisso[3][0])
            duration = int(compromisso[3][1])
            while duration > 0:
                if horarioatual > 23:
                    print('A duração do compromisso',compromisso[0], 'excedeu as horas do dia!')
                    break
                calendario[datacompromisso][horarioatual] = compromisso[0]
                horarioatual += 1
                duration -= 1
    
    horascomcompromisso = []
    for hora in range(24):
        for diadasemana in calendario:
            if calendario[diadasemana][hora] != '-------':
                horascomcompromisso += [hora]
                break
    if len(horascomcompromisso) != 0:
        hora1 = horascomcompromisso[0]
        hora2 = horascomcompromisso[-1]
    else:
        print('\n\nVocê não tem compromisso marcados nesta semana!')
        return

    iniciodasemana = datetime.strftime(iniciodasemana,'%d/%m/%y')
    fimdasemana = datetime.strftime(fimdasemana,'%d/%m/%y')
    print('\nOBS: Compromissos únicos são capazes de sobrescrever outros compromissos,\nno entanto se compromissos semanais forem cadastrados em horários já usados,\neles vão ser substituidos pelo ultimo compromisso semanal adicionado.\nUm compromisso semanal nunca sobrescrevera um compromisso único!\n')
    print('\n\nCompromissos adicionados semanalmente só são contabilizados da data atual adiante!\n\n')
    print(f"{'Compromissos da Semana: ': ^30}{'|'}{iniciodasemana: >20}{'-': ^20}{fimdasemana: <20}{'|'}")
    print()
    print(f"{'XX:XX-XX:XX': <17}{'| '}{'Segunda': ^13}{'| '}{'Terça': ^13}{'| '}{'Quarta': ^13}{'| '}{'Quinta': ^13}{'| '}{'Sexta': ^13}{'| '}{'Sabado': ^13}{'| '}{'Domingo':^13}{'|'}")
    print(f"{'-':-^123}")
    for hora in range(hora1,hora2+1):
        if hora == 24:
            break
        if hora < 10:
            print('0',end='')
            if hora != 9:
                print(f"{hora}{':00-0'}{hora+1}{':00': <9}",end='')
            else:
                print(f"{hora}{':00-'}{hora+1}{':00': <9}",end='')
        else:
            print(f"{hora}{':00-'}{hora+1}{':00': <9}",end='')  
        for diadasemana in calendario:
            print(f"{'| '}{calendario[diadasemana][hora]: ^13}",end='')
        print('|')
        print(f"{'-':-^123}")


if __name__ == '__main__': 
    main()