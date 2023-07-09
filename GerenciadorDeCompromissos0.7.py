from datetime import datetime,timedelta,date
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
        elif opc == '3':
            MontarCalendario(unitario,semanal)
        elif opc == '4':
            EditarArquivo(disciplinas,'d')
            EditarArquivo(unitario,'u')
            EditarArquivo(semanal,'s')
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
                    periodo = input('Digite previsao de começo e término da disciplina (Ex: 23/04/22 22/07/22): ').split()
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
                                periodo = input('Digite previsao de começo e término da disciplina (Ex: 23/04/22 22/07/22): ').split()
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
    while True: 
        opc = input()
        if opc == '1':
            print('\n'*5)
            print('1 - Adicionar novo compromisso')
            print('2 - Adicionar disciplina do banco de dados aos compromisso')
            print('3 - Voltar')
            opc = input()
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
                    elif check[0] == 'n' or check[0] == -2:
                        print('Operação Cancelada!')
                        return unitario,semanal
                    else:
                        if check[1] == 'u':
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
                return unitario,semanal
            else:
                print('Digite uma opção válida! (1, 2 ou 3)')
                continue
                
        elif opc == '2':
            print('Qual compromisso você deseja editar? ')
            compromisso = OpcaoExistente(compromissos,0)
            if compromisso != -1:
                while True:
                    print('O que você deseja alterar?\n ')
                    for info in compromissos[compromisso]:
                        print(info)
                    print()
                    print('1 - Nome')
                    print('2 - Dia')
                    print('3 - Horário')
                    print('4 - Voltar')
                    opc = input()
                    if opc == '1':
                        while True:
                            nome = input('Digite o nome do compromisso: ')
                            check = ValidacaoInput(nome) 
                            if check == -1: break
                            elif check == -2: return unitario,semanal
                        compromissos[compromisso][0] = nome

                    elif opc == '2':
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
                            elif check[0] == 'n' or check[0] == -2:
                                print('Operação Cancelada!')
                                compromissos[compromisso][len(compromissos[compromisso])-2] = reverser
                                return unitario,semanal
                            else:
                                if check[1] == 'u':
                                    unitario.remove(check[0])
                                print('O compromisso:-',check[0][0],'- foi sobrescristo no horário em questão!')                        
                        else:
                            while True:
                                dia = input('Dia(s) da semana separados em espaço sem acentos nem caracteres especiais: ').split()
                                check = ValidacaoInput(dia,'dia') 
                                if check == -1: break
                                elif check == -2: return unitario,semanal
                            compromissos[compromisso][len(compromissos[compromisso])-3] = dia

                    elif opc == '3':
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
                            elif check[0] == 'n' or check[0] == -2:
                                print('Operação Cancelada!')
                                compromissos[compromisso][len(compromissos[compromisso])-1] = reverser
                                return unitario,semanal
                            else:
                                if check[1] == 'u':
                                    unitario.remove(check[0])
                                print('O compromisso:-',check[0][0],'- foi sobrescristo no horário em questão!')
                        else:
                            compromissos[compromisso][len(compromissos[compromisso])-1] = horario

                    elif opc == '4':
                        break
                    else:
                        print('Opção Inexistente! ')
                        continue
                    print('Atualizado!')
                    break
        elif opc == '3':
            print('Digite qual compromisso você deseja excluir: \n')
            compromisso = OpcaoExistente(compromissos,0)
            if compromisso != -1:
                print('O compromisso:-',compromissos[compromisso][0],'- foi excluido!')
                compromissos.pop(compromisso)
        elif opc == '4':
            return unitario,semanal
        else:
            print('Digite uma opção valida!(1,2,3 ou 4!)')
            continue

        unitario = []
        semanal = []
        for compromisso in compromissos:
            if type(compromisso[1]) == str:
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
                print('Data(s) inexistentes ou em formato inadequado. Digite novamente ou digite "b" para sair')
                return 3
        if data[0] > data[1]:
            print('Data(s) inexistentes ou em formato inadequado. Digite novamente ou digite "b" para sair')
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
    opcoesvalidas = []
    for item in iteravel:
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
                return item

        
