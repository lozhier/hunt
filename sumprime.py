import sympy
import sys
import random

# Aumentando o limite de recursão para números grandes
sys.setrecursionlimit(10000)

# Função para gerar primos grandes aleatórios com n dígitos
def gerar_primos_aleatorios(digitos, limite_inferior=None, limite_superior=None):
    # Definir os limites de acordo com o número de dígitos
    limite_inferior = 10**(digitos - 1) if limite_inferior is None else limite_inferior
    limite_superior = 10**digitos if limite_superior is None else limite_superior
    
    # Gerar um número aleatório dentro do intervalo
    candidato = random.randint(limite_inferior, limite_superior)
    while True:
        # Encontrar o próximo primo maior ou igual ao candidato
        candidato = sympy.nextprime(candidato)
        if candidato >= limite_superior:
            break
        yield candidato

# Função para encontrar pares de primos P e Q que satisfaçam P + Q + 1 = P'
def encontrar_primos(digitos=1000, limite=1):
    contador = 0
    for p in gerar_primos_aleatorios(digitos):
        for q in gerar_primos_aleatorios(digitos):
            p_mais_q_mais_1 = p + q + 1
            if sympy.isprime(p_mais_q_mais_1):
                print(f'Encontrado: P = {p}, Q = {q}, P\' = {p_mais_q_mais_1}')
                contador += 1
                if contador >= limite:
                    return
    print(f'Encontrei {contador} pares de primos.')

# Modifique o número de dígitos para 1000 e defina o número máximo de pares a serem encontrados
encontrar_primos(digitos=1000, limite=1)
