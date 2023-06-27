from datetime import datetime
def main():   

    disciplinas = LerArquivo()
    unitario = []
    semanal = []

    while True:
        opc = menu()
        if opc == '1':
            disciplinas = TratamentoDasDisciplinas(disciplinas)
        elif opc == '2':
            unitario,semanal = TratamentoDeCompromissos(unitario,semanal,disciplinas)
            print(unitario,semanal)
        elif opc == '3':
            pass
        elif opc == '4':
            pass
        elif opc == '5':
            EditarArquivo(disciplinas)
            break
        

def LerArquivo():
    infodisciplina = []
    alldisciplinas = []
    #abre o arquivo com as variaveis se ele existir e retorna uma tupla com essas informações, em caso negativo cria
    try:
        disciplinascadastradas = (open('disciplinascadastradas.txt','r'))
        for line in disciplinascadastradas:
            info = line.split(',')
            if len(info) == 4:
                infodisciplina += info[:3]
            elif len(info) == 3:
                infodisciplina += [info[:2]]
            elif len(info) == 1:
                alldisciplinas += [infodisciplina] 
                infodisciplina = []
    except FileNotFoundError:
        disciplinascadastradas = (open('disciplinascadastradas.txt','w'))

    disciplinascadastradas.close()
    return alldisciplinas

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
            elif opc == '4':
                pass
            elif opc == '5':
                return '5'
            else:
                print('Digite uma opção válida! (1, 2, 3, 4 ou 5)')
            
def TratamentoDasDisciplinas(disciplinas):

    print('\n'*10)
    print('1 - Inserir uma disciplina')
    print('2 - Editar informações de uma disciplina')
    print('3 - Excluir uma disciplina')
    print('4 - Voltar')

    while True:
        opc = input()
        if opc == '1':
            while True:
                #Coleta as informações pro cadastro de disciplinas
                print('\n'*10)
                while True:
                    cod = input('Digite o código da disciplina: ')
                    if ValidacaoInput(cod) == -1: break
                while True:
                    nome = input('Digite o nome da disciplina: ')
                    if ValidacaoInput(nome) == -1: break
                while True:
                    turma = input('Digita o nome da turma: ')
                    if ValidacaoInput(turma) == -1: break
                while True:
                    dias = input('Digite os dias da semana separados em espaço (Ex: Terça Quinta): ').split()
                    if ValidacaoInput(dias,'dia') == -1: break
                while True:
                    horario = input('Digite o horário da aula e a duração em horas nessa ordem(Só aceitam valores inteiros - Ex: 16 1): ').split()
                    if ValidacaoInput(horario,'horario') == -1: break
                while True:
                    periodo = input('Digite previsao de começo e término da disciplina (Ex: 23/04 22/07): ').split()
                    if ValidacaoInput(periodo,'periodo') == -1: break

                geral = [cod,nome,turma,dias,horario,periodo]
                disciplinas += [geral]
                
                again = ''
                while again.lower() != 's' and again.lower() != 'n':
                    again = input('Deseja adicionar outro filme?(s/n) ')
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
                                if ValidacaoInput(cod) == -1: break
                            disciplinas[disciplina][int(opc)-1] = cod
                        elif opc == '2':
                            while True:
                                nome = input('Digite o nome da disciplina: ')
                                if ValidacaoInput(nome) == -1: break
                            disciplinas[disciplina][int(opc)-1] = nome
                        elif opc == '3':
                            while True:
                                turma = input('Digita o nome da turma: ')
                                if ValidacaoInput(turma) == -1: break
                            disciplinas[disciplina][int(opc)-1] = turma
                        elif opc == '4':
                            while True:
                                dias = input('Digite os dias da semana separados em espaço (Ex: Terça Quinta): ').split()
                                if ValidacaoInput(dias,'dia') == -1: break
                            disciplinas[disciplina][int(opc)-1] = dias
                        elif opc == '5':
                            while True:
                                horario = input('Digite o horário da aula e a duração em horas nessa ordem (Só aceitam valores inteiros - Ex: 16 1): ').split()
                                if ValidacaoInput(horario,'horario') == -1: break
                            disciplinas[disciplina][int(opc)-1] = horario
                        elif opc == '6':
                            while True:
                                periodo = input('Digite previsao de começo e término da disciplina (Ex: 23/04 22/07): ').split()
                                if ValidacaoInput(periodo,'periodo') == -1: break
                            disciplinas[disciplina][int(opc)-1] = periodo
                        print('Dados atualizados!')
                        return disciplina

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


