from datetime import datetime
def main():   

    disciplinas = LerArquivo('disciplinascadastradas.txt')
    unitario = LerArquivo('unitarioscadastrados.txt')
    semanal = LerArquivo('semanaiscadastrados.txt')
    while True:
        opc = menu()
        if opc == '1':
            disciplinas = TratamentoDasDisciplinas(disciplinas)
        elif opc == '2':
            unitario,semanal = TratamentoDeCompromissos(unitario,semanal,disciplinas)
        elif opc == 3:
            PrintarSemana(semanal)
        elif opc == '4':
            EditarArquivo(disciplinas)
            EditarArquivo(unitario)
            EditarArquivo(semanal)
            break
            

def LerArquivo(nomarquivo):
    infosevento = []
    allarquivo = []
    #abre o arquivo com as variaveis se ele existir e retorna uma tupla com essas informações, em caso negativo cria
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
        infocadastrada = (open(nomarquivo,'w'))

    infocadastrada.close()
    return allarquivo

def menu():
    while True:
        print('\n'*2)
        print('Bom dia! O que deseja fazer agora?')
        print('1 - Adicionar, Editar ou Excluir disciplinas ao banco de dados.')
        print('2 - Adicionar, Editar ou Excluir compromissos ao seu calendario')
        print('3 - Acessar seu calendario')
        print('4 - Sair')
        while True:
            opc = input()
            if opc == '1':
                return '1'
            elif opc == '2':
                return '2'
            elif opc == '3':
                print('1 - Calendário')
                print('2 - Exibir compromissos da semana')
                print('3 - Buscar compromissos de uma semana')
                print('4 - Lembretes')
                print('5 - Voltar')
                return 3
            elif opc == '4':
                return '4'
            else:
                print('Digite uma opção válida! (1, 2, 3 ou 4)')
            
def TratamentoDasDisciplinas(disciplinas):

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
                    elif check == -2: return disciplinas
                if cod.lower() in coddisciplinascadastradas:
                    print('Código ja vinculado a uma disciplina! Códigos e nomes devem ser únicos!')
                    return disciplinas
                while True:
                    nome = input('Digite o nome da disciplina: ')
                    check = ValidacaoInput(nome) 
                    if check == -1: break
                    elif check == -2: return disciplinas
                if nome.lower() in nomedisciplinascadastradas:
                    print('Nome ja vinculado a uma disciplina! Códigos e nomes devem ser únicos!')
                    return disciplinas
                while True:
                    turma = input('Digita o nome da turma: ')
                    check = ValidacaoInput(turma) 
                    if check == -1: break
                    elif check == -2: return disciplinas
                while True:
                    dias = input('Digite os dias da semana separados em espaço (Ex: Terça Quinta): ').split()
                    check = ValidacaoInput(dias,'dia') 
                    if check == -1: break
                    elif check == -2: return disciplinas
                while True:
                    horario = input('Digite o horário da aula e a duração em horas nessa ordem(Só aceitam valores inteiros - Ex: 16 1): ').split()
                    check = ValidacaoInput(horario,'horario') 
                    if check == -1: break
                    elif check == -2: return disciplinas
                while True:
                    periodo = input('Digite previsao de começo e término da disciplina (Ex: 23/04 22/07): ').split()
                    check = ValidacaoInput(periodo,'periodo') 
                    if check == -1: break
                    elif check == -2: return disciplinas
                geral = [cod,nome,turma,dias,horario,periodo]
                disciplinas += [geral]
                
                again = ''
                while again.lower() != 's' and again.lower() != 'n':
                    again = input('Deseja adicionar outra disciplina?(s/n) ')
                    if again == 'n': 
                        return disciplinas
                    elif again == 's':
                        break
                    else:
                        print('Digite "s" ou "n" ')

        elif opc == '2':
            while True:
                print('Informe de qual disciplina você quer alterar os dados: ')
                disciplina = OpcaoExistente(disciplinas,0)
                if disciplina != -1:
                    print('O que você deseja alterar?: ')
                    print('1 - Código da disciplina, 2 - Nome da disciplina, 3 - Nome da turma, 4 - Dias da semana, 5 - Horarios, 6 - Periodo')
                    opc = input('\n')
                    if opc != '1' and opc != '2' and opc != '3' and opc != '4' and opc != '5' and opc != '6':
                        again = ''
                        while again.lower() != 's' and again.lower() != 'n':
                            again = input('Atributo inválido ou ausente.Ainda deseja alterar algum dado? ')
                            if again == 'n': return disciplinas
                            elif again == 's': continue
                            else: print('Digite "s" ou "n"')
                    else:
                        print('Você vai editar: ',disciplinas[disciplina][int(opc)-1])
                        if opc == '1':
                            while True:
                                cod = input('Digite o código da disciplina: ')
                                check = ValidacaoInput(cod)
                                if check == -1: break
                                elif check == -2: return disciplinas
                            disciplinas[disciplina][int(opc)-1] = cod
                        elif opc == '2':
                            while True:
                                nome = input('Digite o nome da disciplina: ')
                                check = ValidacaoInput(nome) 
                                if check == -1: break
                                elif check == -2: return disciplinas
                            disciplinas[disciplina][int(opc)-1] = nome
                        elif opc == '3':
                            while True:
                                turma = input('Digita o nome da turma: ')
                                check = ValidacaoInput(turma) 
                                if check == -1: break
                                elif check == -2: return disciplinas
                            disciplinas[disciplina][int(opc)-1] = turma
                        elif opc == '4':
                            while True:
                                dias = input('Digite os dias da semana separados em espaço (Ex: Terça Quinta): ').split()
                                check = ValidacaoInput(dias,'dia') 
                                if check == -1: break
                                elif check == -2: return disciplinas
                            disciplinas[disciplina][int(opc)-1] = dias
                        elif opc == '5':
                            while True:
                                horario = input('Digite o horário da aula e a duração em horas nessa ordem (Só aceitam valores inteiros - Ex: 16 1): ').split()
                                check = ValidacaoInput(horario,'horario') 
                                if check == -1: break
                                elif check == -2: return disciplinas
                            disciplinas[disciplina][int(opc)-1] = horario
                        elif opc == '6':
                            while True:
                                periodo = input('Digite previsao de começo e término da disciplina (Ex: 23/04 22/07): ').split()
                                check = ValidacaoInput(periodo,'periodo') 
                                if check == -1: break
                                elif check == -2: return disciplinas
                            disciplinas[disciplina][int(opc)-1] = periodo
                        print('Dados atualizados!')
                        return disciplinas

        elif opc == '3':
            while True:
                print('Informe de qual disciplina você quer excluir: ')
                disciplina = OpcaoExistente(disciplinas,0)
                if disciplina != -1:
                    ctz = input('Você tem certeza que deseja excluir essa disciplina da sua base de dados? Digite exatamente "SIM" se deseja prosseguir (OS DADOS SERÃO REMOVIDOS PERMANENTEMENTE\n E NÃO SERA CAPAZ RESTAURA-LOS NEM QUE JESUS VOLTE!) ')
                    if ctz == 'SIM':
                        del disciplinas[disciplina]
                        print('Apagado :)')
                        break
                return disciplinas
        elif opc == '4':
            return disciplinas
        else: print('Digite uma opção válida! (1, 2, 3 ou 4)') 


