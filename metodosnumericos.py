#Recebe como entrada os valores y(0),t(0), h, quantidade de passos, a função. E calcula cada passo do método.
from sympy import *
from sympy.parsing.sympy_parser import parse_expr

def euler( y0, t0, h, passos, funcao ):
    t, y = symbols("t y")
    funcaoDerivada = parse_expr(funcao)
    passoatual = 0
    auxY = y0
    auxT = t0
    #escreva no arquivo y e t e passo atual
    while(passoatual <= passos):
        derivada = funcaoDerivada.subs(t, auxT)
        derivada = derivada.subs(y, auxY)
        auxT = auxT + h
        auxY = auxY + h*derivada
        print('PASSO: ', passoatual, ' T: ', auxT,' Y: ', auxY,' dY/dT: ', derivada)
        passoatual += 1

    return

def euler_inverso( y0, t0, h, passos, funcao ):
    #z é o novo y
    t, y, z = symbols("t y z")
    funcaoDerivada = parse_expr(funcao)
    passoatual = 0
    novoY = y0
    novoT = t0
    print('PASSO: ', passoatual, ' T: ', novoT,' Y: ', novoY)
    while(passoatual <= passos):
        #agora temos de atribuir os velhos valores, que ja foram impressos
        velhoY = novoY
        velhoT = novoT
        #novo valor de t
        novoT = velhoT + h
        #para calcular o novo valor de y, teremos de usar ele mesmo no calculo da derivada
        derivada = funcaoDerivada.subs(t, novoT)
        derivada = derivada.subs(y, z)
        novoY = solve(velhoY + h*derivada - z, z)[0]
        passoatual += 1
        print('PASSO: ', passoatual, ' T: ', novoT,' Y: ', novoY)
    return

def euler_aprimorado( y0, t0, h, passos, funcao ):
    t, y, z = symbols("t y z")


with open('../metodos/entrada.txt') as fp:
    line=fp.readline()
    #t, y = symbols("t y")

    while(line):        
        metodo = line.split(' ')[0]
        y0 = float(line.split(' ')[1])
        t0 = float(line.split(' ')[2])
        h = float(line.split(' ')[3])
        passos = int(line.split(' ')[4])
        funcao = line.split(' ')[5]
        #teste = sympy.parse_expr(funcao)
        #funcao = parse_expr(funcao)

        #funcao = funcao.subs(t, 0)
        print(metodo, y0, t0, h, passos, funcao)
        if(metodo == 'euler'):
            aux = euler(y0, t0, h, passos, funcao)
        elif(metodo == 'euler_inverso'):
            aux = euler_inverso (y0,t0,h,passos,funcao)
            
        # elif(metodo == 'euler_aprimorado'):
            
        # elif(metodo == 'runge_kutta'):
            
        # elif(metodo == 'adam_bashforth'):
            
        # elif(metodo == 'adam_bashforth_by_euler'):
            
        # elif(metodo == 'adam_bashforth_by_euler_inverso'):
            
        line=fp.readline()

