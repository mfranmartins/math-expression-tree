class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def tokenizar(expressao):
    tokens = []
    numero = ""
    for caractere in expressao:
        if caractere.isdigit() or caractere == ".":
            numero += caractere
        else:
            if numero != "":
                tokens.append(numero)
                numero = ""
            if caractere in "+-*/()":
                tokens.append(caractere)
            elif caractere.isspace():
                continue
            else:
                return None, caractere
    if numero != "":
        tokens.append(numero)
    return tokens, None

def precedencia(operador):
    if operador in "+-":
        return 1
    elif operador in "*/":
        return 2

while True:
    expressao = input("Digite uma expressão matemática: ")
    tokens, caractere_invalido = tokenizar(expressao)
    if caractere_invalido:
        print(f"'{caractere_invalido}' é um caractere inválido. Tente novamente.\n")
    else:
        print(tokens)
        break