def TratamentoDeCompromissos(unitario,semanal,disciplinas):
    compromissos = unitario + semanal
    print('O que deseja fazer: ')
    print('1 - Adicionar compromissos')
    print('2 - Editar Compromissos')
    print('3 - Excluir Compromissos')
    print('4 - Voltar')
    opc = input()
    while True: 
        if opc == '1':
            print('\n'*5)
            print('1 - Adicionar novo compromisso')
            print('2 - Adicionar disciplina do banco de dados aos compromisso')
            print('3 - Voltar')
            opc = input()
            if opc == '1':
                while True:
                    nome = input('Digite o nome do compromisso: ')
                    check = ValidacaoInput(nome) 
                    if check == -1: break
                    elif check == -2: return unitario,semanal
                for compromisso in compromissos:
                    if nome.lower() == compromisso[0].lower():
                        print('Compromisso já cadastrado! So é possível cadastrar compromissos com nomes diferentes')
                        return unitario,semanal

                while True:
                    horario = input('Hora de começo e duração separado por espaço (Somente numeros inteiros. Ex: 16 1) ').split()
                    check = ValidacaoInput(horario,'horario') 
                    if check == -1: break
                    elif check == -2: return unitario,semanal

                while True:
                    recorrencia = input('O compromisso tem recorrência semanal?(Se não quiser que ela seja removido passados a data digite "s"(s/n) ')
                    check = ValidacaoInput(recorrencia,'sn') 
                    if check == -1: break
                    elif check == -2: return unitario,semanal

                if recorrencia == 'n':
                    while True:
                        dia = input('Data do compromisso (Ex: "25/07"): ')
                        check = ValidacaoInput(dia,'diames') 
                        if check == -1: break
                        elif check == -2: return unitario,semanal
                        if ValidacaoInput(dia,'diames') == -2: return unitario,semanal
                    while True:
                        lembrete = input('Deseja adicionar um lembrete? (s/n)')
                        check = ValidacaoInput(lembrete,'sn') 
                        if check == -1: break
                        elif check == -2: return unitario,semanal
                    compromissounitario = [nome, lembrete,dia,horario]
                    unitario += [compromissounitario]
                    print('Adicionado')
                    return unitario,semanal
                else:
                    while True:
                        dia = input('Dia(s) da semana separados por espaço: ').split()
                        check = ValidacaoInput(dia,'dia') 
                        if check == -1: break
                        elif check == -2: return unitario,semanal

                    compromissosemanal = [nome,dia,horario]
                    semanal += [compromissosemanal]
                    print('Adicionado')
                    return unitario,semanal
            elif opc == '2':
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
                    compromissosemanal = [disciplinas[disciplina][1],disciplinas[disciplina][4],disciplinas[disciplina][5]]
                    semanal += [compromissosemanal]
                return unitario,semanal
            elif opc == '3':
                return unitario,semanal
            else:
                print('Digite uma opção válida! (1, 2 ou 3)')
                
        elif opc == '2':
            print('Qual compromisso você deseja editar? ')
            compromisso = OpcaoExistente(compromissos,0)
            if compromisso != -1:
                while True:
                    print('O que você deseja alterar? ')
                    print('1 - Nome')
                    print('2 - Dia')
                    print('3 - Horário')
                    print('4 - Recorrência')
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
                        if len(compromissos[compromisso]) == 4:
                            while True:
                                dia = input('Data do compromiso: ')
                                check = ValidacaoInput(dia,'diames')
                                if check == -1: break
                                elif check == -2: return unitario,semanal
                            compromissos[compromisso][len(compromissos[compromisso])-2] = dia                        
                        else:
                            while True:
                                dia = input('Dias da semana separados em espaço: ').split()
                                check = ValidacaoInput(dia,'dia') 
                                if check == -1: break
                                elif check == -2: return unitario,semanal
                            compromissos[compromisso][len(compromissos[compromisso])-2] = dia

                    elif opc == '3':
                        while True:
                            horario = input('Hora de começo e duração separado por espaço (Somente numeros inteiros. Ex: 16 1) ')
                            check = ValidacaoInput(horario,'horario') 
                            if check == -1: break
                            elif check == -2: return unitario,semanal
                        compromissos[compromisso][len(compromissos[compromisso])-1] = horario

                    elif opc == '4':
                        while True:
                            recorrencia = input('O compromisso tem recorrência semanal?(Se não quiser que ela seja removido passados a data digite "s"(s/n) ')
                            check = ValidacaoInput(recorrencia,'sn') 
                            if check == -1: break
                            elif check == -2: return unitario,semanal

                        if recorrencia == 'n':
                            while True:
                                lembrete = input('Deseja adicionar um lembrete? (s/n)')
                                check = ValidacaoInput(lembrete,'sn') 
                                if check == -1: break
                                elif check == -2: return unitario,semanal
                            compromissos[compromisso][1:1] = [lembrete]
                            print('Atualizado')
                        else:
                            if len(compromissos[compromisso]) == 4:
                                del compromissos[compromisso][1]
                            print('Atualizado')

                    elif opc == '5':
                        break
                    else:
                        print('Opção Inexistente! ')
                        continue
                    break
        elif opc == '3':
            print('Digite qual compromisso você deseja excluir: ')
            compromisso = OpcaoExistente(compromissos,0)
            if compromisso != -1:
                compromissos.pop(compromisso)

            
        unitario = []
        semanal = []
        for compromisso in compromissos:
            if len(compromisso) == 4:
                unitario += [compromisso]
            else:
                semanal += [compromisso]
        return unitario,semanal



