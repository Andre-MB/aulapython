import random

def createdCpf () :

    cpf = []
    
    for x in range(9):
        n = random.randint(0,9)
        cpf.append(n)
    
    cpf = calcdigito(10,cpf)

    cpf = calcdigito(11,cpf)
    
    print("".join(map(str,cpf)))

def calcdigito(fator: int, cpf):
    soma = sum(cpf[i] * (fator - i) for i in range(fator - 1) )

    resto = (soma*10) % 11

    if resto == 10:
        resto = 0

    cpf.append(resto)
    return cpf
        
createdCpf()