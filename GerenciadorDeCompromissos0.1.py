def main():
    #abre o arquivo com as variaveis se ele existir, em caso negativo cria
    try:
        disciplinascadastradas = (open('disciplinascadastradas.txt','r'))
    except:
        disciplinascadastradas = (open('disciplinascadastradas.txt','w'))

    while True:
        opc = menu()
        if opc == '1':
            disciplinascadastradas = TratamentoDasDisciplinas(disciplinascadastradas)
        elif opc == '2':
            pass
        elif opc == '3':
            pass
        elif opc == '4':
            break
        elif opc == '5':
            for i in disciplinascadastradas:
                print(i)
            disciplinascadastradas.close()
            break

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
                #while True:
                    #opc2 = input()
            elif opc == '5':
                return 5
            
def TratamentoDasDisciplinas(disciplinascadastradas):
    print('\n'*30)
    print('1 - Inserir disciplina')
    print('2 - Editar Disciplina')
    print('3 - Excluir Disciplina')
    print('4 - Voltar')
    while True:
        opc = input()
        if opc == '1':
            #coleta as informações pro cadastro de disciplinas
            print('\n'*30)
            cod = input('Digite o código da disciplina: ')
            nome = input('Digite o nome da disciplina: ')
            turma = input('Digita o nome da turma: ')
            dias = input('Digite os dias da semana separados em espaço (Ex: Terça Quinta): ')
            horario = input('Digite o horário de começo e o de término das aulas separados em espaço(Ex: 16 17): ')
            periodo = input('Digite previsao de começo e término da disciplina (Ex: 23/04 22/07): ')
            geral = [cod,nome,turma,dias,horario,periodo]
            
            for item in geral:
                disciplinascadastradas.write(item)
            again = input('Deseja adicionar outro filme?(s/n)')

            while again != 's' or again != 'n':
                again = input('Deseja adicionar outro filme?(s/n) ')
                if again == 's': continue
                elif again == 'n': return disciplinascadastradas
        if opc == '2':
            pass
        if opc == '3':
            pass
        if opc == '4':
            return 

main()