def EditarArquivo(eventos,identificador):
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
    diacompromisso = datetime.strptime(novocompromisso[2], '%d/%m/%y')
    for compromisso in compromissos:
        if type(compromisso[1]) == str:
            if novocompromisso[2] == compromisso[2] and novocompromisso[3][0] == compromisso[3][0]:
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
                    if diasemana.lower() == semana[diacompromisso.weekday()] and compromisso[3][0] == novocompromisso[3][0]:
                        while True:
                            print('Existe um compromisso no mesmo horário. Deseja sobrescrever?\n (O compromisso em questão vai ser substituido na respectiva data):\n-',compromisso[0],novocompromisso[2] ,'-(s/n) ')
                            sn = input()
                            check = ValidacaoInput(sn,'sn')
                            if check == -1: break
                            elif check == -2: return -2
                        if sn.lower() == 's':
                            return compromisso,'s'
                        else:
                            return -2
    return -1

def MontarCalendario(unitario,semanal):
    semana = ['segunda','terca','quarta','quinta','sexta','sabado','domingo']
    semanaasermostrada = -1
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
                    print('O compromisso: ',compromisso[0],'está marcado para',semana[data.weekday()].upper(),'desta semana!')
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
        #iniciodasemana = datetime.strftime(datetime.today()-timedelta(days=hoje),'%d/%m/%y')
        #fimdasemana = datetime.strftime(datetime.today()+timedelta(days=6-hoje),'%d/%m/%y')
    for compromisso in semanal:
        inicioperiodo = datetime.strptime(compromisso[2][0],'%d/%m/%y')
        fimperiodo = datetime.strptime(compromisso[2][1],'%d/%m/%y')
        for dia in compromisso[1]:
            diasemana = semana.index(dia.lower())
            if compromisso[0] == 'Taekwondo':
                print('Taekyon')
                print(inicioperiodo, iniciodasemana + timedelta(days=diasemana),fimperiodo)
            if inicioperiodo <= iniciodasemana + timedelta(days=diasemana) <= fimperiodo:
                print('Taekyon')
                horarioatual = int(compromisso[3][0])
                duration = int(compromisso[3][1])
                while duration > 0:
                    if horarioatual > 23:
                        print('A duração do compromisso excedeu as horas do dia!')
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
                    print('A duração do compromisso excedeu as horas do dia!')
                    break
                calendario[datacompromisso][horarioatual] = compromisso[0]
                horarioatual += 1
                duration -= 1

    iniciodasemana = datetime.strftime(iniciodasemana,'%d/%m/%y')
    fimdasemana = datetime.strftime(fimdasemana,'%d/%m/%y')
    print('\nOBS: Compromissos únicos são capazes de sobrescrever outros compromissos,\nno entanto se compromissos semanais forem cadastrados em horários já usados,\neles vão ser substituidos pelo ultimo compromisso semanal adicionado.\nUm compromisso semanal nunca sobrescrevera um compromisso único!\n')
    print(f"{'Compromissos da Semana: ': ^30}{iniciodasemana: >20}{'-': ^20}{fimdasemana: <20}")
    print()
    print(f"{'XX:XX': <15}{'Segunda': ^14}{'Terça': ^14}{'Quarta': ^14}{'Quinta': ^14}{'Sexta': ^14}{'Sabado': ^14}{'Domingo':^14}")
    for hora in range(24):
        if hora < 10:
            print('0',end='')
        print(f"{hora}{':00': <13}",end='')
        for diadasemana in calendario:
            print(f"{calendario[diadasemana][hora]: ^13}",end=' ')
        print()


if __name__ == '__main__': 
    main()