def ValidacaoInput(entrada,tipo='nomes'):
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
    elif tipo == 'dia':
        for dia in entrada:
            existe = 'n'
            diasdasemana = ['domingo','segunda','terca','terça','quarta','quinta','sexta','sabado','sábado']
            for diadasemana in diasdasemana:
                if dia.lower() == diadasemana:
                    existe = 's'
                    break
            if existe == 'n':
                print('Dia da semana inexistente! Digite novamente')
                return 1 
        return -1
    elif tipo == 'diames':
        try:
            testedata = datetime.strptime(entrada,'%d/%m')
        except ValueError:
            print('Data inexistente. Digite novamente ou digite "b" para sair')
            return 1
        return -1
    elif tipo == 'horario':
        if len(entrada) != 2:
            print('Quantidade de dados imcompatível. Digite novamente ou digite "b" para sair')
            return 10
        for hora in entrada:
            try:
                hora = int(hora)
            except TypeError:
                print('Dados invalidos! Digite novamente ou digite "b" para sair')
                print(type(hora))
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
            print('Quantidade de dados imcompatível. Digite novamente ou digite "b" para sair')
            return 10
        for data in entrada:
            try:
                testedadata = datetime.strptime(data,'%d/%m')
                return -1
            except ValueError:
                print('Data(s) inexistentes ou em formato inadequado. Digite novamente ou digite "b" para sair')
                return 3
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
    opcoesvalidas = []
    for item in iteravel:
        opcoesvalidas += [item[posnome].lower()]
        print(item[posnome])
    opc = input()
    if opc.lower() not in opcoesvalidas:
        print('Opção Invalida')
        return -1
    else:
        for item in range(len(opcoesvalidas)):
            if opc.lower() == opcoesvalidas[item]:
                return item

        
def EditarArquivo(eventos):
    try:
        if len(eventos[0]) == 6:
            eventoscadastrados = open('disciplinascadastradas.txt','w')
        elif len(eventos[0]) == 3:
            eventoscadastrados = open('semanaiscadastrados.txt','w')
        elif len(eventos[0]) == 4:
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

def PrintarSemana(semanal):
    #diasdasemana = ['doming','segunda','terça','quarta','quinta','sexta','sabado']
    print('* %15s %15s %15s %15s %15s %15s %15s' %('|Domingo','|Segunda','|Terça','|Quarta','|Quinta','|Sexta','|Sabado'))


main()