def TratamentoDeCompromissos(semanal,unitario,disciplinas):
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
                    if ValidacaoInput(nome) == -1: break
                while True:
                    dia = input('Dia(s) da semana: ').split()
                    if ValidacaoInput(dia,'dia') == -1: break
                while True:
                    horario = input('Hora de começo e duração separado por espaço (Somente numeros inteiros. Ex: 16 1) ').split()
                    if ValidacaoInput(horario,'horario') == -1: break
                while True:
                    recorrencia = input('O compromisso tem recorrência semanal?(Se não quiser que ela seja removido passados a data digite "s"(s/n) ')
                    if ValidacaoInput(recorrencia,'sn') == -1: break
                if recorrencia == 'n':
                    while True:
                        lembrete = input('Deseja adicionar um lembrete? (s/n)')
                        if ValidacaoInput(lembrete,'sn') == -1: break
                    unitario += [nome,lembrete,dia,horario]
                    print('Adicionado')
                    return unitario,semanal
                else:
                    semanal += [nome,dia,horario]
                    print('Adicionado')
                    return unitario,semanal
            elif opc == '2':
                if len(disciplinas) == 0:
                    print('Nenhuma disciplina cadastrada')
                    return
                print('Qual disciplina você quer adicionar? ')
                disciplina = OpcaoExistente(disciplinas,0)
                if disciplina != -1:
                    compromissosemanal = [disciplinas[disciplina][1],disciplinas[disciplina][4],disciplinas[disciplina][5]]
                    semanal += [compromissosemanal]
                return unitario,semanal
            elif opc == '3':
                return 3
            else:
                print('Digite uma opção válida! (1, 2 ou 3)')
        elif opc == '2':
            print('Qual compromisso você deseja editar? ')
            compromissos = unitario + semanal
            compromisso = OpcaoExistente(compromissos,0)
            if compromisso != -1:
                while True:
                    print('O que você deseja alterar? ')
                    print('1 - Nome')
                    print('2 - Dia(s) da Semana')
                    print('3 - Horário')
                    print('4 - Recorrência')
                    print('5 - Voltar')
                    opc = input()
                    if opc == '1':
                        while True:
                            nome = input('Digite o nome do compromisso: ')
                            if ValidacaoInput(nome) == -1: break
                        compromissos[compromisso][0] = nome
                    elif opc == '2':
                        while True:
                            dia = input('Dia(s) da semana: ')
                            if ValidacaoInput(dia,'dia') == -1: break
                        compromissos[compromissos][len(compromissos[compromissos])-2] = dia
                    elif opc == '3':
                        while True:
                            horario = input('Hora de começo e duração separado por espaço (Somente numeros inteiros. Ex: 16 1)')
                            if ValidacaoInput(horario,'horario') == -1: break
                        compromissos[compromisso][len(compromissos[compromissos])-1] = horario
                    elif opc == '4':
                        while True:
                            recorrencia = input('O compromisso tem recorrência semanal?(Se não quiser que ela seja removido passados a data digite "s"(s/n) ')
                            if ValidacaoInput(recorrencia,'sn') == -1: break
                        if recorrencia == 'n':
                            while True:
                                lembrete = input('Deseja adicionar um lembrete? (s/n)')
                                if ValidacaoInput(lembrete,'sn') == -1: break
                                compromissos[compromisso][1:1] = [lembrete]
                            print('Atualizado')
                        else:
                            if len(compromissos[compromisso]) == 4:
                                del compromissos[compromisso][1]
                            print('Atualizado')
                    unitario = []
                    semanal = []
                    for compromisso in compromissos:
                        if len(compromisso) == 4:
                            unitario += [compromisso]
                        else:
                            semanal += [compromisso]
                    return unitario,semanal
                    
                    




def ValidacaoInput(entrada,tipo='nomes'):
    if entrada == '' or entrada == '\n' or entrada == []:
        print('Entrada obrigatória, não é possivel deixar em branco. Digite novamente!')
        return 0
    elif tipo == 'dia':
        for dia in entrada:
            existe = 'n'
            diassemana = ['domingo','segunda','terca','terça','quarta','quinta','sexta','sabado','sábado']
            for feira in diassemana:
                if dia.lower() == feira:
                    existe = 's'
                    break
            if existe == 'n':
                print('Dia da semana inexistente!')
                return 1 
        return -1
    elif tipo == 'horario':
        if len(entrada) != 2:
            print('Quantidade de dados imcompatível. Digite novamente!')
            return 10
        for hora in entrada:
            try:
                hora = int(hora)
            except TypeError:
                print('Dados invalidos! Digite novamente! ')
                print(type(hora))
                return 20
        if not 24>= hora >= 0:
            print('Duração Irregular. Digite novamente!')
            return 200
        try:
            ehhora = datetime.strptime(entrada[0],'%H')
            return -1
        except ValueError:
            print('Horário Inexistente ou Formato inadequado. Digite novamente!')
            return 2            
    elif tipo == 'periodo':
        if len(entrada) != 2:
            print('Quantidade de dados imcompatível. Digite novamente!')
            return 10
        for data in entrada:
            try:
                data = datetime.strptime(data,'%d/%m')
                return -1
            except ValueError:
                print('Data(s) inexistentes ou em formato inadequado. Digite novamente!')
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

        
def EditarArquivo(disciplinas):
    disciplinascasdatradas = open('disciplinascadastradas.txt','w')
    for disciplina in disciplinas:
        
        for item in disciplina:

            if type(item) == str:
                disciplinascasdatradas.write(item)
                disciplinascasdatradas.write(',')
        
            if type(item) == list:
                disciplinascasdatradas.write('\n')

                for elemento in item:
                    disciplinascasdatradas.write(elemento)
                    disciplinascasdatradas.write(',')
        disciplinascasdatradas.write('\n\n')
    
    disciplinascasdatradas.close()

main()