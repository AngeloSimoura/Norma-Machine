import machines.fatorial
import machines.mult
import machines.soma
import Registradores

option='1'
instrucoes = {}
listRegistradores = {
    'A': Registradores.Registrador(0),
    'B': Registradores.Registrador(0),
    'C': Registradores.Registrador(0),
    'D': Registradores.Registrador(0),
}
currentInst = 'init'

def printStats():
        tVals = ''
        for k in listRegistradores:
            tVals += f'{k}:{listRegistradores[k].valor} '

        if not currentInst in instrucoes:
            print(f'\nValores finais: {tVals}')
        else:
            print(f"({tVals}) [Instrução({currentInst}): {instrucoes[currentInst][0]}]")
def programaInstrucoes():
        global currentInst
        currentInst = 'init'
        while  currentInst in instrucoes:
            inst = instrucoes[currentInst][0]
            reg = instrucoes[currentInst][1]

            if inst == 'ADD':
                listRegistradores[reg].add()

                currentInst = instrucoes[currentInst][2]

            elif inst == 'SUB':
                listRegistradores[reg].sub()

                currentInst = instrucoes[currentInst][2]

            elif inst == 'ZER':
                currentInst = instrucoes[currentInst][2] if (
                    listRegistradores[reg]).zer() == 1 else instrucoes[currentInst][3]
            printStats()


while(option!='0'):
    print('\n\nMáquina Norma')
    print("\n1 - Soma")
    print("2 - Multiplicação")
    print("3 - Fatorial")
    print("0 - Sair")
    option = input("\nInsira a opção desejada: ")

    if option == '0':
        print('\nFim do programa')
        exit()
    elif option == '1':
        print("Insira os valores para os registradores A e B")
        temp = int(input("A: "))
        listRegistradores['A'] = Registradores.Registrador(temp)
        temp = int(input("B: "))
        listRegistradores['B'] = Registradores.Registrador(temp)

        instrucoes = machines.soma.get()
        programaInstrucoes()
        
    elif option == '2':
        print("Insira os valores para os registradores A e B")
        temp = int(input("A: "))
        listRegistradores['A'] = Registradores.Registrador(temp)
        temp = int(input("B: "))
        listRegistradores['B'] = Registradores.Registrador(temp)

        instrucoes = machines.mult.get()
        programaInstrucoes()
        
    elif option == '3':
        print("Insira os valores para o registrador")
        temp = int(input("A: "))
        listRegistradores['A'] = Registradores.Registrador(temp)
        listRegistradores['B'] = Registradores.Registrador(0)

        instrucoes = machines.fatorial.get()
        programaInstrucoes()
        
    else:
        print('Opção não encontrada!')