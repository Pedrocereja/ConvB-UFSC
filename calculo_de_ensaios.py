import numpy as np
import cmath as cm
from scipy import interpolate

## todo: criar função para converter números em coordenadas polares

def par(z1, z2):
    ### Calcula a impedância equivalente de dois circuitos em paralelo
    aux = 1/z1 + 1/z2
    Zeq = 1/aux
    return Zeq

def p(nome, variavel = ""):
    ### Escreve uma variável em formato bonito no prompt
    if variavel=="":
        print("\n", nome)
    else:
        print(nome, " =", variavel)

# Ensaios do motor

def ensaios(Rt, Vz, Pr):
    ## A função calcula os parâmetros do circuito equivalente para um motor de indução trifásico e retorna os parâmetros R, X, rf e xm.
    ## Rt são os valores do ensaio com rotor travado, em que Rt = [Tensão de linha, Corrente de linha, Potência trifásica];
    ## Vz são os valores do ensaio em vazio, em que Vz = [Tensão de linha, Corrente de linha, Potência trifásica];
    ## Pr são os valores de potência em função da tensão de alimentação, em que Pr = [[V0, V1, V2, ...], [P0, P1, P2, ...]]

    ### Ensaio com rotor travado
    
    #### valores de fase
    V = Rt[0]/np.sqrt(3)
    I = Rt[1]
    P1f = Rt[2]/3

    Req = P1f/I**2
    Xeq = np.sqrt( (V/I)**2 - Req**2 )

    R = Req/2 #### assumimos que R1 = R2
    X = Xeq/2 #### assumimos que X1 = X2
    p("R1 e R2", R)
    p("X1 e X2", X)

    ### Perdas rotacionais

    f = interpolate.interp1d(Pr[0], Pr[1], kind = 'linear', fill_value='extrapolate')
    Prot = f(0)
    p("Perdas rotacionais", Prot)

    ### Ensaio a vazio

    V = Vz[0]/np.sqrt(3)
    I = Vz[1]
    P1f = Vz[2]/3

    Pferro = P1f - R*I**2 - Prot/3
    alpha = - np.arccos(P1f/(V*I))
    Vm = V - (R + 1j*X)*I*cm.rect(1, alpha)
    Ic = Pferro/V * cm.rect(1, cm.phase(Vm))
    Im = I*cm.rect(1, alpha) - Ic

    rf = abs(Vm/Ic)
    xm = abs(Vm/Im)
    p("rf", rf)
    p("xm", xm)

    return R, X, rf, xm

