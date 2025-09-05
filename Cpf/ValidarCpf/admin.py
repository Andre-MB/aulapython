def validar_cpf(cpf: str) -> bool:

    cpf = cpf.replace('.', '').replace('-', '')

    if not cpf.isdigit() or len(cpf) != 11:
        return False

    numeros = [int(d) for d in cpf]

    if numeros == numeros[::-1] or len(set(numeros)) == 1:
        return False

    resto1 = calcdigito(10, numeros)

    if resto1 != numeros[9]:
        return False

    resto2 = calcdigito(11, numeros)

    return resto2 == numeros[10]

def calcdigito(fator: int, cpf):
    soma = sum(cpf[i] * (fator - i) for i in range(fator - 1) )

    resto = (soma*10) % 11

    if resto == 10:
        resto = 0
    
    return resto


cpfs = [
    "123.456.789-12",  # inválido
    "529.982.247-25",  # válido
    "777.777.777-77",   # inválido (todos os dígitos iguais)
    "62067769308"
]

for cpf in cpfs:
    if validar_cpf(cpf):
        print(f"O CPF {cpf} é válido!")
    else:
        print(f"O CPF {cpf} é inválido!")