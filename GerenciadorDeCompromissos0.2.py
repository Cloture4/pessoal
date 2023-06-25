def main():   

    compromissos = LerArquivo()

    while True:
        opc = menu()
        if opc == '1':
            compromissos = TratamentoDasDisciplinas(compromissos)
        elif opc == '2':
            pass
        elif opc == '3':
            pass
        elif opc == '4':
            pass
        elif opc == '5':
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
        print('Bom dia! O que deseja fazer agora?')
        print('1 - Adicionar, Editar ou Excluir disciplinas do seu calendario.')
        print('2 - Adicionar, Editar ou Excluir compromissos ao seu calendario')
        print('3 - Editar compromissos ou disciplinas')
        print('4 - Acessar seu calendario')
        print('5 - Sair')
        while True:
            opc = input()
            if opc == '1':
                return '1'
            elif opc == '2':
                return '2'
            elif opc == '3':
                return '3'
            elif opc == '4':
                print('1 - Calendário')
                print('2 - Exibir compromissos das semana')
                print('3 - Buscar compromissos de uma semana')
                print('4 - Lembretes')
                print('5 - Voltar')
            elif opc == '5':
                return '5'
            else:
                print('Digite uma opção válida! (1, 2, 3, 4 ou 5)')
            
def TratamentoDasDisciplinas(compromissos):

    #print('\n'*30)
    print('1 - Inserir disciplina')
    print('2 - Editar Disciplina')
    print('3 - Excluir Disciplina')
    print('4 - Voltar')

    while True:
        opc = input()
        if opc == '1':
            again = ''
            while again != 's' and again != 'n':
                #coleta as informações pro cadastro de disciplinas
                print('\n'*30)
                cod = input('Digite o código da disciplina: ')
                nome = input('Digite o nome da disciplina: ')
                turma = input('Digita o nome da turma: ')
                dias = input('Digite os dias da semana separados em espaço (Ex: Terça Quinta): ').split()
                horario = input('Digite o horário de começo e o de término das aulas separados em espaço(Ex: 16:00 17:00): ').split()
                periodo = input('Digite previsao de começo e término da disciplina (Ex: 23/04 22/07): ').split()

                geral = [cod,nome,turma,dias,horario,periodo]
                compromissos += [geral]
                EditarArquivo(compromissos)

                again = input('Deseja adicionar outro filme?(s/n) ')
                if again == 'n': 
                    return compromissos


        if opc == '2':
            pass
        if opc == '3':
            pass
        if opc == '4':
            return 

def EditarArquivo(compromissos):
    disciplinascasdatradas = open('disciplinascadastradas.txt','w')
    for compromisso in compromissos:
        
        for item in compromisso:

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