expressao = input("Digite uma  matemática: ")

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
                raise ValueError(f"Caractere inválido: {caractere}")
    if numero != "":
        tokens.append(numero)
    return tokens
tokens = tokenizar(expressao)
print(tokens)
