from datetime import datetime
def main():   

    disciplinas = LerArquivo()

    while True:
        opc = menu()
        if opc == '1':
            disciplinas = TratamentoDasDisciplinas(disciplinas)
        elif opc == '2':
            pass
        elif opc == '3':
            pass
        elif opc == '4':
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
                return '4'
            else:
                print('Digite uma opção válida! (1, 2, 3 ou 4)')
            
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
                    horario = input('Digite o horário de começo e o de término das aulas separados em espaço(Ex: 16:00 17:00): ').split()
                    if ValidacaoInput(horario,'horario') == -1: break
                while True:
                    periodo = input('Digite previsao de começo e término da disciplina (Ex: 23/04 22/07): ').split()
                    if ValidacaoInput(periodo,'periodo') == -1: break

                geral = [cod,nome,turma,dias,horario,periodo]
                disciplinas += [geral]
                EditarArquivo(disciplinas)
                
                again = ''
                while again.lower() != 's' and again.lower() != 'n':
                    again = input('Deseja adicionar outro filme?(s/n) ')
                    if again == 'n': 
                        return disciplinas
                    elif again == 's':
                        break
                    else:
                        print('Digite "s" ou "n" ')

        if opc == '2':
            while True:
                print('Informe de qual disciplina você quer alterar os dados: ')
                materias = []
                for disciplina in disciplinas:
                    materias += [disciplina[1].lower()]
                    print(disciplina[1])
                opc = input('\n')
                if opc.lower() not in materias:
                    again = ''
                    while again.lower() != 's' and again.lower() != 'n':
                        again = input('Disciplina inválida ou ausente.Ainda deseja alterar algum dado? ')
                        if again == 'n': return disciplinas
                        elif again == 's': continue
                        else: print('Digite "s" ou "n"')
                else:
                    for pos in range(len(materias)):
                        if materias[pos].lower() == opc.lower(): break

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
                        print('Você vai editar: ',disciplinas[pos][int(opc)-1])
                        if opc == '1':
                            while True:
                                cod = input('Digite o código da disciplina: ')
                                if ValidacaoInput(cod) == -1: break
                            disciplinas[pos][int(opc)-1] = cod
                        elif opc == '2':
                            while True:
                                nome = input('Digite o nome da disciplina: ')
                                if ValidacaoInput(nome) == -1: break
                            disciplinas[pos][int(opc)-1] = nome
                        elif opc == '3':
                            while True:
                                turma = input('Digita o nome da turma: ')
                                if ValidacaoInput(turma) == -1: break
                            disciplinas[pos][int(opc)-1] = turma
                        elif opc == '4':
                            while True:
                                dias = input('Digite os dias da semana separados em espaço (Ex: Terça Quinta): ').split()
                                if ValidacaoInput(dias,'dia') == -1: break
                            disciplinas[pos][int(opc)-1] = dias
                        elif opc == '5':
                            while True:
                                horario = input('Digite o horário de começo e o de término das aulas separados em espaço(Ex: 16:00 17:00): ').split()
                                if ValidacaoInput(horario,'horario') == -1: break
                            disciplinas[pos][int(opc)-1] = horario
                        elif opc == '6':
                            while True:
                                periodo = input('Digite previsao de começo e término da disciplina (Ex: 23/04 22/07): ').split()
                                if ValidacaoInput(periodo,'periodo') == -1: break
                            disciplinas[pos][int(opc)-1] = periodo
                        EditarArquivo(disciplinas)
                        print('Dados atualizados!')
                        return disciplina

        elif opc == '3':
            while True:
                print('Informe de qual disciplina você quer excluir: ')
                materias = []
                for disciplina in disciplinas:
                    materias += [disciplina[1].lower()]
                    print(disciplina[1])
                opc = input('\n')
                if opc.lower() not in materias:
                    again = ''
                    while again.lower() != 's' and again.lower() != 'n':
                        again = input('Disciplina inválida ou ausente.Ainda deseja remover alguma disciplina? ')
                        if again == 'n': return disciplinas
                        elif again == 's': continue
                        else: print('Digite "s" ou "n"')
                else:
                    ctz = input('Você tem certeza que deseja excluir essa disciplina da sua base de dados? Digite exatamente "SIM" se deseja prosseguir (OS DADOS SERÃO REMOVIDOS PERMANENTEMENTE\n E NÃO SERA CAPAZ RESTAURA-LOS NEM QUE JESUS VOLTE!) ')
                    if ctz == 'SIM':
                        for materia in range(len(materias)):
                            print(materias[materia][1],opc)
                            if opc.lower() == materias[materia]:
                                print('Cheguei?')
                                del disciplinas[materia]
                                print('Apagado :)')
                                break
                        EditarArquivo(disciplinas)
                    else:
                        print('Operação Cancelada!')

                return disciplinas
        elif opc == '4':
            return disciplinas 

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
            print('Dados insuficientes. Digite novamente!')
            return 4
        for hora in entrada:
            try:
                hora = datetime.strptime(hora,'%H:%M')
                return -1
            except ValueError:
                print('Horário Inexistente ou Formato inadequado. Digite novamente!')
                return 2
            
    elif tipo == 'periodo':
        if len(entrada) != 2:
            print('Dados insuficientes. Digite novamente!')
            return 4
        for data in entrada:
            try:
                data = datetime.strptime(data,'%d/%m')
                return -1
            except ValueError:
                print('Data(s) inexistentes ou em formato inadequado. Digite novamente!')
                return 3

    else: 
        return -1

        

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